"""
    Filename: models.py
    Description: Defines the data models for the Mochi API client.
    Author: Your Name <your.email@example.com>
    Date Created: November 16, 2024
    Version: 0.1.1
    Last Modified: November 16, 2024 by Your Name
    License: MIT License
    Dependencies:
        - json (standard library)
"""

import json


class BaseEntity:
    """
    BaseEntity class provides a method to convert the entity's attributes to a JSON string.

    Methods:
        to_json(): Converts the entity's attributes to a JSON string.
    """
    def to_json(self):
        """Convert entity to a JSON string."""
        return json.dumps(self.__dict__)


class CreateCard(BaseEntity):
    """
    A class used to represent a card to be created.
    Attributes
    ----------
    content : str
        The content of the card.
    deck_id : int
        The ID of the deck to which the card belongs.
    template_id : int, optional
        The ID of the template used for the card (default is None).
    archived : bool, optional
        Whether the card is archived (default is None).
    review_reverse : bool, optional
        Whether the card should be reviewed in reverse (default is None).
    pos : int, optional
        The position of the card (default is None).
    fields : dict, optional
        The fields of the card (default is an empty dictionary).
    attachments : list, optional
        The attachments of the card (default is an empty list).
    Methods
    -------
    add_field(field_id, value)
        Adds or updates a field for the card.
    add_attachment(file_name, content_type, data)
        Adds an attachment to the card.
    """
    def __init__(
        self,
        content,
        deck_id,
        template_id=None,
        archived=None,
        review_reverse=None,
        pos=None,
        fields=None,
        attachments=None,
    ):
        self.content = content
        self.deck_id = deck_id
        self.template_id = template_id
        self.archived = archived
        self.review_reverse = review_reverse
        self.pos = pos
        self.fields = fields or {}
        self.attachments = attachments or []

    def add_field(self, field_id, value):
        """Add or update a field for the card."""
        self.fields[field_id] = value

    def add_attachment(self, file_name, content_type, data):
        """Add an attachment to the card."""
        self.attachments.append(
            {"file-name": file_name, "content-type": content_type, "data": data}
        )
