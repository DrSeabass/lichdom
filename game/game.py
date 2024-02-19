from enum import Enum
import random
import pickle
import os.path

from game.cards.card import Card, Theme, CardType
from game.cards.deck import Deck
from game.player import Player
from game.action import UserPrompt, UserPromptBase, select_from_prompts, file_path_prompt


# TODO: Hang game end string off of a terminal node for the state machine, consolidating where output happens
class TerminalCondition(Enum):
    CATACLYSM = 0
    LOST_RESOLVE = 1
    FAILED_LICHDOM = 2
    LICHDOM = 3
    GODHOOD = 4
    NOT_TERMINAL = 5


class DrawStepResultBase(Enum):
    MAGICAL_CATACLYSM = 0
    CARD = 1



class DrawStepResult:

    def __init__(self, base, card):
        self.base: DrawStepResultBase = base
        self.card: Card = card

    def ends_game(self):
        if self.base == DrawStepResultBase.MAGICAL_CATACLYSM:
            return True
        else:
            return False

    def __str__(self) -> str:
        return "{}: {}".format(self.base, self.card)


class Game:

    @staticmethod
    def get_save_location_from_journal_dir(dirname):
        return os.path.join(dirname, "game_state.sav")

    def __init__(self, journal_directory=None):
        self.player: Player = Player()
        self.deck: Deck = Deck()
        self.previous_card: Card = None
        self.previous_state = None
        self.terminal = TerminalCondition.NOT_TERMINAL
        self.deck.shuffle()
        self.journal_directory = journal_directory
        if journal_directory is None:
            self.archival = False
            self.save_path = None
        else:
            self.archival = True
            self.one_time_setup()
            
        self.game_step = 1
        self.journal_entry = 1
        if self.save_path is not None and os.path.exists:
            self.load()
        else:
            self.save()

    def one_time_setup(self):
        self.save_path = Game.get_save_location_from_journal_dir(self.journal_directory)
        # Ensure the directory structure
        # -game_root
        # -- game_state.sav
        # -- journal
        # --- entry_1.md
        # --- entry_2.md
        # --- ...
        # -- resources
        # -- rules
        # -- random tables & entities
        # -- spades
        # --- Ace of Spades.md
        # --- 2 of Spades.md
        # --- ...
        # -- hearts
        # -- clubs
        # -- diamonds
        if not os.path.exists(self.journal_directory): #If it does exist, assume we're loading a game.
            os.makedirs(self.journal_directory)
            os.makedirs(os.path.join(self.journal_directory, "journal"))
            # TODO: Do this later if it looks like you want the raw material dumped every time.  Text is cheap.
            #os.makedirs(os.path.join(self.journal_directory, "resources"))
            #os.makedirs(os.path.join(self.journal_directory, "resources", "rules"))
            #os.makedirs(os.path.join(self.journal_directory, "resources", "random tables & entities"))
            #os.makedirs(os.path.join(self.journal_directory, "resources", "spades"))
            #os.makedirs(os.path.join(self.journal_directory, "resources", "hearts"))
            #os.makedirs(os.path.join(self.journal_directory, "resources", "clubs"))
            #os.makedirs(os.path.join(self.journal_directory, "resources", "diamonds"))
        else: #Directory existed.
            self.display("Looks like you're resuming a game.  Trying to load from {}".format(self.save_path))
            self.load()

    def get_step_actions(self):
        # if the player has 2 truths, they may attempt to ascend to lichdom, prompt them
        # if the player has a scrying / scheming card, they may scry, prompt them
        # otherwise, force the draw step

        truth_count = 0
        prompts = [UserPrompt(UserPromptBase.DRAW) ]
        if len(self.player.hand) > 0:
            prompts.append(UserPrompt(UserPromptBase.DISPLAY_PLAYER_HAND))
        for card in self.player.hand:
            if card.cardType == CardType.TRUTH:
                truth_count += 1
            elif card.cardType == CardType.SCHEME_SCRY:
                prompts.append(UserPrompt(UserPromptBase.SCHEME_SCRY, card))
        if truth_count >= 2:
            prompts.append(UserPrompt(UserPromptBase.ATTEMPT_LICHDOM))

        prompts.append(UserPrompt(UserPromptBase.SAVE))
        if self.previous_state is not None:
            prompts.append(UserPrompt(UserPromptBase.LOAD))
        return prompts

    def prompt_user(self, prompt_actions):
        self.display("Turn {}: {}".format(self.game_step, self.player.player_state_str()))
        return select_from_prompts(prompt_actions)

    def draw(self):
        if len(self.deck) == 0:
            raise ValueError("You can't deck yourself in this game; should always have 4 catastrophe cards")
        next_card = self.deck.draw()
        if (
                self.previous_card is not None
                and self.previous_card.theme == Theme.Arcane
                and next_card.theme == Theme.Arcane
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
        self.display("Rolled for truths: {}".format(rolls))
        score += sum(rolls)
        self.display("Final Score: {}".format(score))
        # TODO: There have to be better places to keep these strings
        if score <= 4:
            self.display(
                """You die horribly, your flesh boils and your bones crumble to dust,
cursing the land where you attempted the foul ritual.""", record=True)
            self.terminal = TerminalCondition.FAILED_LICHDOM
        elif 4 < score <= 8:
            self.display(
                """You become a wraith, a half ethereal horror beyond the comprehension of other mortals.
You will inevitably lose your mind and sanity in the many years ahead haunting your lair, becoming only a monster with
no other ambitions besides consuming human souls. A beast far removed from your goal of power.""", record=True)
            self.terminal = TerminalCondition.FAILED_LICHDOM
        elif 8 < score <= 11:
            self.display(
                """Your foul ritual partially succeeds, giving you immense power and an extremely long life.
You will live 12 13 hundreds of years, command armies and establish cults that will outlive you…
but you are not immortal. Your body will eventually wither and die, everything you built will crumble to dust,
and your name will be forgotten. You are only mortal after all.""", record=True)
            self.terminal = TerminalCondition.FAILED_LICHDOM
        elif 11 < score < 19:
            self.display(
                """You made it. Your immortal soul will linger in this world forever, just enough time to discover
all the secrets of the cosmos. Your body may decay with time, but you will find younger vessels as the ages pass by.
You are a lich.""", record=True)
            self.terminal = TerminalCondition.LICHDOM
        else:
            self.display(
                """Time doesn’t have meaning any more. Ages come and go, empires rise and fall, and you stand above
them all while learning the most corrupting secrets of the void beyond reality. You have become a god""", record=True)
            self.terminal = TerminalCondition.GODHOOD

    def process_card(self, card):
        self.display("Drew to: {}".format(card))
        if not (
                card.cardType == CardType.ADVERSITY or
                card.cardType == CardType.EVENT or
                card.cardType == CardType.CATASTROPHE
        ):
            self.player.hand.append(card)
        if not (  # if not card with delayed processing
                card.cardType == CardType.SCHEME_SCRY or
                card.cardType == CardType.PLOTS_CURSES
        ):
            display_dict = card.take_actions(self.player, self.deck)
            display_string = "{}\n\n# Prompt\n\n{}".format(display_dict["title"], display_dict["boiler_plate"])
            for prompt in display_dict["prompts"]:
                display_string = "{}\n{}".format(display_string, prompt)
            if len(display_dict["confounds"]) > 0:
                display_string = "{}\n# Confounds\n\n".format(display_string)
            for confound in display_dict["confounds"]:
                display_string = "{}\n## {}\n\n{}\n\n### Prompts\n\n".format(display_string, confound["title"], confound["boiler_plate"] )
                for prompt in confound["prompts"]:
                    display_string = "{}\n{}".format(display_string, prompt)
            display_string = "{}\n# Journal Entry".format(display_string)
            self.display(display_string, self.archival)
        if self.player.resolve <= 0:
            self.terminal = TerminalCondition.LOST_RESOLVE

    def step(self):
        possible_actions = self.get_step_actions()
        selected_action = self.prompt_user(possible_actions)
        match selected_action.base_prompt:
            case UserPromptBase.DRAW:
                self.game_step += 1
                drawn_card = self.draw()
                if drawn_card.base == DrawStepResultBase.CARD:
                    self.process_card(drawn_card.card)
                else:  # Magical Cataclysm
                    self.terminal = TerminalCondition.CATACLYSM
            case UserPromptBase.DISPLAY_PLAYER_HAND:
                self.display(self.player.player_hand_str())
            case UserPromptBase.SCHEME_SCRY:
                hand_size_before = len(self.player.hand)
                selected_action.card.take_actions(self.player, self.deck)
                hand_size_after = len(self.player.hand)
                if hand_size_before != hand_size_after: # If the player used the scry card and didn't abort.
                    self.game_step += 1
            case UserPromptBase.ATTEMPT_LICHDOM:
                self.game_step += 1
                self.attempt_lichdom()
            case UserPromptBase.SAVE:
                self.save()
            case UserPromptBase.LOAD:
                self.load()

    def save(self):
        self.previous_state = self.dehydrate()
        if self.save_path is not None:
            self.display("Saving to {}".format(self.save_path))
            open_flags = "wb"
            if not os.path.exists(self.save_path):
                open_flags = "xb"
            with open(self.save_path, open_flags) as save_file:
                pickle.dump(self.previous_state, save_file)
        else:
            self.display("No save path set, only saved in memory, not to disk.")

    def load(self):
        if self.previous_state is None:
            if os.path.exists(self.save_path):
                self.previous_state = pickle.load(open(self.save_path, "rb"))
            else:
                return # No previous state to load
        saved_game = Game.hydrate(self.previous_state)
        if os.path.exists(self.save_path):
            with open(self.save_path, "rb") as save_file:
                previous_state = pickle.load(save_file)
                saved_game = Game.hydrate(previous_state)
                self.__dict__ = saved_game.__dict__
                self.previous_state = previous_state

    def play(self):
        while self.terminal == TerminalCondition.NOT_TERMINAL:
            self.step()
        match self.terminal:
            case TerminalCondition.CATACLYSM:
                self.display("In your bid to become a lich, you have meddled with powers you did not understand and could not control.  Not only will you not live forever, no one will live. Forever.", record=True)
            case TerminalCondition.LOST_RESOLVE:
                self.display("You lose the will to carry on.  You will never become a lich.  You will never become a god.  You will never be remembered.  You will never be anything.", record=True)
            case TerminalCondition.FAILED_LICHDOM:
                self.display("You fail in your bid to become a lich.", record=True)
            case TerminalCondition.LICHDOM:
                self.display("You succeeded in your bid to become a lich!", record=True)
            case TerminalCondition.GODHOOD:
                self.display("You enjoy success beyond what you could have ever imagined.  You are not merely some undead, undying vessel.  You are a god.", record=True)

    def dehydrate(self):
        return {
            "player": self.player.dehydrate(),
            "deck": self.deck.dehydrate(),
            "previous_card": self.previous_card.dehydrate() if self.previous_card else None,
            "terminal": self.terminal.name,
            "game_step": self.game_step
        }

    @staticmethod
    def hydrate(data):
        game = Game()
        game.player = Player.hydrate(data["player"])
        game.deck = Deck.hydrate(data["deck"])
        game.previous_card = Card.hydrate(data["previous_card"]) if data["previous_card"] else None
        game.terminal = TerminalCondition[data["terminal"]]
        game.game_step = data["game_step"]
        return game

    def display(self,text, record=False):
        print(text)
        if record and self.archival:
            path = os.path.join(self.journal_directory, "journal", "entry_{}.md".format(self.journal_entry))
            self.journal_entry += 1
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w") as journal_entry:
                journal_entry.write(text)