class Decks:
    def __init__(self, session, base_url):
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
        """returns A list of documents containing a bookmark.

        :return: _description_
        :rtype: _type_
        """
        response = self.session.get(self.base_url)
        response.raise_for_status()
        return response.json()["docs"]

    def update_deck(self, deck_id, **kwargs):
        response = self.session.post(f"{self.base_url}{deck_id}", json=kwargs)
        response.raise_for_status()
        return response.json()

    def delete_deck(self, deck_id):
        response = self.session.delete(f"{self.base_url}{deck_id}")
        response.raise_for_status()
        # return response.json()
