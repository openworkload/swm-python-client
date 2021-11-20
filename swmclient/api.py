"""Contains end user interface to make SWM API queries"""

from typing import Optional

from .connection import SwmConnection
from .generated.api.default import get_user_flavor, get_user_job, get_user_node, get_user_remote
from .generated.models.flavor import Flavor
from .generated.models.job import Job
from .generated.models.node import Node
from .generated.models.remote_site import RemoteSite


class SwmApi:
    def __init__(self, url: str, key_file: str, cert_file: str, ca_file: str, password: str = "") -> None:
        self._conn = SwmConnection(url, key_file, cert_file, ca_file)
        headers = {"Accept": "application/json"}
        self._conn.establish(headers, password)

    def get_jobs(self) -> Optional[list[Job]]:
        if (client := self._conn.get_auth_client()) is not None:
            return get_user_job.sync(client=client)
        return None

    def get_flavors(self) -> Optional[list[Flavor]]:
        if (client := self._conn.get_auth_client()) is not None:
            return get_user_flavor.sync(client=client)
        return None

    def get_nodes(self) -> Optional[list[Node]]:
        if (client := self._conn.get_auth_client()) is not None:
            return get_user_node.sync(client=client)
        return None

    def get_remote_sites(self) -> Optional[list[RemoteSite]]:
        if (client := self._conn.get_auth_client()) is not None:
            return get_user_remote.sync(client=client)
        return None
