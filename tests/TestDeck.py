import unittest

## I don't love doing this, but I want to be able to keep the tests separate from the root directory
## and I don't want to muck with sys in every file in a package to have the tests in-file.
import sys
sys.path.append(".")

from game.cards.deck import Deck

class TestDeck(unittest.TestCase):

    def test_deck_initializes_full(self):
        deck = Deck()
        self.assertEqual(len(deck), 52)

    def test_negative_fails(self):
        deck = Deck()
        with self.assertRaises(ValueError):
            deck.draw_many(-1)

    def test_zero_fails(self):
        deck = Deck()
        with self.assertRaises(ValueError):
            deck.draw_many(0)

    def test_too_many_fails(self):
        deck = Deck()
        with self.assertRaises(ValueError):
            deck.draw_many(len(deck) + 1)

    def test_draw_removes_expected_card_count(self):
        deck = Deck()
        deck_len = len(deck)
        to_draw = 3
        expected_len = deck_len - to_draw
        _ = deck.draw_many(to_draw)
        self.assertEqual(len(deck), expected_len)

    def test_draw_and_replace(self):
        deck = Deck()
        drawn = deck.draw_many(5)
        deck.push_many(drawn)

    def test_dehydrate_hydrate(self):
        deck = Deck()
        deck.shuffle()
        data = deck.dehydrate()
        rehydrated = Deck.hydrate(data)
        for card1, card2 in zip(deck.cards, rehydrated.cards):
            self.assertEqual(card1, card2)


if __name__ == "__main__":
    unittest.main()