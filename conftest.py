# tests/conftest.py
"""
This module sets up pytest fixtures for testing with the Mochi API client.
Fixtures:
    mochi_client: 
    A session-scoped fixture that provides an authenticated instance of the Mochi client.
    It retrieves the API key from the environment variable `MOCHI_API_KEY` and raises a
    ValueError if the variable is not set.
Dependencies:
    - pytest
    - os
    - mochi.client.Mochi
    - mochi.auth.Auth
"""
import pytest
from mochi.client import Mochi
from mochi.auth import Auth
import os

# tests/conftest.py or inside individual test files


@pytest.fixture(scope="session")
def mochi_client():
    """
    Fixture to create and return a Mochi client instance for the test session.

    This fixture retrieves the Mochi API key from the environment variable 
    'MOCHI_API_KEY'. If the environment variable is not set, it raises a 
    ValueError. The API key is then used to authenticate and create a Mochi 
    client instance.

    Returns:
        Mochi: An authenticated Mochi client instance.

    Raises:
        ValueError: If the 'MOCHI_API_KEY' environment variable is not set.
    """
    api_key = os.environ.get("MOCHI_API_KEY")
    if not api_key:
        raise ValueError("MOCHI_API_KEY environment variable not set")
    auth = Auth.Token(api_key)
    return Mochi(auth=auth)
