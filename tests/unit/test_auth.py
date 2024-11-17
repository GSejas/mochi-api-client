import pytest
from mochi.auth import Auth


def test_token_initialization():
    """
    Test the initialization of the Auth.Token class.

    This test verifies that the Auth.Token class correctly initializes
    with the provided API key.

    Assertions:
        - The api_key attribute of the Auth.Token instance should match
          the provided api_key.
    """
    api_key = "test_api_key"
    auth = Auth.Token(api_key)
    assert auth.api_key == api_key


def test_get_headers():
    """
    Unit test for the get_headers method of the Auth.Token class.

    This test verifies that the get_headers method returns a non-None value
    when provided with a valid API key.

    Steps:
    1. Create an instance of Auth.Token with a test API key.
    2. Call the get_headers method on the instance.
    3. Assert that the returned headers are not None.

    Raises:
        AssertionError: If the headers returned by get_headers are None.
    """
    api_key = "test_api_key"
    auth = Auth.Token(api_key)
    headers = auth.get_headers()
    assert headers is not None
