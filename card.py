# TODO: Lift Card Definitions Out Into Separate File(s)
from enum import Enum

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
    SCHEME_SCRY = 1 # TODO: Probably need to break this up
    ADVERSITY = 2
    PLOTS_CURSES = 3 # TODO: Probably need to break this up
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


class Card:
    suit: Suit
    theme: Theme
    cardType: CardType
    value: FaceValue

    def __init__(self, suit: Suit, value: FaceValue):
        self.suit = suit
        self.value = value
        self.theme = suit.get_theme()
        self.cardType = value.get_cardtype()

    def __str__(self):
        return "{} {}, {} {}".format(self.value, self.suit, self.theme, self.cardType)