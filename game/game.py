from enum import Enum
import random

from game.cards.card import Card, Theme, CardType
from game.cards.deck import Deck
from game.player import Player


class UserPromptBase(Enum):
    DRAW = 0
    DISPLAY_PLAYER_HAND = 1
    ATTEMPT_LICHDOM = 2
    SCHEME_SCRY = 3


class UserPrompt:

    def __init__(self, base, card=None):
        self.base_prompt = base
        if card is not None:
            self.card = card

    def __str__(self):
        match self.base_prompt:
            case UserPromptBase.DRAW:
                return "Draw a Card"
            case UserPromptBase.DISPLAY_PLAYER_HAND:
                return "Show Player Hand"
            case UserPromptBase.ATTEMPT_LICHDOM:
                return "Attempt the Lichdom Ritual"
            case UserPromptBase.SCHEME_SCRY:
                return str(self.card)


class DrawStepResultBase(Enum):
    MAGICAL_CATACLYSM = 0
    CARD = 1


class DrawStepResult:

    def __init__(self, base, card):
        self.base : DrawStepResultBase = base
        self.card : Card = card

    def ends_game(self):
        if self.base == DrawStepResultBase.MAGICAL_CATACLYSM:
            return True
        else:
            return False


class Game:

    def __init__(self):
        self.player: Player = Player()
        self.deck: Deck = Deck()
        self.previous_card: Card = None
        self.continue_game: bool = True

    def get_step_actions(self):
        # if the player has 2 truths, they may attempt to ascend to lichdom, prompt them
        # if the player has a scrying / scheming card, they may scry, prompt them
        # otherwise, force the draw step

        truth_count = 0
        prompts = [
            UserPrompt(UserPromptBase.DRAW),
            UserPrompt(UserPromptBase.DISPLAY_PLAYER_HAND)
        ]
        for card in self.player.hand:
            if card.cardType == CardType.TRUTH:
                truth_count += 1
            elif card.cardType == CardType.SCHEME_SCRY:
                prompts.append(UserPrompt(UserPromptBase.SCHEME_SCRY, card))
        if truth_count >= 2:
            prompts.append(UserPrompt(UserPromptBase.ATTEMPT_LICHDOM))

        return prompts

    def prompt_user(self, prompt_actions):
        print(self.player.player_state_str())
        for index, action in enumerate(prompt_actions):
            print("{}: {}".format(index, action))
        user_input = input("Choose an action (by inputting the number): ")
        try:
            selected_index = int(user_input)
            if 0 <= selected_index < len(prompt_actions):
                return selected_index
        except ValueError:
            print("{} was a bad selection.".format(user_input))
            return self.prompt_user(prompt_actions)

    def draw(self):
        if len(self.deck) == 0:
            raise ValueError("You can't deck yourself in this game; should always have 4 catastrophe cards")
        next_card = self.deck.draw()
        print("Drew to {}".format(next_card))
        if (
                self.previous_card is not None
                and self.previous_card.theme == Theme.ARCANE
                and next_card.theme == Theme.ARCANE
                and next_card.cardType == CardType.CATASTROPHE
                and self.previous_card.cardType == CardType.CATASTROPHE
        ):
            return DrawStepResult(DrawStepResultBase.MAGICAL_CATACLYSM, next_card)
        return DrawStepResult(DrawStepResultBase.CARD, next_card)

    def attempt_lichdom(self):
        truths = 0
        companions = 0
        influence = 0
        for card in self.player.hand:
            match card.cardType:
                case CardType.TRUTH:
                    truths += 1
                case CardType.COMPANION:
                    companions += 1
                case CardType.INFLUENCE:
                    influence += 1
        score = companions + influence + self.player.resolve
        rolls = []
        for _ in range(truths):
            roll = random.randint(1, 6)
            rolls.append(roll)
        print("Rolled for truths: {}".format(rolls))
        score += sum(rolls)
        print("Final Score: {}".format(score))
        # TODO: There have to be better places to keep these strings
        if score <= 4:
            print(
                "You die horribly, your flesh boils and your bones crumble to dust, cursing the land where you attempted the foul ritual.")
        elif 4 < score <= 8:
            print(
                "You become a wraith, a half ethereal horror beyond the comprehension of other mortals. You will inevitably lose your mind and sanity in the many years ahead haunting your lair, becoming only a monster with no other ambitions besides consuming human souls. A beast far removed from your goal of power.")
        elif 8 < score <= 11:
            print(
                "Your foul ritual partially succeeds, giving you immense power and an extremely long life. You will live 12 13 hundreds of years, command armies and establish cults that will outlive you… but you are not immortal. Your body will eventually wither and die, everything you built will crumble to dust, and your name will be forgotten. You are only mortal after all.")
        elif 11 < score < 19:
            print(
                "You made it. Your immortal soul will linger in this world forever, just enough time to discover all the secrets of the cosmos. Your body may decay with time, but you will find younger vessels as the ages pass by. You are a lich.")
        else:
            print(
                "Time doesn’t have meaning any more. Ages come and go, empires rise and fall, and you stand above them all while learning the most corrupting secrets of the void beyond reality. You have become a god")

    def process_card(self, card):
        if not (
            card.cardType == CardType.ADVERSITY or
            card.cardType == CardType.EVENT or
            card.cardType == CardType.CATASTROPHE
        ):
            self.player.hand.append(card)
        if not ( # if not card with delayed processing
            card.cardType == CardType.SCHEME_SCRY or
            card.cardType == CardType.PLOTS_CURSES
        ):
            card.take_actions(self.player, self.deck)
        self.continue_game = self.player.resolve > 0

    def step(self):
        possible_actions = self.get_step_actions()
        selected_action_index = self.prompt_user(possible_actions)
        selected_action = possible_actions[selected_action_index]
        match selected_action.base_prompt:
            case UserPromptBase.DRAW:
                drawn_card = self.draw()
                if drawn_card.base == DrawStepResultBase.CARD:
                    self.process_card(drawn_card.card)
                else:  # Magical Cataclysm
                    #TODO Handle end of world via cataclysm
                    print("PLACE HOLDER END OF WORLD TEXT")
                    self.continue_game = False
            case UserPromptBase.DISPLAY_PLAYER_HAND:
                print(self.player.player_hand_str())
            case UserPromptBase.SCHEME_SCRY:
                selected_action.card.take_actions(self.player, self.deck)
            case UserPromptBase.ATTEMPT_LICHDOM:
                self.attempt_lichdom()
                self.continue_game = False


    def play(self):
        while self.continue_game:
            self.step()
