def test_create_delete_decks(mochi_client):

    decks = mochi_client.decks.list_decks()
