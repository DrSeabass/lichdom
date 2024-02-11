import random
from copy import deepcopy
from enum import Enum
import unittest


class Theme(Enum):
    MUNDANE = 0
    ARCANE = 1

    def __str__(self):
        match self:
            case Theme.MUNDANE:
                return "Mundane"
            case Theme.ARCANE:
                return "Arcane"
            case _:
                raise TypeError("Unexpected value {}".format(self))


class Suit(Enum):
    SPADES = 0
    CLUBS = 1
    HEARTS = 2
    DIAMONDS = 3

    @staticmethod
    def get_suit_theme(suit):
        match suit:
            case Suit.SPADES:
                return Theme.ARCANE
            case Suit.CLUBS:
                return Theme.ARCANE
            case Suit.HEARTS:
                return Theme.MUNDANE
            case Suit.DIAMONDS:
                return Theme.MUNDANE
            case _:
                raise TypeError("Unexpected value {}".format(suit))

    def get_theme(self):
        return Suit.get_suit_theme(self)

    def __str__(self):
        match self:
            case Suit.SPADES:
                return "of Spades"
            case Suit.CLUBS:
                return "of Clubs"
            case Suit.HEARTS:
                return "of Hearts"
            case Suit.DIAMONDS:
                return "of Diamonds"
            case _:
                raise TypeError("Unexpected value {}".format(self))


class CardType(Enum):
    EVENT = 0
    SCHEME_SCRY = 1
    ADVERSITY = 2
    PLOTS_CURSES = 3
    COMPANION = 4
    INFLUENCE = 5
    CATASTROPHE = 6
    TRUTH = 7

    def __str__(self):
        match self:
            case CardType.EVENT:
                return "Event"
            case CardType.SCHEME_SCRY:
                return "Scheming or Scrying"
            case CardType.ADVERSITY:
                return "Adverse Event"
            case CardType.PLOTS_CURSES:
                return "Plot or Curse"
            case CardType.COMPANION:
                return "Companion"
            case CardType.INFLUENCE:
                return "Influence"
            case CardType.CATASTROPHE:
                return "Catastrophe"
            case CardType.TRUTH:
                return "Truth"
            case _:
                raise TypeError("Unexpected value {}".format(self))


class FaceValue(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

    @staticmethod
    def get_face_cardtype(fv):
        match fv:
            case FaceValue.ACE:
                return CardType.TRUTH
            case FaceValue.TWO:
                return CardType.EVENT
            case FaceValue.THREE:
                return CardType.EVENT
            case FaceValue.FOUR:
                return CardType.EVENT
            case FaceValue.FIVE:
                return CardType.EVENT
            case FaceValue.SIX:
                return CardType.SCHEME_SCRY
            case FaceValue.SEVEN:
                return CardType.ADVERSITY
            case FaceValue.EIGHT:
                return CardType.ADVERSITY
            case FaceValue.NINE:
                return CardType.ADVERSITY
            case FaceValue.TEN:
                return CardType.PLOTS_CURSES
            case FaceValue.JACK:
                return CardType.COMPANION
            case FaceValue.QUEEN:
                return CardType.INFLUENCE
            case FaceValue.KING:
                return CardType.CATASTROPHE
            case _:
                raise TypeError("Unexpected value {}".format(fv))

    def get_cardtype(self):
        return FaceValue.get_face_cardtype(self)

    def __str__(self):
        match self:
            case FaceValue.ACE:
                return "Ace"
            case FaceValue.TWO:
                return "Two"
            case FaceValue.THREE:
                return "Three"
            case FaceValue.FOUR:
                return "Four"
            case FaceValue.FIVE:
                return "Five"
            case FaceValue.SIX:
                return "Six"
            case FaceValue.SEVEN:
                return "Seven"
            case FaceValue.EIGHT:
                return "Eight"
            case FaceValue.NINE:
                return "Nine"
            case FaceValue.TEN:
                return "Ten"
            case FaceValue.JACK:
                return "Jack"
            case FaceValue.QUEEN:
                return "Queen"
            case FaceValue.KING:
                return "King"
            case _:
                raise TypeError("Unexpected value {}".format(self))


class RandomPrompt:
    def __init__(self, prompt: str, responses: list):
        self.prompt: str = prompt
        self.responses: list = responses


EMPTY_SLUG = {
    "boiler_plate": "",
    "fixed_prompts": [],
    "random_prompts": []
}


class Card:
    # Event Cards are just Cards
    # Scrying / Scheming Cards have player driven interaction, but it's handled in game right now
    # Plot cards are event cards with delayed text
    # Companion and Influence Cards have no actions of their own and just display text
    # Adversity Cards have Player driven actions
    # Catastrophe Cards have Player driven actions

    def __init__(self, suit: Suit, value: FaceValue, slug=EMPTY_SLUG):
        if list(EMPTY_SLUG.keys()) != list(slug.keys()):
            raise ValueError(
                "Missing required keys. Got {}, expected {}".format(list(slug.keys()), list(EMPTY_SLUG.keys())))
        self.suit: Suit = suit
        self.value: FaceValue = value
        self.theme: Theme = suit.get_theme()
        self.cardType: CardType = value.get_cardtype()
        # Always display boilerplate text
        self.boilerplate_text: str = slug["boiler_plate"]
        # Display each of the fixed writing prompts
        self.fixed_prompts: list = slug["fixed_prompts"]
        # Display one of each of the random prompt sets
        self.random_prompt_sets: list = slug["random_prompts"]

    def __str__(self):
        return "{} {}, {} {}".format(self.value, self.suit, self.theme, self.cardType)

    def copy(self):
        return deepcopy(self)

    def take_actions(self, player, deck):
        print(self.boilerplate_text)
        print()
        for fp in self.fixed_prompts:
            print(fp)
            print()
        for prompt in self.random_prompt_sets:
            print(prompt.prompt)
            print(random.choice(prompt.responses))
            print()

    def __eq__(self, card2):
        return (
                type(self) == type(card2)
                and self.suit == card2.suit
                and self.value == card2.value
        )


class TestCard(unittest.TestCase):
    def test_not_same_memory(self):
        card1 = Card(Suit.SPADES, FaceValue.ACE)
        card2 = Card(Suit.SPADES, FaceValue.ACE)
        self.assertTrue(card1 == card2)
        self.assertFalse(id(card1) == id(card2))

    def test_same_memory(self):
        card1 = Card(Suit.SPADES, FaceValue.ACE)
        self.assertTrue(card1 == card1)
        self.assertTrue(id(card1) == id(card1))

    def test_not_same(self):
        card1 = Card(Suit.SPADES, FaceValue.ACE)
        card2 = Card(Suit.CLUBS, FaceValue.ACE)
        self.assertFalse(card1 == card2)
        self.assertFalse(id(card1) == id(card2))

    def test_copy_is_deep(self):
        card1 = Card(Suit.SPADES, FaceValue.ACE)
        card2 = card1.copy()
        self.assertTrue(card1 == card2)
        card1.suit = Suit.HEARTS
        self.assertFalse(card1 == card2)


if __name__ == '__main__':
    unittest.main()
