"""Contains class required to establish connections over SwmQuery"""

import pathlib
import ssl
import typing

from .generated.client import AuthenticatedClient


class SwmConnection:

    _client = None

    def __init__(self, url: str, key_file: str, cert_file: str, ca_file: str) -> None:
        self._ca_file = pathlib.Path(ca_file)
        self._key_file = pathlib.Path(key_file)
        self._cert_file = pathlib.Path(cert_file)
        self._url = url

        if not self._ca_file.exists():
            raise FileNotFoundError(f"No such file: {self._ca_file}")
        if not self._key_file.exists():
            raise FileNotFoundError(f"No such file: {self._key_file}")
        if not self._cert_file.exists():
            raise FileNotFoundError(f"No such file: {self._cert_file}")

    def establish(self, password: typing.Union[str, None] = None) -> None:
        if not self._client:
            ssl_context: ssl.SSLContext = ssl.create_default_context()
            ssl_context.verify_mode = ssl.CERT_REQUIRED
            ssl_context.load_verify_locations(cafile=str(self._ca_file))
            ssl_context.load_cert_chain(certfile=str(self._cert_file), keyfile=str(self._key_file), password=password)
            self._client = AuthenticatedClient(base_url=self._url, verify_ssl=ssl_context, token="")

    def get_auth_client(self) -> typing.Optional[AuthenticatedClient]:
        return self._client
