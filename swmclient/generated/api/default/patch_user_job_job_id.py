from http import HTTPStatus
from io import BytesIO
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import File, Response


def _get_kwargs(
    job_id: str,
    *,
    modification: str,
) -> Dict[str, Any]:
    headers = {}
    headers["modification"] = modification

    return {
        "method": "patch",
        "url": "/user/job/{jobId}".format(
            jobId=job_id,
        ),
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, File]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = File(payload=BytesIO(response.content))

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, File]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    modification: str,
) -> Response[Union[Any, File]]:
    """Update a job

     Modify the job state or properties

    Args:
        job_id (str):
        modification (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, File]]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        modification=modification,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    modification: str,
) -> Optional[Union[Any, File]]:
    """Update a job

     Modify the job state or properties

    Args:
        job_id (str):
        modification (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, File]
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
        modification=modification,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    modification: str,
) -> Response[Union[Any, File]]:
    """Update a job

     Modify the job state or properties

    Args:
        job_id (str):
        modification (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, File]]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        modification=modification,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    modification: str,
) -> Optional[Union[Any, File]]:
    """Update a job

     Modify the job state or properties

    Args:
        job_id (str):
        modification (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, File]
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
            modification=modification,
        )
    ).parsed
