from requests.exceptions import HTTPError


class Cards:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = f"{base_url}cards/"

    def create_card(self, content, deck_id, **kwargs):
        # Combine required parameters with any additional keyword arguments
        payload = {
            "content": content,
            "deck-id": deck_id,
            **kwargs,  # This adds the optional parameters to the payload
        }
        response = self.session.post(self.base_url, json=payload)
        response.raise_for_status()
        return response.json()

    def get_card(self, card_id):
        try:
            response = self.session.get(f"{self.base_url}{card_id}")
            response.raise_for_status()
            return response.json()
        except HTTPError as e:
            # Log error, re-raise with more context, or handle accordingly
            raise Exception(f"Failed to get card with ID {card_id}: {e}")

    def list_cards(self):
        response = self.session.get(self.base_url)
        response.raise_for_status()
        return response.json()["docs"]

    def update_card(self, card_id, **kwargs):
        response = self.session.post(f"{self.base_url}{card_id}", json=kwargs)
        response.raise_for_status()
        return response.json()

    def delete_card(self, card_id):
        response = self.session.delete(f"{self.base_url}{card_id}")
        response.raise_for_status()
        return response.json()
