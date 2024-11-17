import pytest
import requests
from mochi.template import Templates
from unittest.mock import patch
from tests.unit.tdata import mocked_template_list_response, mocked_single_template_response


@pytest.fixture
def templates():
    """
    Creates and returns a Templates object with a pre-configured session and base URL.

    Returns:
        Templates: An instance of the Templates class initialized with a requests session and the base URL for the Mochi API.
    """
    session = requests.Session()
    base_url = "https://app.mochi.cards/api/"
    return Templates(session, base_url)


@patch("requests.Session.get")
def test_get_template(mock_get, templates):
    """
    Test the `get_template` method of the `templates` object.

    Args:
        mock_get (Mock): Mock object for the `requests.get` method.
        templates (Templates): Instance of the `Templates` class.

    Setup:
        - Mocks the response of the `requests.get` method to return a predefined JSON response.

    Test:
        - Calls the `get_template` method with a specific template ID.
        - Asserts that the returned template's ID matches the expected template ID.
    """
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mocked_single_template_response
    response = templates.get_template("tc4BXsu5")
    assert response["id"] == "tc4BXsu5"


@patch("requests.Session.get")
def test_list_templates(mock_get, templates):
    """
    Test the `list_templates` method of the `templates` object.

    This test mocks the `requests.Session.get` method to return a predefined
    response when called. It then calls the `list_templates` method and asserts
    that the first template in the response has the expected ID.

    Args:
        mock_get (MagicMock): Mock object for `requests.Session.get`.
        templates (Templates): Instance of the `Templates` class being tested.

    Asserts:
        The ID of the first template in the response is "C0S8PCfz".
    """
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mocked_template_list_response
    response = templates.list_templates()
    assert response[0]["id"] == "C0S8PCfz"