"""Unit tests for generated path builders (job_id URL encoding)."""

from typing import Any, Callable
from unittest.mock import MagicMock
from urllib.parse import quote

import pytest

from swmclient.generated.api.default import (
    delete_user_job_job_id,
    get_user_job_job_id,
    get_user_job_job_id_metrics,
    get_user_job_job_id_stderr,
    get_user_job_job_id_stdout,
    patch_user_job_job_id,
)


def _mock_client() -> MagicMock:
    client = MagicMock()
    client.base_url = "https://example:8443"
    client.get_headers.return_value = {}
    client.get_cookies.return_value = {}
    client.get_timeout.return_value = 5.0
    client.follow_redirects = False
    return client


@pytest.mark.parametrize(
    ("get_kwargs", "suffix", "extra"),
    [
        (get_user_job_job_id._get_kwargs, "", {}),
        (get_user_job_job_id_stdout._get_kwargs, "/stdout", {}),
        (get_user_job_job_id_stderr._get_kwargs, "/stderr", {}),
        (get_user_job_job_id_metrics._get_kwargs, "/metrics", {}),
        (delete_user_job_job_id._get_kwargs, "", {}),
        (patch_user_job_job_id._get_kwargs, "", {"modification": "requeue"}),
    ],
)
def test_job_id_path_param_is_url_encoded(
    get_kwargs: Callable[..., dict[str, Any]], suffix: str, extra: dict[str, Any]
) -> None:
    client = _mock_client()
    raw = "a/b?c#d e"
    kwargs = get_kwargs(job_id=raw, client=client, **extra)
    encoded = quote(raw, safe="")
    assert kwargs["url"] == f"https://example:8443/user/job/{encoded}{suffix}"
    assert "/user/job/a/b" not in kwargs["url"]


@pytest.mark.parametrize(
    ("get_kwargs", "suffix", "extra"),
    [
        (get_user_job_job_id._get_kwargs, "", {}),
        (get_user_job_job_id_stdout._get_kwargs, "/stdout", {}),
        (get_user_job_job_id_stderr._get_kwargs, "/stderr", {}),
        (get_user_job_job_id_metrics._get_kwargs, "/metrics", {}),
        (delete_user_job_job_id._get_kwargs, "", {}),
        (patch_user_job_job_id._get_kwargs, "", {"modification": "requeue"}),
    ],
)
def test_normal_job_id_unchanged_in_path(
    get_kwargs: Callable[..., dict[str, Any]], suffix: str, extra: dict[str, Any]
) -> None:
    client = _mock_client()
    job_id = "10000000-0000-0000-0000-000000000000"
    assert quote(job_id, safe="") == job_id
    kwargs = get_kwargs(job_id=job_id, client=client, **extra)
    assert kwargs["url"] == f"https://example:8443/user/job/{job_id}{suffix}"
