import json


class BaseEntity:
    def to_json(self):
        """Convert entity to a JSON string."""
        return json.dumps(self.__dict__)


class CreateCard(BaseEntity):
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
