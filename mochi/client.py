import requests
from .auth import Auth

# Assuming cards.py and decks.py are implemented
from .cards import Cards
from .decks import Decks
from .template import Templates


class Mochi:
    def __init__(self, auth, base_url="https://app.mochi.cards/api/"):
        self.session = requests.Session()
        self.session.headers.update(auth.get_headers())
        self.cards = Cards(self.session, base_url)
        self.decks = Decks(self.session, base_url)
        self.templates = Templates(self.session, base_url)

    def close(self):
        self.session.close()
