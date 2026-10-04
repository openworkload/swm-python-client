"""Unit tests for SwmApi wrappers (mocked connection, no network)."""

from io import BytesIO
from unittest.mock import MagicMock, patch

import pytest

from swmclient.api import SwmApi


@pytest.fixture
def api_with_mock_conn() -> tuple[SwmApi, MagicMock]:
    with patch("swmclient.api.SwmConnection") as conn_cls:
        conn = MagicMock()
        conn_cls.return_value = conn
        conn.get_auth_client.return_value = None
        api = SwmApi("https://example:8443", "key.pem", "cert.pem", "ca.pem")
        return api, conn


def test_get_jobs_returns_none_without_client(api_with_mock_conn: tuple[SwmApi, MagicMock]) -> None:
    api, _ = api_with_mock_conn
    assert api.get_jobs() is None


def test_get_jobs_calls_generated_sync(api_with_mock_conn: tuple[SwmApi, MagicMock]) -> None:
    api, conn = api_with_mock_conn
    client = MagicMock()
    conn.get_auth_client.return_value = client
    with patch("swmclient.api.get_user_job.sync", return_value=[]) as sync:
        assert api.get_jobs() == []
        sync.assert_called_once_with(client=client)


def test_cancel_job_calls_sync_detailed(api_with_mock_conn: tuple[SwmApi, MagicMock]) -> None:
    api, conn = api_with_mock_conn
    client = MagicMock()
    conn.get_auth_client.return_value = client
    detailed = MagicMock()
    detailed.content = b"ok"
    with patch("swmclient.api.delete_user_job_job_id.sync_detailed", return_value=detailed) as sync:
        assert api.cancel_job("job-1") == b"ok"
        sync.assert_called_once_with(job_id="job-1", client=client)


def test_submit_job_calls_post_user_job(api_with_mock_conn: tuple[SwmApi, MagicMock]) -> None:
    api, conn = api_with_mock_conn
    client = MagicMock()
    client.get_timeout.return_value = 30.0
    client.with_timeout.return_value = client
    conn.get_auth_client.return_value = client
    with patch("swmclient.api.post_user_job.sync", return_value=MagicMock()) as sync:
        result = api.submit_job(BytesIO(b"#!/bin/bash\n"))
        assert result is not None
        sync.assert_called_once()
        kwargs = sync.call_args.kwargs
        assert kwargs["client"] is client
        assert kwargs["multipart_data"] is not None


def test_get_job_metrics_returns_none_for_non_metrics(api_with_mock_conn: tuple[SwmApi, MagicMock]) -> None:
    api, conn = api_with_mock_conn
    client = MagicMock()
    conn.get_auth_client.return_value = client
    with patch("swmclient.api.get_user_job_job_id_metrics.sync", return_value="not-metrics"):
        assert api.get_job_metrics("job-1") is None


def test_purge_jobs_returns_none_without_client(api_with_mock_conn: tuple[SwmApi, MagicMock]) -> None:
    api, _ = api_with_mock_conn
    assert api.purge_jobs() is None
