"""Contains end user interface to make SWM API queries"""

from typing import Optional

from .connection import SwmConnection
from .generated.api.default import get_user_job
from .generated.models.job import Job


class SwmApi:
    def __init__(self, url: str, key_file: str, cert_file: str, ca_file: str, password: str = "") -> None:
        self._conn = SwmConnection(url, key_file, cert_file, ca_file)
        headers = {"Accept": "application/json"}
        self._conn.establish(headers, password)

    def get_jobs(self) -> Optional[list[Job]]:
        if (client := self._conn.get_auth_client()) is not None:
            return get_user_job.sync(client=client)
        return None
