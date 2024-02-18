import random
from copy import deepcopy
from enum import Enum


class Theme(Enum):
    Mundane = 0
    Arcane = 1

    def __str__(self):
        return self.name


class Suit(Enum):
    Spades = 0
    Clubs = 1
    Hearts = 2
    Diamonds = 3

    @staticmethod
    def get_suit_theme(suit):
        match suit:
            case Suit.Spades:
                return Theme.Arcane
            case Suit.Clubs:
                return Theme.Arcane
            case Suit.Hearts:
                return Theme.Mundane
            case Suit.Diamonds:
                return Theme.Mundane
            case _:
                raise TypeError("Unexpected value {}".format(suit))

    def get_theme(self):
        return Suit.get_suit_theme(self)

    def __str__(self):
        return self.name


class CardType(Enum):
    EVENT = 0
    SCHEME_SCRY = 1
    ADVERSITY = 2
    PLOTS_CURSES = 3
    COMPANION = 4
    INFLUENCE = 5
    CATASTROPHE = 6
    TRUTH = 7

    def __str__(self):
        match self:
            case CardType.EVENT:
                return "Event"
            case CardType.SCHEME_SCRY:
                return "Scheming or Scrying"
            case CardType.ADVERSITY:
                return "Adverse Event"
            case CardType.PLOTS_CURSES:
                return "Plot or Curse"
            case CardType.COMPANION:
                return "Companion"
            case CardType.INFLUENCE:
                return "Influence"
            case CardType.CATASTROPHE:
                return "Catastrophe"
            case CardType.TRUTH:
                return "Truth"
            case _:
                raise TypeError("Unexpected value {}".format(self))
            
card_type_descriptions = {
    CardType.EVENT: """Events in the life of your sorcerer for which you do not need to roll a challenge, you can simply make up what you wish to resolve the
event as it fits your story, then discard the card. Narrative Events should be used as an opportunity for developing the world around your character; 
perhaps describing an encounter with an almost extinct but ancient sentient race, your dealings with the guild of imperial librarians, or a great victory
against the secretive cult of the Serpent God. 
""",
    CardType.SCHEME_SCRY: """Special opportunities for your sorcerer to change future events through Mundane Scheming of Arcane Scrying. Keep the card to
use whenever you wish, but only after completing an event and before drawing the next card. If the deck doesn’t contain enough cards to draw, you lose
the game. You can explain it as a mishap of your Scheming or Scrying, such as failing to control other conspirators or trapping your mind inside
a crystal ball.""",
    CardType.ADVERSITY: """Significant challenges in the life of your sorcerer, such as navigating a complicated political landscape or surviving a 
duel against another sorcerer. Remember that you can use Corrupting Powers to repeat the roll of an Adversity challenge with the same bonuses and penalties
as the first roll, but this increases your Doom by 1 hence reducing your maximum Resolve for the rest of the game.""",
    CardType.PLOTS_CURSES: """Mundane Plots and Arcane Curses work against you, such as a conspiracy to end your life, or enemy petitions to responsive gods
to halt your progress and thwart your ambitions. Keep the card visible on the table. The next time you have to roll a challenge of the same nature (Mundane or Arcane),
apply a penalty of -2 and discard the card. The penalties of several Plot/Curse cards are cumulative over the next challenge""",
    CardType.COMPANION: """Mundane and Arcane allies in your story, such as the spirit of the fi rst wizard to walk this world, or an assassin that seeks favour with
an elder god. Keep the card with you while your companion is alive, providing a +1 bonus to challenges of the same nature (Mundane or Arcane). You can also sacrifice a
Companion for one of the following effects, then discard the card.""",
    CardType.INFLUENCE: """Influence over the Mundane or the Arcane that provides a critical - but fleeting - help in the form of things such as favours owed by
powerful mortals or forgotten rituals of power that can only be uttered once.""",
    CardType.CATASTROPHE: """The impending Doom in your story. It can represent many different things, such as personal failure, unavoidable traps by bitter enemies,
or general strife in the world. When you draw a Catastrophe you immediately gain 1 Doom and reduce 1 Resolve unless you sacrifice a Companion, which suffers the horrible
consequences of the Catastrophe instead. Shuffle the Catastrophe card back into the deck after resolving its effects. If you draw two Arcane Calamities in consecutive turns,
you bring the end of times to your world and lose the game."""
}


class FaceValue(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

    @staticmethod
    def get_face_card_type(fv):
        match fv:
            case FaceValue.ACE:
                return CardType.TRUTH
            case FaceValue.TWO:
                return CardType.EVENT
            case FaceValue.THREE:
                return CardType.EVENT
            case FaceValue.FOUR:
                return CardType.EVENT
            case FaceValue.FIVE:
                return CardType.EVENT
            case FaceValue.SIX:
                return CardType.SCHEME_SCRY
            case FaceValue.SEVEN:
                return CardType.ADVERSITY
            case FaceValue.EIGHT:
                return CardType.ADVERSITY
            case FaceValue.NINE:
                return CardType.ADVERSITY
            case FaceValue.TEN:
                return CardType.PLOTS_CURSES
            case FaceValue.JACK:
                return CardType.COMPANION
            case FaceValue.QUEEN:
                return CardType.INFLUENCE
            case FaceValue.KING:
                return CardType.CATASTROPHE
            case _:
                raise TypeError("Unexpected value {}".format(fv))

    def get_cardtype(self):
        return FaceValue.get_face_card_type(self)

    def __str__(self):
        match self:
            case FaceValue.ACE:
                return "Ace"
            case FaceValue.TWO:
                return "Two"
            case FaceValue.THREE:
                return "Three"
            case FaceValue.FOUR:
                return "Four"
            case FaceValue.FIVE:
                return "Five"
            case FaceValue.SIX:
                return "Six"
            case FaceValue.SEVEN:
                return "Seven"
            case FaceValue.EIGHT:
                return "Eight"
            case FaceValue.NINE:
                return "Nine"
            case FaceValue.TEN:
                return "Ten"
            case FaceValue.JACK:
                return "Jack"
            case FaceValue.QUEEN:
                return "Queen"
            case FaceValue.KING:
                return "King"
            case _:
                raise TypeError("Unexpected value {}".format(self))


class RandomPrompt:
    def __init__(self, prompt: str, responses: list):
        self.prompt: str = prompt
        self.responses: list = responses


EMPTY_SLUG = {
    "boiler_plate": "",
    "fixed_prompts": [],
    "random_prompts": []
}


class Card:
    # Event Cards are just Cards
    # Scrying / Scheming Cards have player driven interaction, but it's handled in game right now
    # Plot cards are event cards with delayed text
    # Companion and Influence Cards have no actions of their own and just display text
    # Adversity Cards have Player driven actions
    # Catastrophe Cards have Player driven actions

    def __init__(self, suit: Suit, value: FaceValue, slug=EMPTY_SLUG):
        if list(EMPTY_SLUG.keys()) != list(slug.keys()):
            raise ValueError(
                "Missing required keys. Got {}, expected {}".format(list(slug.keys()), list(EMPTY_SLUG.keys())))
        self.suit: Suit = suit
        self.value: FaceValue = value
        self.theme: Theme = suit.get_theme()
        self.cardType: CardType = value.get_cardtype()
        # Always display boilerplate text
        self.boilerplate_text: str = slug["boiler_plate"]
        # Display each of the fixed writing prompts
        self.fixed_prompts: list = slug["fixed_prompts"]
        # Display one of each of the random prompt sets
        self.random_prompt_sets: list = slug["random_prompts"]

    def __str__(self):
        match self.cardType:
            case CardType.SCHEME_SCRY:
                noun = "Scheme" if self.theme == Theme.Mundane else "Scrying"
                return "{} of {}, {} {}".format(self.value, self.suit, self.theme, noun)
            case CardType.PLOTS_CURSES:
                noun = "Plot" if self.theme == Theme.Mundane else "Curse"
                return "{} of {}, {} {}".format(self.value, self.suit, self.theme, noun)
            case _:
                return "{} of {}, {} {}".format(self.value, self.suit, self.theme, self.cardType)

    def copy(self):
        return deepcopy(self)

    def take_actions(self, player, deck):
        display_dict = {
            "title": "",
            "boiler_plate": "",
            "prompts": [],
            "confounds": []
        }
        display_dict["title"] = "[[{}]]".format(str(self))
        display_dict["boiler_plate"] = self.boilerplate_text.replace("\n", " ")
        for fp in self.fixed_prompts:
            display_dict["prompts"].append("* {}".format(fp).replace("\n", " "))
        for prompt in self.random_prompt_sets:
            if prompt.prompt == "":
                to_add = "* {}".format(random.choice(prompt.responses).replace("\n", " "))
            else:
                to_add = "* {}\n\t* {}".format(prompt.prompt, random.choice(prompt.responses).replace("\n", " "))
            display_dict["prompts"].append(to_add)
        return display_dict

    def __eq__(self, card2):
        return (
                self.cardType == card2.cardType
                and self.suit == card2.suit
                and self.value == card2.value
        )

    def dehydrate(self):
        return {
            "suit": self.suit.name,
            "value": self.value.name
        }

    @staticmethod
    def hydrate(data):
        return Card(Suit[data["suit"]], FaceValue[data["value"]])

    def obsidian_string(self):
        fixed_prompt_strings = ""
        random_prompt_strings = ""
        for prompt in self.fixed_prompts:
            fixed_prompt_strings = "{}\n* {}".format(fixed_prompt_strings, prompt.replace("\n", " "))
        for random_prompt in self.random_prompt_sets:
            random_response_prefix = ""
            if random_prompt.prompt == "":
                random_response_prefix = "\n* "
            else:
                random_response_prefix = "\n\t* "
            this_prompt = "* {}".format(random_prompt.prompt.replace("\n", " "))
            for response in random_prompt.responses:
                this_prompt = "{}{}{}".format(this_prompt, random_response_prefix, response.replace("\n", " "))
            random_prompt_strings = "{}\n{}".format(random_prompt_strings, this_prompt)
        return """{}

# Setup
{}

# Fixed Writing Prompts
{}

# Random Writing Prompts
{}
""".format(self, self.boilerplate_text, fixed_prompt_strings, random_prompt_strings)
