def test_create_delete_cards(mochi_client):

    cards = mochi_client.cards.list_cards()

    # Working with decks
    new_deck = mochi_client.decks.create_deck(name="My new deck")
    print(new_deck)

    # Working with cards
    new_card = mochi_client.cards.create_card("New card content", new_deck["id"])
    print(new_card)

    mochi_client.cards.delete_card(new_card["id"])

    mochi_client.decks.delete_deck(new_deck["id"])
