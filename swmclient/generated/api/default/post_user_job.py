from http import HTTPStatus
from io import BytesIO
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_user_job_multipart_data import PostUserJobMultipartData
from ...types import File, Response


def _get_kwargs(
    *,
    multipart_data: PostUserJobMultipartData,
) -> Dict[str, Any]:

    pass

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": "/user/job",
        "files": multipart_multipart_data,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, File]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = File(payload=BytesIO(response.content))

        return response_200
    if response.status_code == HTTPStatus.METHOD_NOT_ALLOWED:
        response_405 = cast(Any, None)
        return response_405
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
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
    *,
    client: Union[AuthenticatedClient, Client],
    multipart_data: PostUserJobMultipartData,
) -> Response[Union[Any, File]]:
    """Submit a new job script

     A new job is submitted with a specific job script

    Args:
        multipart_data (PostUserJobMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, File]]
    """

    kwargs = _get_kwargs(
        multipart_data=multipart_data,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    multipart_data: PostUserJobMultipartData,
) -> Optional[Union[Any, File]]:
    """Submit a new job script

     A new job is submitted with a specific job script

    Args:
        multipart_data (PostUserJobMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, File]
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    multipart_data: PostUserJobMultipartData,
) -> Response[Union[Any, File]]:
    """Submit a new job script

     A new job is submitted with a specific job script

    Args:
        multipart_data (PostUserJobMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, File]]
    """

    kwargs = _get_kwargs(
        multipart_data=multipart_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    multipart_data: PostUserJobMultipartData,
) -> Optional[Union[Any, File]]:
    """Submit a new job script

     A new job is submitted with a specific job script

    Args:
        multipart_data (PostUserJobMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, File]
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
