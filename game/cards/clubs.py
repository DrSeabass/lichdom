from game.cards.card import FaceValue, RandomPrompt

card_slugs = {
    FaceValue.ACE: {
        "boiler_plate":
            """A truth of all realities that gives you power over death and places you above all other mortals, giving
you a chance at immortality.""",
        "fixed_prompts": [

        ],
        "random_prompts": [
            RandomPrompt("Where do you learn it?",
[
    """The dreams of a slumbering serpent-god within the tomb of a sorcerer-king of aeons past.""",
    """Hidden in the future verses of a poem written by civilisations not yet born; a truth that only
foul sorcery can reveal.""",
    """A secret of the priests of an ancient religion to a god now dead; a truth only accessible through
atavistic scrying requiring great sacrifice."""]),
RandomPrompt("What is it?",
[
    """Split your soul into pieces and trap them within several artefacts that must be protected with traps,
incantations and demons bound to your immortal will.""",
    """The unused wish that was conceded by the first god to the fi rst sorcerer when time was young.""",
    """Bind your consciousness to a swarm of lesser beings. Each body is mortal, but the swarm will prevail through
the ages guided by your indomitable will."""])
        ]
    },
    FaceValue.TWO: {
        "boiler_plate": """Your search of forgotten lore in ancient ruins and dusty tomes takes you to communicating
with elder gods, long forgotten by other mortals. You hear their calling in the heavy darkness on the darkest nights,
cold whispers in an unknown language older than time itself, uttering unfathomable truths and making terrible demands
from their mortal worshippers.
        """,
        "fixed_prompts": [
            "How did you contact them and what was the cost?",
            "What answers do you seek and why can’t you find them without their help?",
            "What do they want from you in return that they can’t take by themselves?",
            "Do you keep worshipping them after your encounter and do you try to spread its cult to other mortals?"],
        "random_prompts": [
            RandomPrompt("Who speaks to you?",
[
    """Arioch, lord of the seven nights, who demands souls in exchange for his treacherous favour.""",
    """Azathoth, the sleeping god beyond the veil, whose dreams manifest as horrifying reality.""",
    """Jhebbal-Sag, a blood-thirsty entity worshipped by uncivilised savages beyond the red river.
Father of all earthly demons"""
        ])]
    },
    FaceValue.THREE: {
        "boiler_plate": """You discover the remains of an ancient civilisation; impossibly old and
incredibly beautiful. They were masters of such wonders that it makes you question the worth of your own achievements.
Silence besets the abandoned place; no doubt these fallen jade statues and sundered colourful temples were
once witness to wondrous and horrifying events now lost to recorded history. Perhaps their fall is for the best.""",
        "fixed_prompts": [
            "What destroyed them and how long ago was it?",
            "What remains of them now among the broken pieces of their ancient glory?",
            "How did you discover the ruins and what were you looking for?",
            "Where are the ruins and what problem did you have on the journey?"
        ],
        "random_prompts": [
            RandomPrompt("Who were they?",
                         [
                             """A race that came to your world in the time before the Cataclysm to
flee their demonic masters.""",
                             """A cruel culture that built Cyclopean monuments to their defunct emperors and
practised necromancy.""",
                             """A complex civilisation that transcended their own organic bodies,
animating complex machines with their spirits."""])
        ]
    },
    FaceValue.FOUR: {
        "boiler_plate": """You are trapped and lost for many days in a forsaken and dangerous dungeon below
the ruins of an ancient city. You came looking for an artefact older than the Cataclysm, but you only found corruption
and death instead. The darkness itself seems to whisper warnings, and furtive red eyes observe all your movements with
malevolent intent. You are not welcome here.""",
        "fixed_prompts": [
            "Where are you lost?",
            "What ancient artefact or forsaken knowledge do you seek in this place?",
            "Who died so you could survive and escape this baleful dungeon?"
        ],
        "random_prompts": [
            RandomPrompt("What threatens you?",
[
    """Black statues come to life in the sunken ruins of the Marsh of Decay; animated by the souls of cursed priests
of a forgotten religion.""",
    """An aggressive race of albino ape-men, worshippers of forgotten dark gods, that eat all trespassers while
keeping them alive with unnatural drugs.""",
"""Undead and grotesque aberrations guarding the basalt tomb of the Lord of Worms, a famous sorcerer that delved into
necromancy and made gruesome pacts with unholy demons."""])
        ]
    },
    FaceValue.FIVE: {
        "boiler_plate":
            """Your thirst for arcane knowledge leads you to stealing a cursed tome of lore from an obscure cult,
the secret meaning of ancient runes, or the ancient wisdom of a disappearing culture. You had to lie, kill and threaten
to get it, perhaps even destroying the original owners or condemning them to a fate worse than death.""",
        "fixed_prompts": [
            "What did you steal and why is it important to you?",
            "How did you learn of its existence and what did it cost you?",
            "Did you gain the knowledge you were looking for?",
            "Who were its previous guardians and how did you steal from them?",
            "What’s the final destiny of those you have wronged with this plot?"
        ],
        "random_prompts": [
            RandomPrompt("What esoteric knowledge did you steal?",
[
    "The first words spoken by the Raven to the last woman in the first day after the Cataclysm.",
    "The detailed description of a ritual lost to time, which you are now unwilling to enact due to its dire cost.",
    "The true name of a demon, which grants absolute power over the corrupted will of the beast"])
        ]
    },
    FaceValue.SIX: {
        "boiler_plate": """By extensive and careful research in ancient tomes of sorcery, reading the shapes revealed
in the smoke of a sacrifice, making abhorrent deals in the dark with powerful demons, or by any other
unfathomable arcane means, you are able to discern your destiny from the entanglement of multiple realities
other mortals call “future”. You now have knowledge that makes allies seek your favour and enemies despair in fear of
your vengeance. Use it well.""",
        "fixed_prompts": [
            "What did you see in your future that disturbed you?",
            "How did you change the future to your advantage?",
            "What did this scrying ritual cost you and why cannot be repeated in the same way?",
            "What were you looking for in the future?"
        ],
        "random_prompts": [
            RandomPrompt("How do you read the future?",
[
    "You discern events yet to come from the prophetic verses written in the dried skin of a serpent-god.",
    "The entrails of human sacrifice speak of the secrets of powerful mortals and reveal horrors to come.",
    "Half-truths whispered from the darkness by a menacing demon that speaks in riddles and demands payment."])
        ]
    },
    FaceValue.SEVEN: {
        "boiler_plate": """An arcane trap written in the crumbling pages, fading glyphs, or rotten scrolls you study.
Words that imprison the mind of the reader in a nightmare lasting weeks, months, years or centuries.""",
        "fixed_prompts": [
            "What were you hoping to learn in your studies?"
            "How did you free yourself and how long were you imprisoned?"
        ],
        "random_prompts": [
            RandomPrompt("What were you researching?",
[
    """The book of Vathanos, which contains the transcripts of hundreds of years of conversations between the priests
of a dead religion and a demon.""",
    "The glyphs in the tomb of Thoth-Amon, a powerful sorcerer that was the favourite of the serpent demon-god Set.",
    "Half-burnt scrolls hidden for centuries in the ruins of a forsaken temple."]),
    RandomPrompt("Where was your mind imprisoned?",
[
    "Absolute darkness in complete silence. A timeless void beyond the seas of swirling chaos.",
    "A vortex of fire where other souls were trapped forever, too weak now to escape.",
    "Within the mind of a demon, bound by his willpower"])]
    },
    FaceValue.EIGHT: {
        "boiler_plate": """While learning a new spell or ritual, either a mistake or a purposefully placed error in
your source of sorcerous knowledge, causes an unexpected and dangerous magical mishap that you only
barely manage to control.""",
        "fixed_prompts": [
            "How do you control the mishap and what does it cost you?",
            "Who is to blame for this failure?"
        ],
        "random_prompts": [
            RandomPrompt("What sorcerous mishap occurs?",
[
    "A tear in reality opens a portal to an unstable plane where unformed demons abound.",
    "The dead rise for miles around you, animated by a sliver of consciousness of a vengeful god.",
    """A vortex of chaos and insanity grows and expands in the room, like a festering wound with the will
to consume the world."""]
),
            RandomPrompt("What sorcery were you performing?",
[
    "A simple ritual to speak with the dead.",
    "A spell learned from the notes of an ascetic monk you found petrified.",
    "A complex ritual to access the spirit world and search for someone."])
        ]
    },
    FaceValue.NINE: {
        "boiler_plate": """Your research of forgotten arts takes you to create an alchemical concoction that
attracts death. Yourself or someone close to you is gravely injured. The foul smell of the potion was a clear warning
of danger, but no reward comes without risk and you had to try its effects.""",
        "fixed_prompts": [
            "What was the most difficult ingredient to obtain and why?",
            "Is this the fi rst time you try? Why did you fail in the past?"
        ],
        "random_prompts": [
            RandomPrompt("What were the expected effects?",
[
    "Opening your mind to the secrets whispered by the darkness and the elements.",
    "Channelling your powers in the chaotic planes.",
    "Rising the dead from their rotting sleep."
    ]),
            RandomPrompt("But instead...",
[
    "The potion transforms the subject into an aggressive monstrosity with only a faint resemblance of a human mind.",
    "The subject grows an insatiable hunger for human fl esh that goes beyond any other desire.",
    "The subject phases out of existence for hours, returning with a broken mind and speaking in babbles"])
        ]
    },
    FaceValue.TEN: {
        "boiler_plate":
            """A baleful curse that diminishes your powers and disrupts your plans. Your enemy is probably familiar with
wizardry or a devout follower of a powerful god.""",
        "fixed_prompts": [
            "Why were you cursed?",
            "Are they a new enemy or an old one?",
            "How do you overcome it?"
        ],
        "random_prompts": [
            RandomPrompt("Who cursed you?",
[
    "The hierophant of the cult of Yig, father of all serpents and whisperer of unfathomable secrets, seeking revenge.",
    "A lonely witch driven by hate and greed. What did you do to her to ignite such loathing?",
    """Your old master, who you believed to be dead; its body petrified and sunken under the waters of the boiling sea.
How are you responsible for such a horrible destiny?"""]),
            RandomPrompt("What’s the effect of the curse?.",
[
    """Snakes detest you and actively seek to harm you. They come at you from the shadows of your own house,
making any rest difficult.""",
    "You are speechless for days, preventing you from chanting your terrible incantations.",
    "Food rots in your hands and water turns to ash in your mouth."]
)
        ]
    },
    FaceValue.JACK: {
        "boiler_plate": """You encounter a curious companion that follows you on your ambitious quest. Their skills
will be useful in the arcane world of perilous research and dark rituals you need to navigate before transcending
to lichdom. But do not get too attached, they are dispensable, after all.""",
        "fixed_prompts": [
            "What is their name?",
            "What do they look like?",
            "How do you meet?",
            "Why do they ally with you?"        ],
        "random_prompts": [
            RandomPrompt("Who is this curious character?",
[
    """An alchemist that achieved the transformation of lead into gold once in the past, but the secret was stolen from
his mind by a dream thief.""",
    "A self exiled dream thief condemned to death in many civilised lands for crimes against the mind.",
    "The trapped consciousness of a demon, its soul prisoner within your skull."]),
            RandomPrompt("What is special about them?",
[
    "Owes you their life or existence and is now bound to serve you.",
    "Was driven mad by a previous experience.",
    "Needs you and your power to destroy a common enemy that threatens both their body and mind."])
        ]
    },
    FaceValue.QUEEN: {
        "boiler_plate": """Help from arcane powers is not readily available to most mortals, but you have
the opportunity to buy their assistance or command them to give you aid by heinous sorcery, secret knowledge, or
other means. After all, you are a true master of the arcane among mortals.""",
        "fixed_prompts": [
            "How do you encounter them? Do they come to you or do you seek them out?",
            "Why do they help you and what does it cost you?",
            "Why can you only request their aid once?"
        ],
        "random_prompts": [
            RandomPrompt("Which master of the arcane helps you?",
[
    """The spirit of Skelos, or an incorporeal simulacrum of his consciousness, emerges from fading scripture
to give advice speaking in riddles. Only you can see him.""",
    """A witch, daughter of a prince of hell, tells you about the secrets whispered to her by demons and
malevolent spirits of the dark forest in which she lives.""",
    """A wandering seer offers cryptic visions of the future at the cost of some of your happiest memories, which
you will forget forever. Which memory do you give up and how does it change you for the worst?"""])
        ]
    },
    FaceValue.KING: {
        "boiler_plate":
            "A terrible unnatural event shakes the world or baleful arcane powers are directed towards you.",
        "fixed_prompts": [
            "Did you cause this catastrophe?",
            "How did you escape and what did it cost you?",
            "How did you change after this event?",
        ],
        "random_prompts": [
            RandomPrompt("",
[
    """You read a description of reality that shatters your understanding of it and drives you mad.
Where do you read it?""",
    """A ritual of light and darkness summons a fl esh-consuming mist that spreads through the world.
How do you avoid it?""",
    """A powerful demon has noticed you and detests your arrogance. Submit to its will to survive.
Why has it noticed you now? How do you release yourself?""",
    """A sorcerer queen of old awakens from her tomb. A cult quickly forms around her and takes arms to conquer all.
Why does she hate you?""",
    """You have an encounter with an enemy sorcerer in a position of power, barely surviving the duel.
What gives them power?""",
    """A failed spell sends you to an empty world beyond the shimmering chaos. How do you return?"""])
        ]
    }
}