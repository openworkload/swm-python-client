from http import HTTPStatus
from typing import Any, Dict, Union, Optional, cast

import httpx

from ... import errors
from ...types import Response
from ...client import Client
from ...models.job_metrics import JobMetrics


def _get_kwargs(
    job_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/user/job/{jobId}/metrics".format(client.base_url, jobId=job_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, JobMetrics]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = JobMetrics.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, JobMetrics]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_id: str,
    *,
    client: Client,
) -> Response[Union[Any, JobMetrics]]:
    """Job resource metrics

     Returns avg/max CPU, memory, and GPU metrics for a job, aggregated via
    PromQL against the configured Prometheus instance. Missing series are
    returned as JSON null.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, JobMetrics]]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, JobMetrics]]:
    """Job resource metrics

     Returns avg/max CPU, memory, and GPU metrics for a job, aggregated via
    PromQL against the configured Prometheus instance. Missing series are
    returned as JSON null.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, JobMetrics]
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: Client,
) -> Response[Union[Any, JobMetrics]]:
    """Job resource metrics

     Returns avg/max CPU, memory, and GPU metrics for a job, aggregated via
    PromQL against the configured Prometheus instance. Missing series are
    returned as JSON null.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, JobMetrics]]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, JobMetrics]]:
    """Job resource metrics

     Returns avg/max CPU, memory, and GPU metrics for a job, aggregated via
    PromQL against the configured Prometheus instance. Missing series are
    returned as JSON null.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, JobMetrics]
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
        )
    ).parsed
