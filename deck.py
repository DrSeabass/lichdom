from card import Suit, FaceValue, Card

class Deck:
    cards = []

    def __init__(self):
        for suit in Suit:
            for value in FaceValue:
                self.cards.append(Card(suit, value))