"""Contains end user interface to make SWM API queries"""

from io import BytesIO
from typing import Any, Union, Optional

from .connection import SwmConnection
from .generated.types import File
from .generated.models.job import Job
from .generated.api.default import (
    get_user_job,
    get_user_node,
    post_user_job,
    get_user_image,
    get_user_flavor,
    get_user_remote,
    get_user_job_job_id,
    patch_user_job_job_id,
    delete_user_job_job_id,
    get_user_job_job_id_stderr,
    get_user_job_job_id_stdout,
)
from .generated.models.node import Node
from .generated.models.image import Image
from .generated.models.flavor import Flavor
from .generated.models.remote_site import RemoteSite
from .generated.models.post_user_job_multipart_data import PostUserJobMultipartData


class SwmApi:
    """Main class for all the API bindins."""

    def __init__(
        self, url: str, key_file: str, cert_file: str, ca_file: str, password: Union[str, None] = None
    ) -> None:
        self._conn = SwmConnection(url, key_file, cert_file, ca_file)
        headers = {"Accept": "application/json"}
        self._conn.establish(headers, password)

    def get_jobs(self) -> Optional[list[Job]]:
        if client := self._conn.get_auth_client():
            return get_user_job.sync(client=client)
        return None

    def get_job_stdout(self, job_id: str) -> Optional[Union[Any, File]]:
        if client := self._conn.get_auth_client():
            return get_user_job_job_id_stdout.sync(job_id=job_id, client=client)
        return None

    def get_job_stderr(self, job_id: str) -> Optional[Union[Any, File]]:
        if client := self._conn.get_auth_client():
            return get_user_job_job_id_stderr.sync(job_id=job_id, client=client)
        return None

    def get_job(self, job_id: str) -> Optional[Union[Any, File]]:
        if client := self._conn.get_auth_client():
            return get_user_job_job_id.sync(job_id=job_id, client=client)
        return None

    def get_flavors(self) -> Optional[list[Flavor]]:
        if client := self._conn.get_auth_client():
            return get_user_flavor.sync(client=client)
        return None

    def get_images(self) -> Optional[list[Image]]:
        if client := self._conn.get_auth_client():
            return get_user_image.sync(client=client)
        return None

    def get_nodes(self) -> Optional[list[Node]]:
        if client := self._conn.get_auth_client():
            return get_user_node.sync(client=client)
        return None

    def get_remote_sites(self) -> Optional[list[RemoteSite]]:
        if client := self._conn.get_auth_client():
            return get_user_remote.sync(client=client)
        return None

    def cancel_job(self, job_id: str) -> Optional[bytes]:
        if client := self._conn.get_auth_client():
            response = delete_user_job_job_id.sync_detailed(job_id=job_id, client=client)
            return response.content
        return None

    def requeue_job(self, job_id: str) -> Optional[bytes]:
        if client := self._conn.get_auth_client():
            response = patch_user_job_job_id.sync_detailed(job_id=job_id, client=client, modification="requeue")
            return response.content
        return None

    def submit_job(self, script_bytes: BytesIO) -> Optional[File]:
        if client := self._conn.get_auth_client():
            data = PostUserJobMultipartData(script_content=File(payload=script_bytes))
            return post_user_job.sync(client=client, multipart_data=data)
        return None
