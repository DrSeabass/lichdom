from card import FaceValue, RandomPrompt

card_slugs = {
    FaceValue.ACE: {
        "boiler_plate": """
A truth of this world that
gives you power over
death and places you
above all other mortals, giving
you a chance at immortality.
""",
        "fixed_prompts": [],
        "random_prompts": [
            RandomPrompt(
                "Where do you find it?",
                [
                    """
In the Book of Skelos,
crumbling scrolls long
buried in the shelves of
the forbidden library and
guarded by blind sages.
                    """,
                    """
Hieroglyphics on the broken
walls of a half buried city
under the desert sands.
                    """,
                    """
Experiments described in
the journal of a sorcerer with
a similar quest to yours,
now consumed by worms
in a cursed necropolis.
"""
                ]
            ),
            RandomPrompt(
                "What is it?",
                [
                    """
Death is only another
alchemical process that can
be stopped with the proper
research of the body and the
right potions
                    """,
                    """
A soul can be trapped in
this world by offering other
souls in return, preventing
it from abandoning its
mortal body when it stops
functioning.
                    """,
                    """
Resurrection is possible,
and it has been recorded in
the sacred texts of forgotten
religions. An undying
body might be achievable
by worshipping foul gods
that demand abhorrent
sacrifices.
                    """
                ]
            )
        ]
    },
    FaceValue.TWO: {
        "boiler_plate": """""",
        "fixed_prompts": [],
        "random_prompts": []
    },
    FaceValue.THREE: {
        "boiler_plate": """""",
        "fixed_prompts": [],
        "random_prompts": []
    },
    FaceValue.FOUR: {
        "boiler_plate": """""",
        "fixed_prompts": [],
        "random_prompts": []
    },
    FaceValue.FIVE: {
        "boiler_plate": """""",
        "fixed_prompts": [],
        "random_prompts": []
    },
    FaceValue.SIX: {
        "boiler_plate": """""",
        "fixed_prompts": [],
        "random_prompts": []
    },
    FaceValue.SEVEN: {
        "boiler_plate": """""",
        "fixed_prompts": [],
        "random_prompts": []
    },
    FaceValue.EIGHT: {
        "boiler_plate": """""",
        "fixed_prompts": [],
        "random_prompts": []
    },
    FaceValue.NINE: {
        "boiler_plate": """""",
        "fixed_prompts": [],
        "random_prompts": []
    },
    FaceValue.TEN: {
        "boiler_plate": """""",
        "fixed_prompts": [],
        "random_prompts": []
    },
    FaceValue.JACK: {
        "boiler_plate": """""",
        "fixed_prompts": [],
        "random_prompts": []
    },
    FaceValue.QUEEN: {
        "boiler_plate": """""",
        "fixed_prompts": [],
        "random_prompts": []
    },
    FaceValue.KING: {
        "boiler_plate": """""",
        "fixed_prompts": [],
        "random_prompts": []
    }
}