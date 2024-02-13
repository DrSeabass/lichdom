from enum import Enum
import random
from game.cards.card import Card, CardType, FaceValue, Suit
from game.action import select_from_prompts


class PaymentType(Enum):
    RESOLVE = 0
    DOOM = 1
    CARD = 2
    ABANDON = 3

    def __str__(self):
        match self:
            case PaymentType.RESOLVE:
                return "Lose 1 Resolve"
            case PaymentType.DOOM:
                return "Gain 1 Doom"
            case PaymentType.CARD:
                return "Sacrifice a Card"
            case PaymentType.ABANDON:
                return "Abandon attempt and pay no cost"


class Payment:
    def __init__(self, type, card=None):
        self.type: PaymentType = type
        self.card = card

    def __str__(self):
        output = "{}".format(self.type)
        if self.card:
            output = "{}: {}".format(output, self.card)
        return output


class SchemeScry(Card):
    def __init__(self, suit: Suit, value: FaceValue, slug={}):
        super().__init__(suit, value, slug)

    def prompt_user_scheme_scry(self, uncertain, certain):
        print("Replace one of these cards:")
        for index, card in enumerate(certain):
            print("{}: {}".format(index, card))
        print("With one of these cards:")
        for index, card in enumerate(uncertain):
            print("{}: {}".format(index, card))
        user_input = input("Your Selections (in the format number, number)")
        try:
            selections = user_input.split(',')
            removed_index = int(selections[0])
            replaced_index = int(selections[1])
            if 0 < removed_index >= len(certain):
                print("Certain card to remove index is illegal, try again")
                return self.prompt_user_scheme_scry(uncertain, certain)
            if 0 < replaced_index >= len(uncertain):
                print("Uncertain card to select index is illegal, try again")
                return self.prompt_user_scheme_scry(uncertain, certain)
            swap = certain[removed_index]
            certain[removed_index] = uncertain[replaced_index]
            uncertain[replaced_index] = swap
            return uncertain, certain
        except:
            print("Couldn't understand your selections.  Please try again.")
            return self.prompt_user_scheme_scry(uncertain, certain)

    def scheme_scry(self, deck):
        rolls = [random.randint(1, 6), random.randint(1, 6)]
        rolls.sort()
        certain_count = rolls[0]
        uncertain_count = rolls[1]
        certain_future = deck.draw_many(certain_count)
        uncertain_future = deck.draw_many(uncertain_count)
        uncertain_future, certain_future = self.prompt_user_scheme_scry(uncertain_future, certain_future)
        deck.push_many(uncertain_future)
        deck.shuffle()
        random.shuffle(certain_future)
        deck.push_many(certain_future)

    def find_possible_payment(self, player):
        options = [Payment(PaymentType.ABANDON)]
        if player.resolve > 1:
            options.append(Payment(PaymentType.RESOLVE))
        if player.doom < 3:
            options.append(Payment(PaymentType.DOOM))
        for card in player.hand:
            if card.cardType == CardType.INFLUENCE or card.cardType == CardType.SCHEME_SCRY:
                if card is not self:
                    options.append(Payment(PaymentType.CARD, card))
        return options

    def take_actions(self, player, deck):
        options = self.find_possible_payment(player)
        payment = select_from_prompts(options)
        match payment.type:
            case PaymentType.DOOM:
                player.increase_doom()
            case PaymentType.RESOLVE:
                player.decrease_resolve()
            case PaymentType.CARD:
                player.hand.remove(payment.card)
            case PaymentType.ABANDON:
                return
        player.hand.remove(self)
        self.scheme_scry(deck)
        super().take_actions(player, deck)
