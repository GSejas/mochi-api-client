import pytest
import requests
from mochi.decks import Decks
from unittest.mock import patch


@pytest.fixture
def decks():
    """
    Creates and returns a Decks object initialized with a requests session and base URL.

    Returns:
        Decks: An instance of the Decks class initialized with a requests session and base URL.
    """
    session = requests.Session()
    base_url = "https://app.mochi.cards/api/"
    return Decks(session, base_url)


@patch("requests.Session.post")
def test_create_deck(mock_post, decks):
    """
    Test the create_deck method of the Decks class.

    This test mocks the requests.Session.post method to simulate the API response
    when creating a new deck. It verifies that the create_deck method returns the
    expected deck ID.

    Args:
        mock_post (MagicMock): Mock object for requests.Session.post.
        decks (Decks): Instance of the Decks class.

    Asserts:
        The response from create_deck contains the expected deck ID.
    """
    mock_post.return_value.json.return_value = {"id": "test_deck_id"}
    response = decks.create_deck("name")
    assert response["id"] == "test_deck_id"


@patch("requests.Session.get")
def test_get_deck(mock_get, decks):
    """
    Test the `get_deck` method of the `decks` object.

    This test mocks the `requests.Session.get` method to return a predefined JSON response.
    It then calls the `get_deck` method with a test deck ID and asserts that the returned
    response contains the expected deck ID.

    Args:
        mock_get (Mock): Mock object for `requests.Session.get`.
        decks (object): The object containing the `get_deck` method to be tested.
    """
    mock_get.return_value.json.return_value = {"id": "test_deck_id"}
    response = decks.get_deck("test_deck_id")
    assert response["id"] == "test_deck_id"


@patch("requests.Session.get")
def test_list_decks(mock_get, decks):
    """
    Test the list_decks method of the decks object.

    This test mocks the GET request to return a predefined JSON response
    and verifies that the list_decks method correctly processes the response.

    Args:
        mock_get (Mock): Mock object for the GET request.
        decks (object): The decks object being tested.

    Asserts:
        The ID of the first deck in the response is "test_deck_id".
    """
    mock_get.return_value.json.return_value = {"docs": [{"id": "test_deck_id"}]}
    response = decks.list_decks()
    assert response[0]["id"] == "test_deck_id"


@patch("requests.Session.post")
def test_update_deck(mock_post, decks):
    """
    Test the update_deck method of the Decks class.

    This test mocks the requests.Session.post method to simulate a successful
    API response when updating a deck. It verifies that the update_deck method
    returns the expected response.

    Args:
        mock_post (Mock): Mock object for requests.Session.post.
        decks (Decks): Instance of the Decks class.

    Asserts:
        The response from update_deck contains the expected deck ID.
    """
    mock_post.return_value.json.return_value = {"id": "test_deck_id"}
    response = decks.update_deck("test_deck_id", name="new name")
    assert response["id"] == "test_deck_id"


@patch("requests.Session.delete")
def test_delete_deck(mock_delete, decks):
    """
    Test the `delete_deck` method of the `decks` object.

    This test mocks the `requests.Session.delete` method to simulate a successful
    deck deletion with a 204 No Content status code. It verifies that the `delete_deck`
    method returns `None` when the deck is successfully deleted.

    Args:
        mock_delete (Mock): Mock object for `requests.Session.delete`.
        decks (object): The decks object with the `delete_deck` method to be tested.
    """
    mock_delete.return_value.status_code = 204
    response = decks.delete_deck("test_deck_id")
    assert response is None