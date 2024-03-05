from mochi.client import Mochi
from mochi.auth import Auth

auth = Auth.Token("token")
mochi = Mochi(auth=auth)


# list decks
decks = mochi.decks.list_decks()
print(decks)


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

# Working with templates
templates = mochi.templates.list_templates()
# if len(decks) < 1:

#     # Working with decks
#     new_deck = mochi.decks.create_deck(name="My new deck")
#     print(new_deck)


new_deck = mochi.decks.create_deck(name="Latin")

for card in cards:
    import time

    time.sleep(1)

    fields = {
        "name": {"id": "name", "value": card["front"]},
        "V72yjxYh": {"id": "V72yjxYh", "value": card["back"]},
        "5jSBGlOS": {"id": "5jSBGlOS", "value": card["mnemonic"]},
        "Vd2elLj0": {"id": "Vd2elLj0", "value": card["sentence"]},
    }

    print(f"## << {card['front']} >>\n---\n<< {card['back']} >>")
    # Working with cards
    new_card = mochi.cards.create_card(
        f"## << {card['front']} >>\n---\n<< {card['back']} >>",
        new_deck["id"],
        template_id="cpyLWrBm",
        fields=fields,
    )
    print(new_card)


# Working with cards
new_card = mochi.cards.create_card("New card content", (decks[0])["id"])
print(new_card)

# Working with templates
templates = mochi.templates.list_templates()
print(templates)
