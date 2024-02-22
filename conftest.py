# tests/conftest.py
import pytest
from mochi.client import Mochi
from mochi.auth import Auth

# tests/conftest.py or inside individual test files
import os
import pytest
from mochi.client import Mochi
from mochi.auth import Auth


@pytest.fixture(scope="session")
def mochi_client():
    api_key = os.environ.get("MOCHI_API_KEY")
    if not api_key:
        raise ValueError("MOCHI_API_KEY environment variable not set")
    auth = Auth.Token(api_key)
    return Mochi(auth=auth)
