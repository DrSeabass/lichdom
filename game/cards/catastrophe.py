from enum import Enum

import game.player
from game.cards.card import Card, CardType, FaceValue, Suit
from game.action import select_from_prompts


class SacrificeType(Enum):
    NOONE = 0,
    SOMEONE = 1

    def __str__(self):
        match self:
            case SacrificeType.NOONE:
                return "Sacrifice no one"
            case SacrificeType.SOMEONE:
                return "Sacrifice"


class Sacrifice:
    def __init__(self, card=None):
        if card is not None:
            self.type = SacrificeType.SOMEONE
            self.card = card
        else:
            self.type = SacrificeType.NOONE
            self.card = None

    def __str__(self):
        disp_str = "{}".format(self.type)
        if self.card is not None:
            disp_str = "{} {}".format(disp_str, self.card)
        return disp_str


class Catastrophe(Card):
    def __init__(self, suit: Suit, value: FaceValue, slug={}):
        super().__init__(suit, value, slug)

    @staticmethod
    def get_sacrifices(player : game.player.Player):
        available_companions = [Sacrifice()]
        for card in player.hand:
            if card.cardType == CardType.COMPANION:
                available_companions.append(Sacrifice(card))
        return available_companions

    def take_actions(self, player: game.player.Player, deck: list):
        sacrifices = self.get_sacrifices(player)
        sacrifice = select_from_prompts(sacrifices)
        if sacrifice.type == SacrificeType.SOMEONE:
            print("You sacrificed a companion ({}) to avoid catastrophe!".format(sacrifice))
            player.hand.remove(sacrifice.card)
        else:
            player.decrease_resolve()
            player.increase_doom()
        deck.push(self)
        deck.shuffle()
        super().take_actions(player, deck)
