class Decks:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = f"{base_url}decks/"

    def create_deck(self, name, **kwargs):
        # Combine required parameters with any additional keyword arguments
        payload = {
            "name": name,
            **kwargs,  # This adds the optional parameters to the payload
        }
        response = self.session.post(self.base_url, json=payload)
        response.raise_for_status()
        return response.json()

    def get_deck(self, deck_id):
        response = self.session.get(f"{self.base_url}{deck_id}")
        response.raise_for_status()
        return response.json()

    def list_decks(self):
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
        return response.json()
