from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    job_id: str,
    *,
    client: Client,
    api_key: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/user/job/{jobId}".format(client.base_url, jobId=job_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if api_key is not UNSET:
        headers["api-key"] = api_key

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    job_id: str,
    *,
    client: Client,
    api_key: Union[Unset, str] = UNSET,
) -> Response[Any]:
    kwargs = _get_kwargs(
        job_id=job_id,
        client=client,
        api_key=api_key,
    )

    response = httpx.delete(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    job_id: str,
    *,
    client: Client,
    api_key: Union[Unset, str] = UNSET,
) -> Response[Any]:
    kwargs = _get_kwargs(
        job_id=job_id,
        client=client,
        api_key=api_key,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)
