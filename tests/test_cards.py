# # tests/test_cards.py
# def test_create_card(mochi_client):
#     # Assuming you have a mock or fake API setup
#     card_data = {"content": "Test card content", "deck_id": "test_deck_123"}
#     created_card = mochi_client.cards.create_card("Test card content")
#     assert created_card is not None
#     assert created_card["content"] == card_data["content"]
def test_create_card(mochi_client):

    decks = mochi_client.decks.list_decks()
