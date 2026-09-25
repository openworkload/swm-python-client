"""Contains end user interface to make SWM API queries"""

from io import BytesIO
from typing import Any, Optional, Union

from .connection import SwmConnection
from .generated.api.default import (
    delete_user_job_job_id,
    get_user_flavor,
    get_user_image,
    get_user_job,
    get_user_job_job_id,
    get_user_job_job_id_stderr,
    get_user_job_job_id_stdout,
    get_user_node,
    get_user_remote,
    patch_user_job_job_id,
    post_user_job,
)
from .generated.models.flavor import Flavor
from .generated.models.image import Image
from .generated.models.job import Job
from .generated.models.node import Node
from .generated.models.post_user_job_multipart_data import PostUserJobMultipartData
from .generated.models.remote_site import RemoteSite
from .generated.types import File


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

    def purge_jobs(self) -> Optional[bytes]:
        """Permanently remove all jobs for the authenticated user."""
        if client := self._conn.get_auth_client():
            import httpx

            response = httpx.request(
                "DELETE",
                f"{client.base_url}/user/job",
                headers=client.get_headers(),
                cookies=client.get_cookies(),
                timeout=max(client.get_timeout(), 300.0),
                follow_redirects=client.follow_redirects,
                verify=client.verify_ssl,
            )
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
            # Job submit can exceed the generated client's 5s default when SkyPort
            # is busy (Mnesia/topology); the job may still be accepted server-side.
            return post_user_job.sync(
                client=client.with_timeout(max(client.get_timeout(), 120.0)),
                multipart_data=data,
            )
        return None
