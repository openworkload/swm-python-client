"""Unit tests for SwmConnection (no network)."""

from pathlib import Path

import pytest

from swmclient.connection import SwmConnection


def _write_dummy_pem(path: Path) -> None:
    path.write_text("-----BEGIN CERTIFICATE-----\nMIIB\n-----END CERTIFICATE-----\n", encoding="utf-8")


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
