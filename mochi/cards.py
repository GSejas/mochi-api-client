"""
Filename: cards.py
Description: A client for interacting with the Cards API.
Author: Jorge Sequeira <jsequeira03@gmail.com>
Date Created: November 16, 2024
Version: 0.1.1
Last Modified: November 16, 2024 by Jorge Sequeira
License: MIT License
Dependencies:
    - requests (external library)
"""

from requests.exceptions import HTTPError


class Cards:
    """
    A class to interact with the Cards API.
    Attributes:
        session (requests.Session): The session object to make HTTP requests.
        base_url (str): The base URL for the Cards API.
    Methods:
        create_card(content, deck_id, **kwargs):
            Creates a new card with the given content and deck ID.
                content (str): The content of the card.
                deck_id (str): The ID of the deck to which the card belongs.
                **kwargs: Additional optional parameters for the card.
                dict: The JSON response from the server after creating the card.
        get_card(card_id):
            Retrieves a card with the given card ID.
                card_id (str): The ID of the card to be retrieved.
                dict: The JSON response from the server containing the card details.
                Exception: If the HTTP request returned an unsuccessful status code.
        list_cards(deck_id=None):
            Lists cards in pages of 10 cards per page. Use the bookmark attribute to request the next page.
            Optionally specify a deck-id to fetch only cards for that deck.
                deck_id (str, optional): The ID of the deck to filter cards by. Defaults to None.
                list: A list of card dictionaries.
        update_card(card_id, **kwargs):
            Updates a card with the given card ID using the provided keyword arguments.
        delete_card(card_id):
    """
    def __init__(self, session, base_url):
        """_summary_

        :param session: _description_
        :type session: _type_
        :param base_url: _description_
        :type base_url: _type_
        """
        self.session = session
        self.base_url = f"{base_url}cards/"

    def create_card(self, content, deck_id, **kwargs):
        """_summary_

        Example
        {
            "content": "New card from API. ![](@media/foobar03.png)",
            "deck-id": "btmZUXWM",
            "template-id": "8BtaEAXe",
            "fields": {
                "name": {
                "id": "name",
                "value": "Hello,"
                },
                "JNEnw1e7": {
                "id": "JNEnw1e7",
                "value": "World!"
                },
            },
            "review-reverse?": false,
            "archived?": false,
            "pos": "6V",
            "attachments": [
                {
                "file-name": "foobar03.png",
                "content-type": "image/png",
                "data": "iVBORw0KGgoAAAANSUhEUgAAACgAAAAkCAIAAAB0Xu9BAAAABGdBTUEAALGPC/xhBQAAAuNJREFUWEetmD1WHDEQhDdxRMYlnBFyBIccgdQhKVcgJeQMpE5JSTd2uqnvIGpVUqmm9TPrffD0eLMzUn+qVnXPwiFd/PP6eLh47v7EaazbmxsOxjhTT88z9hV7GoNF1cUCvN7TTPv/gf/+uQPm862MWTL6fff4HfDx4S79/oVAlAUwqOmYR0rnazuFnhfOy/ErMKkcBFOr1vOjUi2MFn4nuMil6OPh5eGANLhW3y6u3aH7ijEDCxgCvzFmimvc95TekZLyMSeJC68Bkw0kqUy1K87FlpGZqsGFCyqEtQNDdFUtFctTiuhnPKNysid/WFEFLE2O102XJdEE+8IgeuGsjeJyGHm/xHvQ3JtKVsGGp85g9rK6xMHtvHO9+WACYjk5vkVM6XQ6OZubCJvTfPicYPeHO2AKFl5NuF5UK1VDUbeLxh2BcRGKTQE3irHm3+vPj6cfCod50Eqv5QxtwBQUGhZhbrGVuRia1B4MNp6edwBxld2sl1splfHCwfsvCZfrCQyWmX10djjOlWJSSy3VQlS6LmfrgNvaieRWx1LZ6s9co+P0DLsy3OdLU3lWRclQsVcHJBcUQ0k9/WVVrmpRzYQzpgAdQcAXxZzUnFX3proannrYH+Vq6KkLi+UkarH09mC8YPr2RMWOlEqFkQClsykGEv7CqCUbXcG8+SaGvJ4a8d4y6epND+pEhxoN0vWUu5ntXlFb5/JT7JfJJqoTdy9u9qc7ax3xJRHqJLADWEl23cFWl4K9fvoaCJ2BHpmJ3s3z+O0U/DmzdMjB9alWZtg4e3yxzPa7lUR7nkvxLHO9+tvJX3mtSDpwX8GajB283I8R8a7D2MhUZr1iNWdny256yYLd52DwRYBtRMvE7rsmtxIUE+zLKQCDO4jlxB6CZ8M17GhuY+XTE8vNhQiIiSE82ZsGwk1pht4ZSpT0YVpon6EvevOXXH8JxVR78QzNuamupW/7UB7wO/+7sG5V4ekXb4cL5Lyv+4IAAAAASUVORK5CYII="
                }
            ]
        }

        :param content: _description_
        :type content: _type_
        :param deck_id: _description_
        :type deck_id: _type_
        :return: _description_
        :rtype: _type_
        """
        # Convert underscores to hyphens in kwargs keys
        kwargs_converted = {k.replace("_", "-"): v for k, v in kwargs.items()}
        # Combine required parameters with any additional keyword arguments
        payload = {
            "content": content,
            "deck-id": deck_id,
            **kwargs_converted,  # This adds the optional parameters to the payload
        }
        response = self.session.post(self.base_url, json=payload)
        response.raise_for_status()
        return response.json()

    def get_card(self, card_id):
        """_summary_

        Example:
        {
            "updated-at": {
                "date": "2021-09-11T14:23:53.250Z"
            },
            "tags": [],
            "content": "New card from API.",
            "name": null,
            "deck-id": "btmZUXWM",
            "pos": "00F",
            "references": [],
            "id": "QQJ8ssvL",
            "reviews": [],
            "created-at": {
                "date": "2021-09-10T01:29:49.879Z"
            },
            "new?": false,
            "archived?": true,
            "template-id": null
        }

        :param card_id: _description_
        :type card_id: _type_
        :raises Exception: _description_
        :return: _description_
        :rtype: _type_
        """
        try:
            response = self.session.get(f"{self.base_url}{card_id}")
            response.raise_for_status()
            return response.json()
        except HTTPError as e:
            # Log error, re-raise with more context, or handle accordingly
            raise Exception(f"Failed to get card with ID {card_id}: {e}")

    def list_cards(self, deck_id=None):
        """Lists cards in pages of 10 cards per page. Use the bookmark attribute to request the next page.

        Optionally specific a deck-id to fetch only cards for that deck.

        {
          "bookmark": "g1AAAABAeJzLYWBgYMpgSmHgKy5JLCrJTq2MT8lPzkzJBYpzGGY5BzimZYaD5Dlg8igyWQAw3xHv",
          "docs": [
            {
              "tags": [],
              "content": "# Hello, world!",
              "name": "Hello world",
              "deck-id": "eH53Hxe8",
              "fields": {},
              "pos": "1",
              "references": [],
              "id": "00UlY4dd",
              "reviews": [],
              "created-at": {
                "date": "2021-09-09T02:49:58.535Z"
              }
            },
            ...
          ]
        }

                :return: _description_
                :rtype: _type_
        """
        response = self.session.get(self.base_url)
        response.raise_for_status()
        return response.json()["docs"]

    def update_card(self, card_id, **kwargs):
        """
        Update a card with the given card_id using the provided keyword arguments.

        Args:
            card_id (str): The ID of the card to be updated.
            **kwargs: Arbitrary keyword arguments containing the fields to be updated.

        Returns:
            dict: The JSON response from the server after updating the card.

        Raises:
            requests.exceptions.HTTPError: If the HTTP request returned an unsuccessful status code.
        """
        response = self.session.post(f"{self.base_url}{card_id}", json=kwargs)
        response.raise_for_status()
        return response.json()

    def delete_card(self, card_id):
        """
        Deletes a card with the given card ID.

        Args:
            card_id (str): The ID of the card to be deleted.

        Raises:
            requests.exceptions.HTTPError: If the HTTP request returned an unsuccessful status code.
        """
        response = self.session.delete(f"{self.base_url}{card_id}")
        response.raise_for_status()