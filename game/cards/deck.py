from game.cards.card import Suit, FaceValue, Card, CardType
from game.cards.catastrophe import Catastrophe
from game.cards.adversity import Adversity
from game.cards.scheme_scry import SchemeScry
import game.cards.hearts as hearts
import game.cards.diamonds as diamonds
import game.cards.clubs as clubs
import game.cards.spades as spades
from copy import deepcopy
import random

SLUGS = {
    Suit.Hearts : hearts.card_slugs,
    Suit.Diamonds : diamonds.card_slugs,
    Suit.Clubs : clubs.card_slugs,
    Suit.Spades : spades.card_slugs
}

class Deck:

    def __init__(self, populate=True):
        self.cards = []
        if populate:
            for suit in Suit:
                for value in FaceValue:
                    card_type = FaceValue.get_face_card_type(value)
                    slug = SLUGS[suit][value]
                    match card_type:
                        case CardType.CATASTROPHE:
                            self.cards.append(Catastrophe(suit, value, slug))
                        case CardType.ADVERSITY:
                            self.cards.append(Adversity(suit, value, slug))
                        case CardType.SCHEME_SCRY:
                            self.cards.append(SchemeScry(suit, value, slug))
                        case _:
                            self.cards.append(Card(suit, value, slug))

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

    def dehydrate(self):
        return [card.dehydrate() for card in self.cards]


    @staticmethod
    def hydrate(data):
        deck = Deck(populate=False)
        deck.cards = [Card.hydrate(card_data) for card_data in data]
        return deck

