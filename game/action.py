from enum import Enum


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

def select_from_prompts(prompt_actions: list):
    for index, action in enumerate(prompt_actions):
        print("{}: {}".format(index, action))
    user_input = input("Choose an action (by inputting the number): ")
    try:
        selected_index = int(user_input)
        if 0 <= selected_index < len(prompt_actions):
            return prompt_actions[selected_index]
        else:
            print("{} was a bad selection.".format(user_input))
            return select_from_prompts(prompt_actions)
    except ValueError:
        print("{} was a bad selection.".format(user_input))
        return select_from_prompts(prompt_actions)
