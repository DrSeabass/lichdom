from enum import Enum
import os.path

class UserPromptBase(Enum):
    DRAW = 0
    DISPLAY_PLAYER_HAND = 1
    ATTEMPT_LICHDOM = 2
    SCHEME_SCRY = 3
    SAVE = 4
    LOAD = 5

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
            case UserPromptBase.SAVE:
                return "Save game state"
            case UserPromptBase.LOAD:
                return "Load game state"


def select_from_prompts(prompt_actions: list):
    if len(prompt_actions) == 1:
        return prompt_actions[0] # Return the compelled action
    elif len(prompt_actions) == 0:
        raise ValueError("Can't select an action from the empty list.")
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


def multiselect_from_prompts(prompt_actions: list, prompt_str):
    if len(prompt_actions) == 0:
        return [] # Return compelled selection
    for index, action in enumerate(prompt_actions):
        print("{}: {}".format(index, action))
    print(prompt_str)
    print("Respond with comma separated numbers, such as 1,3,5")
    response = input()
    if response == "":
        return []
    try:
        to_use = []
        indexes = set(map(lambda x: int(x), response.split(",")))
        for index in indexes:
            to_use.append(prompt_actions[index])
        return to_use
    except:
        return multiselect_from_prompts(prompt_actions, prompt_str)


def select_one_from_two(first_set, second_set, first_string, second_string):
    print(first_string)
    for index, card in enumerate(first_set):
        print("{}: {}".format(index, card))
    print(second_string)
    for index, card in enumerate(second_set):
        print("{}: {}".format(index, card))
    user_input = input("Your Selections (in the format number, number)")
    try:
        selections = user_input.split(',')
        removed_index = int(selections[0])
        replaced_index = int(selections[1])
        if 0 < removed_index >= len(first_set):
            print("First selected index is illegal, try again")
            return select_one_from_two(second_set, first_set, first_string, second_string)
        if 0 < replaced_index >= len(second_set):
            print("Second selected index is illegal, try again")
            return select_one_from_two(second_set, first_set, first_string, second_string)
        return removed_index, replaced_index
    except:
        print("Couldn't understand your selections.  Please try again.")
        return select_one_from_two(second_set, first_set, first_string, second_string)

def file_path_prompt():
    print("Please enter the file path for the save file, empty string to abort")
    possible = input()
    if possible == "":
        return None
    try:
        possible_dir = os.path.dirname(possible)
        os.path.create_dir(possible_dir, exist_ok=True)
        if os.path.exists(possible):
            print("The file already exists, and will be overwritten on save unless you enter a new name.")
        return possible
    except:
        print("Couldn't create the directory for the file, try again")
        return file_path_prompt()

def directory_path_prompt():
    print("Please enter the directory to store the journal or the empty string to not set a directory")
    possible = input()
    if possible == "":
        return None
    dirname, ext = os.path.splitext(possible)
    if ext != "":
        print("That's not a directory, try again")
        return directory_path_prompt()
    if os.path.dirname(dirname):
        try:
            os.path.create_dir(dirname, exist_ok=True)
            return dirname
        except:
            print("Couldn't create the directory, try again")
            return directory_path_prompt()
    else:
        print("That's not a directory, try again")
        return directory_path_prompt()