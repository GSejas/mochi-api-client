def test_create_delete_cards(mochi_client):

    cards = mochi_client.cards.list_cards()

    # Working with decks
    new_deck = mochi_client.decks.create_deck(name="My new deck")
    print(new_deck)

    cards = [
        {
            "front": "Labor",
            "back": "Work",
            "sentence": "Labor omnia vincit.",
            "mnemonic": "Imagine a labrador (Labor) in a lab coat working diligently at a desk.",
        },
        {
            "front": "Schola",
            "back": "School",
            "sentence": "Schola est fundamentum scientiae.",
            "mnemonic": "Picture a school of fish wearing scholar hats swimming through textbooks.",
        },
        {
            "front": "Magister",
            "back": "Teacher",
            "sentence": "Magister discipulis sapientiam tradit.",
            "mnemonic": "Visualize a magician (Magister) teaching rabbits out of his hat instead of pulling them out.",
        },
        {
            "front": "Liber",
            "back": "Book",
            "sentence": "Libri sunt amici optimi.",
            "mnemonic": "Imagine a book (Liber) with limbs, running to hug you like a best friend.",
        },
        {
            "front": "Medicus",
            "back": "Doctor",
            "sentence": "Medicus aegrotos curare debet.",
            "mnemonic": "Envision a medic duck (Medicus) waddling around with a stethoscope.",
        },
        {
            "front": "Bonus",
            "back": "Good",
            "sentence": "Bonus vir semper tirocinium amat.",
            "mnemonic": "Think of a bone (Bonus) giving a thumbs up for being a 'good boy'.",
        },
        {
            "front": "Novus",
            "back": "New",
            "sentence": "Novus rex, nova lex.",
            "mnemonic": "Picture a neon (Novus) sign flashing 'NEW' over a crown.",
        },
    ]

    for card in cards:
        import time

        time.sleep(1)
        # Working with cards
        new_card = mochi_client.cards.create_card(
            f"## << {card['front']} >>\n---\n<< {card['back']} >>",
            new_deck["id"],
            template_id="cpyLWrBm",
        )
        print(new_card)

    mochi_client.cards.delete_card(new_card["id"])

    mochi_client.decks.delete_deck(new_deck["id"])
