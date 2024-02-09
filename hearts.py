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
        "boiler_plate": """
The greed of merchants
doesn’t know limits,
and this particular guild
pushed a little too far by making
demands of someone such as
yourself, who delves in magic
and secrets that would shatter
their minds.
But they do have something you
need, and you must fi nd a way
to snatch it from their greedy
hands before someone else takes
interest.""",
        "fixed_prompts": [
"""
What unreasonable price
did they ask for in their
hubris? 
""",
"""
Did you pay the price or
took what you needed by
force?
""",
"""
Can you trust their
discretion? Do you take
measures to silence them?
"""
        ],
        "random_prompts": [
            RandomPrompt("What do they offer?",[
"""
A map drawn on the
stretched skin of a long
Two of Hearts
extinct beast, leading to
the forsaken tomb of an
infamous sorcerer-king.
""",
"""
The journal of one of the
reclusive members of the
Black Circle, containing
unknown rituals and spells
to summon demons and rot
living fl esh.
""",
"""
The petrifi ed heart of a
giant fi re-breathing serpent,
a most precious alchemical
component in obscure
rituals of necromancy.
""" ])
        ]
    },
    FaceValue.THREE: {
        "boiler_plate":
"""
You receive a threat from
a known or unknown
enemy that achieves its
purpose: to hurt your pride and
disturb your ambitions.
You are enraged by such a
daring move against your person
and vow to destroy them. You are
still bound by mortal passions,
after all.
""",
        "fixed_prompts": [
"""
Who sends the threat and
why do you hate each other?
""",
"""
How do you respond in
your rage? Why can’t you
end their life at this point?
""",
"""
Why is it so important to
you to come on top of this
quarrel?
"""
"""Is your nemesis an
individual or a whole
organisation, such as The
Circle of Sequestered
Mystics, The People of the
Black Circle, or the Temple
of Undying Light?
"""
        ],
        "random_prompts": [
            RandomPrompt("What is the threat?",
                         [
"""
The head of a distant ally,
the pain of torture imprinted
in her rotting eyes.""",
"""A hateful letter written with
poisonous ink distilled from
the blood of an unknown
creature.""",
"""The burned pages of a
fabled book. Unreadable
knowledge made ashes,
its secrets lost to time after
being committed to memory
by your nemesis."""
                         ])
        ]
    },
    FaceValue.FOUR: {
        "boiler_plate": """
The cult of a new god
spreads across the land,
rapidly increasing in
power as the cult infects the
powerful and denounces old and
oppressive institutions.
You know they worship a false
god, or at best a minor entity of
the spheres, and yet you fi nd
some utility in their nonsense.
Impressionable individuals with
devotion to a higher purpose are
the easiest to manipulate.""",
        "fixed_prompts": [
"""
Who is the leader of this
new cult? Are you enemies?
Do you hold some respect
for each other?""",

"""What is the most abhorrent
practice of the cult?"""<

"""Who are the most vocal and
prominent enemies of the
cult? How do they die?"""
],
        "random_prompts": [
            RandomPrompt(
"What is this cult?",
[
    """The Cult of Wyrm rises
from the desert tribes; its
believers willing to sacrifice
themselves to the giant
snakes in their temples.""",
"""The Cult of the Silent One
spreads from the frozen
north; no sound is allowed
in their temples and they
trade secrets for death.""",
"""The Cult of Ardent Fire
develops from a sect; the
rage of their followers tears
down everything that was
holy and sacred to their
forefathers."""])]
    },
    FaceValue.FIVE: {
        "boiler_plate": """
An ancient noble house
seeks your aid in
desperation. Their gods
and medicine have failed them,
and they are now willing to make
a pact with darkness to survive.
Not all the arrogant rulers of the
masses are your allies, but this
opportunity is perfect to advance
your agenda or slight a common
enemy.""",
        "fixed_prompts": [
"""Who needs desperate help
and why do you provide it?""",
"""What do you claim in
return? Simple riches or
an unassuming family
heirloom that it’s older than
they can imagine?""",
"""How do you banish their
torment and who dies in the
process?""",
"""Who infl icts this bane
upon them? Are they your
enemy? If so, why do you
hate them?"""],

        "random_prompts": [
            RandomPrompt(
                "What affl icts the noble house?",
                [
"""A disease of the blood that
rots the body in life while
the mind is trapped forever.""",
"""A curse on the women of
the dynasty. New blood is
stillborn and enemies look
greedily upon their lands
while amassing their armies
at the border."""
"""The crops rot and the
livestock fall prey to savage
beasts summoned from
other realities."""])]
    },
    FaceValue.SIX: {
        "boiler_plate": """
Your constant scheming
against the bickering
noble houses, and
numerous spies infi ltrated in
their own households fi nally
provides results you can use.
You learn political secrets
well protected by steel and
incantations, and now you can
plan ahead to profi t from the
bleak future to come, and even
intrude to your advantage.""",
        "fixed_prompts": [
"""What do you learn that stirs
your anger? How do you
move against it?""",
""""What do you scheme to
profi t from what you have
learned?""",
"""Who dies as a result of your
spying and scheming? Was
it a planned move?""",
"""Who else is an accomplice of
your schemes? Do they owe
you a favour or are they
acting on self-interest?"""
        ],
        "random_prompts": [
            RandomPrompt(
"How do you learn it?",
[
    """Secrets murmured in the
court of a queen by careless
courtesans that drink too
much and boast too freely.""",
"""Sold by the Temple of Silent
Whispers in exchange for
a crippling secret about an
ally of yours.""",
"""Stolen contracts from the
guild of merchants in the
city of Noch, makers of the
famous iridescent steel"""]
            )
        ]
    },
    FaceValue.SEVEN: {
        "boiler_plate": """
Dream thieves, a rare
but mundane threat
perpetuated by unique
and extraordinary mortals,
infi ltrate into your dreams to
steal a precious memory. They
face the terrible shadows of your
mind and horrors lurking in your
unconscious thoughts.""",
        "fixed_prompts": [
"Who sent them against you?",
"What are they trying to steal?"
        ],
        "random_prompts": [
            RandomPrompt("Who is the dream thief?",
                [
"Theleb-Karn, a famous sage in search of the true name of a higher demon.",
"Oone, a lonely adventurer in search of a secret city.",
"Someone without a name, shedding all memories aside to become no-one."
                ]
            ),
            RandomPrompt("What challenges do you present?",
[
    """Immovable doors opened by impossible riddles. The memory is carved in stone and written in an ancient language lost to time.""",
"""An eternal desert inhabited
by sand demons. The
memory is narrated by a
hermit in an oasis with
carnivorous vegetation.
"""
"""A city of crystal and
dangerous creatures frozen
in time until approached by
an intruder. The memory
can be seen in a bottomless
pool at the centre of the city"""]
            )
        ]
    },
    FaceValue.EIGHT: {
        "boiler_plate": """
After many weeks of
careful planning, bribes,
lies, threats and possibly
murder, you become the leader
of a cult. Your followers do your
bidding with limited effi cacy,
but their unquestionable loyalty
makes up for their lack of wits.""",
        "fixed_prompts": [
"Who had to die for you to become the leader?",
"Why do they worship you?",
"What is the most outrageous lie your cultists believe?"],
        "random_prompts": [
            RandomPrompt("What is the axiom of the cult?",
[
"""Mortality is a gift from
the gods and lives are
expendable.""",
"""Mortals are only cattle to
demons and other immortal
entities in an eternal struggle
for supremacy in the higher
spheres.""",
"""The all-knowing leader
will save the cult from the
upcoming cataclysm."""
]),
            RandomPrompt("How do you end up in charge?",
[
"""You create the cult from
nothing, using illusions and
rhetoric to attract the weak.""",
"""You manoeuvre into a
position of power within
an established cult before
murdering the leader.""",
"""The cult forms around you
almost by chance. Your
fame and power spread,
attracting new followers
that think you are a god."""]
            )
        ]
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