"""Unit tests for SwmConnection (no network)."""

import datetime
import ssl
from pathlib import Path

import pytest
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID

from swmclient.connection import SwmConnection


def _write_dummy_pem(path: Path) -> None:
    path.write_text("-----BEGIN CERTIFICATE-----\nMIIB\n-----END CERTIFICATE-----\n", encoding="utf-8")


def _make_ca_and_client(
    tmp_path: Path, *, key_password: bytes | None = None
) -> tuple[Path, Path, Path]:
    """Write a one-off CA PEM plus a client cert/key signed by that CA."""
    ca_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    ca_name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "swm-test-ca")])
    now = datetime.datetime.now(datetime.timezone.utc)
    ca_cert = (
        x509.CertificateBuilder()
        .subject_name(ca_name)
        .issuer_name(ca_name)
        .public_key(ca_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - datetime.timedelta(minutes=1))
        .not_valid_after(now + datetime.timedelta(days=1))
        .add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
        .sign(ca_key, hashes.SHA256())
    )

    client_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    client_name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "swm-test-client")])
    client_cert = (
        x509.CertificateBuilder()
        .subject_name(client_name)
        .issuer_name(ca_name)
        .public_key(client_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - datetime.timedelta(minutes=1))
        .not_valid_after(now + datetime.timedelta(days=1))
        .sign(ca_key, hashes.SHA256())
    )

    ca_path = tmp_path / "ca.pem"
    cert_path = tmp_path / "cert.pem"
    key_path = tmp_path / "key.pem"

    ca_path.write_bytes(ca_cert.public_bytes(serialization.Encoding.PEM))
    cert_path.write_bytes(client_cert.public_bytes(serialization.Encoding.PEM))

    if key_password is None:
        encryption: serialization.KeySerializationEncryption = serialization.NoEncryption()
    else:
        encryption = serialization.BestAvailableEncryption(key_password)

    key_path.write_bytes(
        client_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=encryption,
        )
    )
    return ca_path, cert_path, key_path


def test_connection_raises_when_ca_missing(tmp_path: Path) -> None:
    key = tmp_path / "key.pem"
    cert = tmp_path / "cert.pem"
    _write_dummy_pem(key)
    _write_dummy_pem(cert)
    with pytest.raises(FileNotFoundError, match="No such file"):
        SwmConnection("https://example:8443", str(key), str(cert), str(tmp_path / "missing-ca.pem"))


def test_connection_raises_when_key_missing(tmp_path: Path) -> None:
    ca = tmp_path / "ca.pem"
    cert = tmp_path / "cert.pem"
    _write_dummy_pem(ca)
    _write_dummy_pem(cert)
    with pytest.raises(FileNotFoundError, match="No such file"):
        SwmConnection("https://example:8443", str(tmp_path / "missing-key.pem"), str(cert), str(ca))


def test_connection_constructs_with_existing_files(tmp_path: Path) -> None:
    ca = tmp_path / "ca.pem"
    key = tmp_path / "key.pem"
    cert = tmp_path / "cert.pem"
    _write_dummy_pem(ca)
    _write_dummy_pem(key)
    _write_dummy_pem(cert)

    conn = SwmConnection("https://example:8443", str(key), str(cert), str(ca))
    assert conn.get_auth_client() is None


def test_establish_trusts_only_cluster_ca(tmp_path: Path) -> None:
    ca_path, cert_path, key_path = _make_ca_and_client(tmp_path)
    conn = SwmConnection("https://example:8443", str(key_path), str(cert_path), str(ca_path))
    conn.establish({"Accept": "application/json"})

    client = conn.get_auth_client()
    assert client is not None
    ctx = client.verify_ssl
    assert isinstance(ctx, ssl.SSLContext)
    assert ctx.verify_mode == ssl.CERT_REQUIRED
    assert ctx.check_hostname is True
    assert len(ctx.get_ca_certs()) == 1

    # Regression lock: bare default context keeps the public CA store.
    default_ctx = ssl.create_default_context()
    assert len(default_ctx.get_ca_certs()) > 1


def test_establish_encrypted_key_with_password(tmp_path: Path) -> None:
    password = b"test-secret"
    ca_path, cert_path, key_path = _make_ca_and_client(tmp_path, key_password=password)
    conn = SwmConnection("https://example:8443", str(key_path), str(cert_path), str(ca_path))
    conn.establish({"Accept": "application/json"}, password=password.decode())
    assert conn.get_auth_client() is not None


def test_establish_encrypted_key_wrong_password_raises(tmp_path: Path) -> None:
    ca_path, cert_path, key_path = _make_ca_and_client(tmp_path, key_password=b"correct")
    conn = SwmConnection("https://example:8443", str(key_path), str(cert_path), str(ca_path))
    with pytest.raises((ssl.SSLError, OSError, ValueError, TypeError)):
        conn.establish({"Accept": "application/json"}, password="wrong")


def test_establish_encrypted_key_missing_password_raises(tmp_path: Path) -> None:
    ca_path, cert_path, key_path = _make_ca_and_client(tmp_path, key_password=b"correct")
    conn = SwmConnection("https://example:8443", str(key_path), str(cert_path), str(ca_path))
    # OpenSSL may raise SSLError or OSError (and may attempt a TTY prompt).
    with pytest.raises((ssl.SSLError, OSError, ValueError, TypeError)):
        conn.establish({"Accept": "application/json"})
