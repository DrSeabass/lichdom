from game.cards.card import Card, CardType, FaceValue, Suit

class Catastrophe(Card):
    def __init__(self, suit: Suit, value: FaceValue, slug={}):
        super().__init__(suit, value, slug)

    def get_companions(self, player):
        available_companions = []
        for card in player.hand:
            if card.cardType == CardType.COMPANION:
                available_companions.append(card)
        return available_companions

    def offer_sacrifice(self, options):
        for index, card in enumerate(options):
            print("{}: {}".format(index, card))
        print("Would you like to sacrifice a companion to avoid catastrophe?")
        print("Select a number to sacrifice, or press return to preserve your companions.")
        response = input()
        if response == "":
            return None
        else:
            try:
                index = int(response)
                return options[index]
            except:
                print("I didn't understand. Trying again...")
                return self.offer_sacrifice(options)

    def take_actions(self, player, deck):
        sacrifices = self.get_companions(player)
        if len(sacrifices) > 0:
            sacrifice = self.offer_sacrifice(sacrifices)
            if sacrifice is not None:
                player.hand.remove(sacrifice)
                print("You sacrificed a companion ({}) to avoid catastrophe!".format(sacrifice))
            else:
                player.increase_doom()
        else:
            player.increase_doom()
        super().take_actions(player, deck)