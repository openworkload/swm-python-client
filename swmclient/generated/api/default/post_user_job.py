from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.job_to_submit import JobToSubmit
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/user/job".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, JobToSubmit]]:
    if response.status_code == 200:
        response_200 = JobToSubmit.from_dict(response.json())

        return response_200
    if response.status_code == 405:
        response_405 = None

        return response_405
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, JobToSubmit]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[Any, JobToSubmit]]:
    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[Union[Any, JobToSubmit]]:
    """A new job is submitted with a specific job script"""

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[Any, JobToSubmit]]:
    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[Union[Any, JobToSubmit]]:
    """A new job is submitted with a specific job script"""

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed