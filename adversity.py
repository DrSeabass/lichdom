import random
from card import Card, Suit, FaceValue, CardType

class Adversity(Card):

    def __init__(self, suit: Suit, value: FaceValue, bptext="", fixed=[], random_sets=[]):
        super().__init__(suit, value, bptext, fixed, random_sets)

    def get_threshold(self):
        match self.value:
            case FaceValue.SEVEN:
                return 7
            case FaceValue.EIGHT:
                return 8
            case FaceValue.NINE:
                return 9
            case _:
                raise ValueError("Created adversity card with invalid face value {}.".format(self.value))

    def choose_influences(self, possible_influence):
        for index, card in enumerate(possible_influence):
            print("{}: {}".format(index, card))
        print("Select which influences to use, remembering this task is {}.".format(self.theme))
        print("Respond with comma separated numbers, as in 1, 2, 3")
        response = input()
        if response == "":
            return []
        try:
            to_use = []
            for index in map(lambda x: int(x), response.split(",")):
                to_use.append(possible_influence[index])
            return to_use
        except:
            self.choose_influences(possible_influence)

    def compute_modifiers(self, hand):
        modifiers = 0
        to_resolve = []
        possible_influence = []
        for card in hand:
            if card.theme == self.theme:
                if card.cardType == CardType.TRUTH:
                    print("Knowledge of a truth provides you an advantage in this trial.")
                    modifiers += 1
                elif card.cardType == CardType.COMPANION:
                    print("One of your companions aids you in this trial")
                    modifiers += 1
                elif card.cardType == CardType.ADVERSITY:
                    modifiers -= 2
                    to_resolve.append(card)
            elif card.cardType == CardType.INFLUENCE:
                possible_influence.append(card)
        return modifiers, to_resolve, possible_influence

    def use_influence(self, spent_influence):
        influence_modifier = 0
        for card in spent_influence:
            score = 0
            if card.theme == self.theme:
                score += random.randint(1,6)
                score += random.randint(1, 6)
            else:
                score += random.randint(1, 6)
            print("Your influence has eased your challenge {}.".format(score))
            influence_modifier += score
        return influence_modifier

    def check_target(self, target, modifiers):
        if (target - modifiers) <= 2:
            print("Your preparations allow you to overcome the challenge with ease.")
            return True
        else:
            roll = random.randint(1,6) + random.randint(1,6)
            if (roll + modifiers) >= target:
                print("You successfully navigate the difficulty.")
                return True
            else:
                print("You fail to navigate the difficulty ({} < {})".format(roll, target))
                return False

    def offer_retry(self, player):
        if player.resolve <= 1:
            return False
        else:
            print("1. Use your corrupting powers and try again.")
            print("2. Accept defeat and continue on.")
            response = input()
            try:
                selection = int(response)
                if selection == 1:
                    return True
                elif selection == 2:
                    return False
                else:
                    print("Got invalid user input: {}".format(response))
                    return self.offer_retry(player)
            except:
                print("Got invalid user input: {}".format(response))
                return self.offer_retry(player)

    def take_actions(self, player, deck):
        modifiers, to_resolve, possible_influence = self.compute_modifiers(player.hand)
        spent_influence = self.choose_influences(possible_influence)
        modifiers += self.use_influence(spent_influence)
        target = self.get_threshold()
        success = self.check_target(target, modifiers)
        if not success:
            retry = self.offer_retry(player)
            if not retry:
                player.decrease_resolve()
            else:
                player.increase_doom()
                self.take_actions(player, deck)
        for card in spent_influence:
            player.hand.remove(card)
        for card in to_resolve:
            player.hand.remove(card)
            card.take_actions()
        super().take_actions(player, deck)
