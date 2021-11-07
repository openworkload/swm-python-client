"""Contains end user interface to make SWM API queries"""

import typing

from .connection import SwmConnection
from .generated.api.default import get_user_job
from .generated.client import AuthenticatedClient
from .generated.models.job import Job
from .generated.types import Response


class SwmApi:
    def __init__(self, url: str, key_file: str, cert_file: str, ca_file: str, password: str = "") -> None:
        self._conn = SwmConnection(url, key_file, cert_file, ca_file)
        self._conn.establish(password)

    async def get_jobs(self) -> typing.Optional[list[Job]]:
        if (client := self._conn.get_auth_client()) is not None:
            return await get_user_job.asyncio(client=client)
        return None
