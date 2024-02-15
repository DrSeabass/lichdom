import unittest

## I don't love doing this, but I want to be able to keep the tests separate from the root directory
## and I don't want to muck with sys in every file in a package to have the tests in-file.
import sys
sys.path.append(".")


from game.cards.card import Card, Suit, FaceValue

class TestCard(unittest.TestCase):
    def test_not_same_memory(self):
        card1 = Card(Suit.Spades, FaceValue.ACE)
        card2 = Card(Suit.Spades, FaceValue.ACE)
        self.assertTrue(card1 == card2)
        self.assertFalse(id(card1) == id(card2))

    def test_same_memory(self):
        card1 = Card(Suit.Spades, FaceValue.ACE)
        self.assertTrue(card1 == card1)
        self.assertTrue(id(card1) == id(card1))

    def test_not_same(self):
        card1 = Card(Suit.Spades, FaceValue.ACE)
        card2 = Card(Suit.Clubs, FaceValue.ACE)
        self.assertFalse(card1 == card2)
        self.assertFalse(id(card1) == id(card2))

    def test_copy_is_deep(self):
        card1 = Card(Suit.Spades, FaceValue.ACE)
        card2 = card1.copy()
        self.assertTrue(card1 == card2)
        card1.suit = Suit.Hearts
        self.assertFalse(card1 == card2)

    def test_dehydrate_hydrate(self):
        for suit in Suit:
            for value in FaceValue:
                card = Card(suit, value)
                data = card.dehydrate()
                expected = {
                    "suit": suit.name,
                    "value": value.name
                }
                self.assertEqual(data, expected)
                rehydrated = Card.hydrate(data)
                self.assertEqual(card, rehydrated)


if __name__ == '__main__':
    unittest.main()
