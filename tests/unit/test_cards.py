import pytest
import requests
from mochi.cards import Cards
from unittest.mock import patch


@pytest.fixture
def cards():
    session = requests.Session()
    base_url = "https://app.mochi.cards/api/"
    return Cards(session, base_url)


@patch("requests.Session.post")
def test_create_card(mock_post, cards):
    mock_post.return_value.json.return_value = {"id": "test_card_id"}
    response = cards.create_card("content", "deck_id")
    assert response["id"] == "test_card_id"


@patch("requests.Session.get")
def test_get_card(mock_get, cards):
    """
    Test the get_card method of the cards object.

    Args:
        mock_get (Mock): Mock object for the requests.get method.
        cards (Cards): Instance of the Cards class.

    Test:
        - Mocks the response of the requests.get method to return a predefined JSON response.
        - Calls the get_card method with a test card ID.
        - Asserts that the returned card ID matches the test card ID.
    """
    mock_get.return_value.json.return_value = {"id": "test_card_id"}
    response = cards.get_card("test_card_id")
    assert response["id"] == "test_card_id"


@patch("requests.Session.get")
def test_list_cards(mock_get, cards):
    """
    Test the list_cards method of the cards object.

    Args:
        mock_get (Mock): Mock object for the requests.get method.
        cards (Cards): Instance of the Cards class.

    Returns:
        None

    Asserts:
        The first card's id in the response is "test_card_id".
    """
    mock_get.return_value.json.return_value = {"docs": [{"id": "test_card_id"}]}
    response = cards.list_cards()
    assert response[0]["id"] == "test_card_id"


@patch("requests.Session.post")
def test_update_card(mock_post, cards):
    """
    Test the update_card method of the cards object.

    Args:
        mock_post (Mock): Mock object for the post request.
        cards (Cards): Instance of the Cards class.

    Test:
        - Mocks the post request to return a predefined JSON response.
        - Calls the update_card method with a test card ID and new content.
        - Asserts that the response contains the expected card ID.
    """
    mock_post.return_value.json.return_value = {"id": "test_card_id"}
    response = cards.update_card("test_card_id", content="new content")
    assert response["id"] == "test_card_id"


@patch("requests.Session.delete")
def test_delete_card(mock_delete, cards):
    """
    Test the delete_card method of the cards object.

    Args:
        mock_delete (Mock): A mock object for the delete request.
        cards (Cards): An instance of the Cards class.

    Test:
        - Mocks the delete request to return a status code of 204 (No Content).
        - Calls the delete_card method with a test card ID.
        - Asserts that the response is None, indicating successful deletion.
    """
    mock_delete.return_value.status_code = 204
    response = cards.delete_card("test_card_id")
    assert response is None
