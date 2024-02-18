from enum import Enum
import random
from game.cards.card import Card, Suit, FaceValue, CardType
from game.action import select_from_prompts, multiselect_from_prompts

class RetryActions(Enum):
    RETRY = 0
    ACCEPT = 1
    FAIL = 2

    def __str__(self):
        match self:
            case RetryActions.RETRY:
                return "Use your corrupting powers and try again."
            case RetryActions.ACCEPT:
                return "Accept defeat and continue on."
            case RetryActions.FAIL:
                return "Compelled Failure"


class Adversity(Card):

    def __init__(self, suit: Suit, value: FaceValue, slug={}):
        super().__init__(suit, value, slug)

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

    def compute_modifiers(self, hand):
        modifiers = []
        to_resolve = []
        possible_influence = []
        for card in hand:
            if card.theme == self.theme:
                if card.cardType == CardType.TRUTH:
                    print("Knowledge of a truth provides you an advantage in this trial.")
                    modifiers.append(1)
                elif card.cardType == CardType.COMPANION:
                    print("One of your companions aids you in this trial")
                    modifiers.append(1)
                elif card.cardType == CardType.PLOTS_CURSES:
                    print("An earlier plot or curse influences the trial")
                    modifiers.append(2)
                    to_resolve.append(card)
            if card.cardType == CardType.INFLUENCE:
                possible_influence.append(card)
        return modifiers, to_resolve, possible_influence

    def use_influence(self, spent_influence):
        influence_modifier = 0
        for card in spent_influence:
            score = 0
            if card.theme == self.theme:
                score += random.randint(1, 6)
                score += random.randint(1, 6)
            else:
                score += random.randint(1, 6)
            print("Your influence has eased your challenge {}.".format(score))
            influence_modifier += score
        return influence_modifier

    @staticmethod
    def check_target(target: int, modifiers: list):
        disp_string = ""
        ret_val = False
        if (target - sum(modifiers)) <= 2:
            disp_string = "Your preparations allow you to overcome the challenge with ease."
            ret_val = True
        else:
            # TODO: Capture rolls, individual modifiers to show to player
            rolls = []
            rolls.append(random.randint(1,6))
            rolls.append(random.randint(1, 6))
            if (sum(rolls) + sum(modifiers)) >= target:
                disp_string = "You successfully navigate the difficulty. {} <".format(target)
                for value in rolls + modifiers:
                    disp_string = "{} {} +".format(disp_string, value)
                disp_string = disp_string[:-1]
                ret_val = True
            else:
                disp_string = "You fail to navigate the difficulty. {} >=".format(target)
                for value in rolls + modifiers:
                    disp_string = "{} {} +".format(disp_string, value)
                disp_string = disp_string[:-1]
                ret_val = False
        print(disp_string)
        return ret_val

    def offer_retry(self, player) -> object:
        if player.resolve <= 1 and player.doom >= 3:
            return RetryActions.FAIL # Can't succeed
        elif player.doom < 3 and player.resolve == 1:
            return  RetryActions.RETRY # Retry Compelled
        else:
            return select_from_prompts([RetryActions.RETRY, RetryActions.ACCEPT])

    def take_actions(self, player, deck, retry=False):
        modifiers, to_resolve, possible_influence = self.compute_modifiers(player.hand)
        spent_influence = multiselect_from_prompts(
            possible_influence,
            "Select which influences to use, remembering this task is {}.".format(self.theme))
        modifiers.append(self.use_influence(spent_influence))
        target = self.get_threshold()
        success = Adversity.check_target(target, modifiers)
        if not success:
            user_selection = self.offer_retry(player)
            print("User selected {}".format(user_selection))
            match user_selection:
                case RetryActions.ACCEPT:
                    player.decrease_resolve()
                case RetryActions.FAIL:
                    player.decrease_resolve()
                case RetryActions.RETRY:
                    print("Trying again...")
                    player.increase_doom()
                    self.take_actions(player, deck, retry=True)
                case _:
                    raise ValueError("Should have hit one of the above cases")
        else:
            player.increase_resolve()
        display_dict = super().take_actions(player, deck)
        for card in spent_influence:
            player.hand.remove(card)
            display_dict["prompts"].append("* You used {} to influence the outcome of the trial.".format(card))
        confounds = []
        for card in to_resolve:
            player.hand.remove(card)
            confounds.append(card.take_actions(player, deck))
        display_dict["confounds"].extend(confounds)
        if success:
            display_dict["prompts"].append("* You successfully navigated the adversity.")
        else:
            display_dict["prompts"].append("* You failed to navigate the adversity.")
        return display_dict
