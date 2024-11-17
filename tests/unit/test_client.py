import pytest
import requests
from mochi.client import Mochi
from mochi.auth import Auth
from unittest.mock import patch


@pytest.fixture
def mochi_client():
    """
    Creates and returns an instance of the Mochi client with a test API key.

    Returns:
        Mochi: An instance of the Mochi client authenticated with a test API key.
    """
    api_key = "test_api_key"
    auth = Auth.Token(api_key)
    return Mochi(auth)


@patch("requests.Session")
def test_mochi_initialization(mock_session, mochi_client):
    """
    Test the initialization of the Mochi client.

    This test ensures that the Mochi client is initialized with the correct
    authorization header in the session.

    Args:
        mock_session (Mock): A mock of the requests.Session object.
        mochi_client (MochiClient): An instance of the MochiClient being tested.

    Assertions:
        Asserts that the 'Authorization' header in the Mochi client's session
        is not None.
    """
    mock_session.return_value.headers = {"Authorization": "Bearer test_api_key"}
    assert mochi_client.session.headers["Authorization"] is not None


@patch("requests.Session.close")
def test_mochi_close(mock_close, mochi_client):
    """
    Test the `close` method of the `mochi_client` to ensure it calls the `close` method of the `requests.Session`.

    Args:
        mock_close (MagicMock): Mock object for `requests.Session.close`.
        mochi_client (MochiClient): Instance of the `MochiClient` to be tested.

    Asserts:
        The `close` method of `requests.Session` is called exactly once.
    """
    mochi_client.close()
    mock_close.assert_called_once()