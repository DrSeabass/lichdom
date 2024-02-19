from enum import Enum
import random
from game.cards.card import Card, Suit, FaceValue, CardType, Theme
from game.action import select_from_prompts, multiselect_from_prompts

class RetryActions(Enum):
    RETRY = 0
    ACCEPT = 1
    FAIL = 2
    SACRIFICE = 3

    def __str__(self):
        match self:
            case RetryActions.RETRY:
                return "Use your corrupting powers and try again."
            case RetryActions.ACCEPT:
                return "Accept defeat and continue on."
            case RetryActions.FAIL:
                return "Compelled Failure"
            case RetryActions.SACRIFICE:
                return "Sacrifice a companion to gain 1d6 bonus to your test."


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
        prompts = []
        for card in hand:
            if card.theme == self.theme:
                if card.cardType == CardType.TRUTH:
                    prompts.append("* Knowledge of a truth [[{}]] provides you an advantage in this trial.".format(card))
                    modifiers.append(1)
                elif card.cardType == CardType.COMPANION:
                    prompts.append("* One of your companions, [[{}]], aids you in this trial.".format(card))
                    modifiers.append(1)
                elif card.cardType == CardType.PLOTS_CURSES:
                    if card.theme == Theme.Mundane:
                        prompts.append("* An earlier plot [[{}]] influences the trial.".format(card))
                    else:
                        prompts.append("* An earlier curse [[{}]] influences the trial.".format(card))
                    modifiers.append(2)
                    to_resolve.append(card)
            if card.cardType == CardType.INFLUENCE:
                possible_influence.append(card)
        return modifiers, to_resolve, possible_influence, prompts

    def use_influence(self, spent_influence):
        influence_modifier = 0
        prompts = []
        for card in spent_influence:
            score = 0
            if card.theme == self.theme:
                score += random.randint(1, 6)
                score += random.randint(1, 6)
            else:
                score += random.randint(1, 6)
            prompts.append("* You used your influence, [[{}]] to ease your challenge by {}.".format(card, score))
            influence_modifier += score
        return influence_modifier, prompts

    @staticmethod
    def check_target(target: int, modifiers: list):
        disp_string = ""
        ret_val = False
        delta = target - sum(modifiers)
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
        return ret_val, delta

    def offer_retry(self, player, deficiency) -> object:
        if player.resolve <= 1 and player.doom >= 3:
            return RetryActions.FAIL # Can't succeed
        elif player.doom < 3 and player.resolve == 1:
            return  RetryActions.RETRY # Retry Compelled
        else:
            maximum_sacrifice = 0
            for card in player.hand:
                if card.cardType == CardType.COMPANION:
                    maximum_sacrifice += 6
            if maximum_sacrifice >= deficiency:
                return select_from_prompts([RetryActions.RETRY, RetryActions.ACCEPT, RetryActions.SACRIFICE])
            else:
                return select_from_prompts([RetryActions.RETRY, RetryActions.ACCEPT])

    def take_actions(self, player, deck, corruption_marks = []):
        modifiers, to_resolve, possible_influence, modifier_prompts = self.compute_modifiers(player.hand)
        spent_influence = multiselect_from_prompts(
            possible_influence,
            "Select which influences to use, remembering this task is {}.".format(self.theme))
        influence_modifiers, influence_prompts = self.use_influence(spent_influence)
        modifiers.append(influence_modifiers)
        target = self.get_threshold()
        success, deficiency = Adversity.check_target(target, modifiers)
        keep_trying = True
        display_dict = super().take_actions(player, deck)
        while not success and keep_trying:
            user_selection = self.offer_retry(player, deficiency)
            match user_selection:
                case RetryActions.ACCEPT:
                    player.decrease_resolve()
                    keep_trying = False
                case RetryActions.FAIL:
                    player.decrease_resolve()
                    keep_trying = False
                case RetryActions.RETRY:
                    print("Trying again...")
                    success, deficiency = Adversity.check_target(target, modifiers)
                    corruption = player.invoke_dark_power(self.theme)
                    player.increase_doom()
                    corruption_marks.append(corruption)
                case RetryActions.SACRIFICE:
                    possible_sacrifices = []
                    for card in player.hand:
                        if card.cardType == CardType.COMPANION:
                            possible_sacrifices.append(card)
                    sacrifices = multiselect_from_prompts(possible_sacrifices, "Select which companions to sacrifice.")
                    total_bonus = 0
                    for sacrifice in sacrifices:
                        player.hand.remove(sacrifice)
                        bonus = random.randint(1, 6)
                        modifiers.append(bonus)
                        display_dict["prompts"].append("* You sacrificed [[{}]] to gain a bonus of {} in a bid to overcome the trial.".format(sacrifice, bonus))
                        total_bonus += bonus
                    if total_bonus >= deficiency:
                        success = True
                case _:
                    raise ValueError("Should have hit one of the above cases")
        if success:
            player.increase_resolve()
        
        display_dict["prompts"].extend(modifier_prompts)
        display_dict["prompts"].extend(influence_prompts)
        confounds = []
        for card in to_resolve:
            player.hand.remove(card)
            confounds.append(card.take_actions(player, deck))
        for card in spent_influence:
            player.hand.remove(card)
        display_dict["confounds"].extend(confounds)
        if success:
            display_dict["prompts"].append("* You successfully navigated the adversity.")
        else:
            display_dict["prompts"].append("* You failed to navigate the adversity.")
        if len(corruption_marks) > 0:
            to_add = "* You used your dark powers to try to overcome this obstacle. This has affected you in the following ways:"
            for mark in corruption_marks:
                to_add = "{}\n\t* {}".format(to_add, mark)
            display_dict["prompts"].append(to_add)
        return display_dict
