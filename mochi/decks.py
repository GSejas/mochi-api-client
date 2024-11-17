"""
Filename: decks.py
Description: A client for interacting with the Decks API.
Author: Jorge Sequeira <jsequeira03@gmail.com>
Date Created: November 16, 2024
Version: 0.1.1
Last Modified: November 16, 2024 by Jorge Sequeira
License: MIT License
Dependencies:
    - requests (external library)
"""


class Decks:
    """
    A client for interacting with the Decks API.
    Attributes:
    Methods:
        create_deck(name, **kwargs):
            Creates a new deck with the specified name and additional 
            properties.
                name (str): The name of the deck.
                **kwargs: Additional properties for the deck.
            Returns:
                dict: The created deck's details.
        get_deck(deck_id):
            Retrieves an existing deck by its ID.
                deck_id (str): The ID of the deck to retrieve.
            Returns:
                dict: The details of the retrieved deck.
        list_decks():
            Lists all decks.
            Returns:
                list: A list of documents containing deck details.
        update_deck(deck_id, **kwargs):
            Updates an existing deck with the specified properties.
                deck_id (str): The ID of the deck to update.
                **kwargs: The properties to update.
            Returns:
                dict: The updated deck's details.
        delete_deck(deck_id):
            Deletes an existing deck by its ID.
                deck_id (str): The ID of the deck to delete.
            Returns:
                None
    """
    def __init__(self, session, base_url):
        """
        Initializes the Decks client.

        Args:
            session (requests.Session): The session object to be used for making HTTP requests.
            base_url (str): The base URL for the API endpoint.
        """
        self.session = session
        self.base_url = f"{base_url}decks/"

    def create_deck(self, name, **kwargs):
        """Decks fundamentally act as collections of cards. In addition to cards, decks can also contain other decks to create heirarchies of content. There are also a number of properties on the deck that control how cards are displayed and reviewd.

        :param name: _description_
        :type name: _type_
        :return: _description_
        :rtype:
        {
            "name": "My new deck",
            "parent-id": "HJBMBGBO",
            "sort": 1,
            "archived?": true,
            "trashed?": "2012-04-23T18:25:43.511Z",
            "show-sides?": true,
            "sort-by-direction": true,
            "review-reverse?": true
        }
        """
        # Convert underscores to hyphens in kwargs keys
        kwargs_converted = {k.replace("_", "-"): v for k, v in kwargs.items()}
        # Combine required parameters with any additional keyword arguments
        payload = {
            "name": name,
            **kwargs_converted,  # This adds the optional parameters to the payload
        }
        response = self.session.post(self.base_url, json=payload)
        response.raise_for_status()
        return response.json()

    def get_deck(self, deck_id):
        """Retrieves a deck that already exists. The returned data will look identical to the data returned from the deck creation request.

        :param deck_id: _description_
        :type deck_id: _type_
        :return: _description_
        :rtype: _type_
        """
        response = self.session.get(f"{self.base_url}{deck_id}")
        response.raise_for_status()
        return response.json()

    def list_decks(self):
        """
        Retrieves a list of decks from the API.

        Sends a GET request to the base URL using the session object and returns the list of decks.

        Returns:
            list: A list of decks retrieved from the API.

        Raises:
            requests.exceptions.HTTPError: If the HTTP request returned an unsuccessful status code.
        """
        response = self.session.get(self.base_url)
        response.raise_for_status()
        return response.json()["docs"]

    def update_deck(self, deck_id, **kwargs):
        """
        Update a deck with the given deck_id using the provided keyword arguments.

        Args:
            deck_id (str): The ID of the deck to update.
            **kwargs: Arbitrary keyword arguments containing the fields to update.

        Returns:
            dict: The JSON response from the server after updating the deck.

        Raises:
            requests.exceptions.HTTPError: If the HTTP request returned an unsuccessful status code.
        """
        response = self.session.post(f"{self.base_url}{deck_id}", json=kwargs)
        response.raise_for_status()
        return response.json()

    def delete_deck(self, deck_id):
        """
        Deletes a deck with the specified deck_id.

        Args:
            deck_id (str): The ID of the deck to be deleted.

        Raises:
            requests.exceptions.HTTPError: If the HTTP request returned an unsuccessful status code.
        """
        response = self.session.delete(f"{self.base_url}{deck_id}")
        response.raise_for_status()
