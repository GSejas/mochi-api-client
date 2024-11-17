"""
Filename: client.py
Description: A client for interacting with the Mochi API.
Author: Jorge Sequeira <jsequeira03@gmail.com>
Date Created: November 16, 2024
Version: 0.1.1
Last Modified: November 16, 2024 by Jorge Sequeira
License: MIT License
Dependencies:
    - requests (external library)

## Sequence Diagram for Creating a Card
```mermaid
sequenceDiagram
    participant User
    participant MochiClient as Mochi Client
    participant CardsAPI as Cards API
    User->>MochiClient: create_card(content, deck_id, kwargs)
    MochiClient->>CardsAPI: POST /cards
    CardsAPI-->>MochiClient: 201 Created
    MochiClient-->>User: New card details
```

## Class Diagram
```mermaid
classDiagram
    class Mochi {
        -session: Session
        -cards: Cards
        -decks: Decks
        -templates: Templates
        +__init__(auth: Auth, base_url: str)
        +close()
    }
    class Auth {
        +Token(api_key: str)
    }
    class Cards {
        +__init__(session: Session, base_url: str)
        +create_card(content: str, deck_id: str, kwargs: dict)
        +get_card(card_id: str)
        +update_card(card_id: str, kwargs: dict)
        +delete_card(card_id: str)
        +list_cards(deck_id: str)
    }
    class Decks {
        +__init__(session: Session, base_url: str)
        +create_deck(name: str, kwargs: dict)
        +get_deck(deck_id: str)
        +update_deck(deck_id: str, kwargs: dict)
        +delete_deck(deck_id: str)
        +list_decks()
    }
    class Templates {
        +__init__(session: Session, base_url: str)
        +get_template(template_id: str)
        +list_templates()
    }
    Mochi --> Auth
    Mochi --> Cards
    Mochi --> Decks
    Mochi --> Templates
```
"""

import requests
from .auth import Auth

# Assuming cards.py and decks.py are implemented
from .cards import Cards
from .decks import Decks
from .template import Templates
from .constant import MOCHI_BASE_API


class Mochi:
    """
    A client for interacting with the Mochi API.
    Attributes:
        session (requests.Session): The session used for making HTTP requests.
        cards (Cards): The Cards API client.
        decks (Decks): The Decks API client.
        templates (Templates): The Templates API client.
    Args:
        auth (Auth): An authentication object that provides the necessary
        headers.
        base_url (str, optional): The base URL for the Mochi API. Defaults to 
        MOCHI_BASE_API.
    Methods:
        close(): Closes the session.
    """

    def __init__(self, auth, base_url=MOCHI_BASE_API):
        """
        Initializes the client with authentication and base URL.

        Args:
            auth (Auth): An authentication object that provides the necessary headers.
            base_url (str, optional): The base URL for the Mochi API. Defaults to MOCHI_BASE_API.

        Attributes:
            session (requests.Session): The session object used for making HTTP requests.
            cards (Cards): The Cards API client.
            decks (Decks): The Decks API client.
            templates (Templates): The Templates API client.
        """
        self.session = requests.Session()
        self.session.headers.update(auth.get_headers())
        self.cards = Cards(self.session, base_url)
        self.decks = Decks(self.session, base_url)
        self.templates = Templates(self.session, base_url)

    def close(self):
        """
        Closes the current session.

        This method should be called to properly close the session and release any
        resources associated with it.
        """
        self.session.close()
