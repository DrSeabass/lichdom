from card import Suit, FaceValue, Card
from copy import deepcopy
import random
import unittest


class Deck:

    def __init__(self):
        self.cards = []
        for suit in Suit:
            for value in FaceValue:
                self.cards.append(Card(suit, value))

    def __len__(self):
        return len(self.cards)

    def __eq__(self, other):
        if not type(self) == type(other):
            return False
        elif not len(self) == len(other):
            for c1, c2 in zip(self.cards, other.cards):
                if c1 != c2:
                    return False
        return True

    def copy(self):
        return deepcopy(self)

    def push_many(self, to_add: list):
        for card in to_add:
            assert (type(card) == Card)
            if card in self.cards:
                raise ValueError("Decks cannot contain duplicate cards.  Deck already had {}.".format(card))
        self.cards = to_add + self.cards

    def push(self, card: Card):
        self.push_many([card])

    def shuffle(self):
        # Shuffle is in-place
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)

    def draw_many(self, count):
        if count > len(self):
            raise ValueError("Can't draw more cards({}) than in the deck({})!".format(count, len(self)))
        elif count <= 0:
            raise ValueError("Can't draw no or negative cards.")
        drawn = []
        for i in range(count):
            drawn.append(self.draw())
        return drawn


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


if __name__ == "__main__":
    unittest.main()
