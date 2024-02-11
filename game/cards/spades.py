from game.cards.card import FaceValue, RandomPrompt

card_slugs = {
    FaceValue.ACE: {
        "boiler_plate":
            """A truth of all realities that gives you power over death and places you above all other mortals,
giving you a chance at immortality.
            """,
        "fixed_prompts": [
        ],
        "random_prompts": [
            RandomPrompt(
                "Where do you find it?",
                [
                    """A dream quest. A ritual that allows your soul to travel to other planes and learn from
the experience of many lives across disparate existences.""",
                    """In the future constellation of stars, as revealed by an artefact of an extinct race found within
a tomb of unfathomable age.""",
                    """Signed a contract with a demon in exchange for abhorrent ritual sacrifices for
the years to come."""]),
            RandomPrompt("What is it?",
[
    """Only death can give you immortality. Follow a terrible ritual of powerful sorcery in the name of
forsaken gods to trap your soul in your body for all eternity.""",
    """Copy your consciousness into several gems, perfectly synchronized by your governing soul, which is merged into
the brains of an indestructible machine.""",
    """Learn the true name of a powerful demon and force it to maintain your soul in the mortal plane or
reveal the ritual of lichdom"""])
        ]
    },
    FaceValue.TWO: {
        "boiler_plate": """You sign a contract with a demon in exchange for wondrous knowledge and dark favours.
The demon refuses to reveal the higher secrets of reality, but is willing to whisper minor truths that could make you
a wolf among sheep. Do not mistake the mild interest of your demonic patron for admiration or recognition, as all
mortals are nothing but fleeting candles of consciousness in the eternal darkness of creation.""",
        "fixed_prompts": [
            "How did you contact the foul demon and what was the terrible cost?",
            "Why is the demon interested in making a deal with a mortal such as yourself?",
            "What do you want to know and why is this information difficult to obtain?",
            "What horrendous shape does the demon take?"
        ],
        "random_prompts": [
            RandomPrompt("What does the demon ask in return for its treacherous favour and unholy patronage?",
[
    "The first born of a new family, willingly offered by the mother.",
    "Nine souls consumed by an otherworldly fi re under a full moon.",
    "Murderous blood spilled between brothers in a holy day; stirred by rage and awakened by envy"])
        ]
    },
    FaceValue.THREE: {
        "boiler_plate": """You discover an ancient and isolated race hidden in plain sight or in a remote corner of
the world beyond a natural barrier. They worship strange gods in their grim temples and use old sorcery to stay hidden.
They may have originated in another plane or evolved in the very same world now dominated by your species; perhaps they
never conquered the surface or their race devolved into a shadow of their previously advanced civilization.
Irrespective of their origin and history, they feel alien and somewhat repulsive to you,
but you can benefit from them.""",
        "fixed_prompts": [
            "How did you discover the hidden race?",
            "Do you expose them or keep the information to yourself?",
            "How do you benefit from their existence?"
        ],
        "random_prompts": [
            RandomPrompt(
                "Who are they?",
             [
                 "Serpent-people living in expansive tunnel systems under inaccessible deserts and remote mountains.",
                 "An underwater species that breeds with humans in isolated communities.",
                 """A devoted human culture worshipping an artificial consciousness trapped in
a strange machine within an ancient tomb of metal."""])
        ]
    },
    FaceValue.FOUR: {
        "boiler_plate": """You dream of a glimmering city that exists in many realities. Somehow you know it’s not just
a dream, but a real place of which you can only find obscure references in fading and crumbling scrolls that do not
make much sense to your limited mortal mind. Perhaps if you find a way to access the marvellous city of wonders,
many of your questions about the nature of the cosmos and the many entities that populate it would be answered.""",
        "fixed_prompts": [
            "Why do you obsess over the wondrous city and what do you imagine you could find within its walls?",
            "Why can’t you find the entrance in your reality and what have you tried in your fruitless search?",
            "How does the city look and why do you suspect it may only be a feverish dream?"
        ],
        "random_prompts": [
            RandomPrompt(
                "What’s the immortal city?",
                [
                    """A fortress at the centre of all realities, constructed by an alien civilisation that once
dominated all planes.""",
                    "The last refuge of an ancient race that transcended death and holds many secrets.",
                    """A reflection of the meeting place of the lords of the Higher Worlds, which are worshipped as
gods in different forms through different realities"""])
        ]
    },
    FaceValue.FIVE: {
        "boiler_plate": """You sacrifice a mortal soul to feed the ego of a powerful demon or dark god, trying to gain
their capricious favour or avoid their menacing wrath. Either to clean an offense or to seek favour from
the dark entity, such terrible acts of ritual murder do not go unnoticed by other mortals around you. For better or
worse, your notoriety increases among mortals and immortal entities.""",
        "fixed_prompts": [
            "Who do you sacrifice and why have they been chosen?",
            "Who is the dark entity and why do you seek to appease it or attract its favour?",
            "Who notices your advances in the dark arts?"
        ],
        "random_prompts": [
            RandomPrompt(
                "What happens during the ritual?",
                [
                    """Two serpents come out of the mouth of the sacrifice. One of them consumes the other before
becoming ash. Not a good omen.""",
                    """Fire doesn’t kill the sacrifice, but it consumes their flesh with savage viciousness until there
is nothing left but blackened bones. A good omen.""",
                    """The day turns night and the moon turns red. The corpse of the sacrifice speaks in
an unknown language before turning to dust. What does it say to you?"""])
        ]
    },
    FaceValue.SIX: {
        "boiler_plate": """You have the opportunity to look into the many futures that diverge from your present by
tracing powerful runes in the ashes of an ancient forest, uttering forgotten words in the lost speech of an alien race,
focusing your mind on a powerful artefact that touches many realities, or by any other means lost to the sages since a
bygone age of wonders.""",
        "fixed_prompts": [
            "Where did you learn to scry the future?",
            "What did you see in your future that disturbed you?",
            "What did this scrying ritual cost you and why cannot be repeated in the same way?"
        ],
        "random_prompts": [
            RandomPrompt(
                "How do you read the future?",
                [
                    """Arcane visions granted by the mummified eye of the fi rst serpent, which upon consumption
submerges the sorcerer into a drugged stupor lasting weeks and revealing future truths and hidden realities.""",
                    """A conscious obsidian ball that can scry into many realities and only responds to
its original owner, a sorcerer of Acheron long dead, but you can trick it once to serve you instead.""",
                    """An abhorrent offering to an elder god reveals truths to come in the agony of
the screaming sacrifice."""])
        ]
    },
    FaceValue.SEVEN: {
        "boiler_plate": """Your craving for power takes you to an ageless tomb or crumbling temple long lost beyond
a natural barrier, now avoided by all civilised cultures due to ancient legends or real dangers.""",
        "fixed_prompts": [
            "Where are the ruins located and why are they difficult to reach?",
            "Who dies in the journey?"
        ],
        "random_prompts": [
            RandomPrompt("What are you looking for?",
[
    """The ruins of fabled Acheron and its ancient knowledge, an empire of demonic sorcerers that disappeared
a millennia ago.""",
    """The heart of a terrible beast, a crucial ingredient in the crafting of a key alchemical concoction in your search
for immortality.""",
    """The tomb of the first wizard to walk your world, as the legend says that consuming its mellified body
can extend life."""]),
            RandomPrompt("What horrors do you find?",
[
    "Savage tribes of pale men live underground and hunt all that moves above.",
    "An unwelcoming hive mind that emerges from millions of semi-intelligent arachnids living in the ruins.""",
    "A creature living among statues, with snakes for hair and a petrifying glance."])
        ]
    },
    FaceValue.EIGHT: {
        "boiler_plate": """Either on your own initiative or because you are attacked, you are involved in
a deadly sorcerous duel with another mage.""",
        "fixed_prompts": [
            "Who is the other sorcerer?",
            "How did you meet?",
            "Why did you become enemies?"
        ],
        "random_prompts": [
            RandomPrompt(
                "Who do you fight?",
[
    "An envoy of the Circle of Sequestered Mystics, sent to destroy you before you destroy them.",
    """A long-dead sorcerer king that rises from eternal sleep. Only a faint sliver of consciousness remains in
    the mummified body; enough to prove a challenge.""",
    """An old fellow mage, even friend, and chief advisor to the queen. He is convinced you are a threat to the kingdom
and the queen."""]
            ),
            RandomPrompt(
                "Where do you fi ght?",
                [
                    """In the steps of the Library of Tanelorn, where the history of ages past is recorded in
languages lost to time by inhuman hands.""",
                    "In their tower of arcane contemplation, riddled with magical traps and mutated monstrosities.",
                    """In the tomb of Nechrubel, who prophesied the end of this reality hundreds of years ago."""])
        ]
    },
    FaceValue.NINE: {
        "boiler_plate": """You find an entrance to the plane of existence containing the unused material of
unborn creations. Your mind shapes everything around you so your consciousness can endure the journey. Many souls have
come to fail here, their ambition quenched by the sight of their dreams and passions. Their minds now trapped forever
in a nightmare of melancholy; grim spirits in the void beyond reality.""",
        "fixed_prompts": [
            "What did you learn?",
            "What did it cost you?"
        ],
        "random_prompts": [
            RandomPrompt("How did you enter?",
[
    "A potent drug and a deep sleep releases the mind from earthly shackles.",
    "Through a gap in our reality at the end of the world.",
    "Through an ephemeral portal opened by a grim ritual learned from the infamous Book of Skelos."]),
            RandomPrompt("What challenges you?",
[
    "The hateful spirit of an old enemy finds you. It seeks your eternal doom.",
    "The entrance into this chaotic world closes and you must find another exit.",
    "A demon made of shadow challenges you to solve his riddle before releasing you from his grasp."])
        ]
    },
    FaceValue.TEN: {
        "boiler_plate": """You suffer the loathsome effect of foul rituals of rival sorcerers, ill words uttered by
the alien throat of a demon, or unspeakable decrees by entities beyond our world that other mortals call gods. You are
cursed.""",
        "fixed_prompts": [
            "Why were you cursed?",
            "How do you overcome it?"
        ],
        "random_prompts": [
            RandomPrompt("Who cursed you?",
[
    """A cabal of sorcerers you rejected in the past; not more than amateurs in the dark sorceries,
but owners of a powerful artefact.""",
    "A demon enraged by your arrogant quest to find immortality as a simple mortal, destined to wither and die.",
    "An obscure god of a forsaken religion, as a favour to a faithful follower of the disappearing cult."]),
            RandomPrompt("What are the effects of the curse?",
[
    """Your soul is trapped in a common object, your body but a husk tended to by the most faithful servants that
pray for your return.""",
    "You become forgetful and can only remember your spells with signifi cant effort.",
    "You stir hate among all other mortals, weakening your bond with allies and boosting your enemies"])
        ]
    },
    FaceValue.JACK: {
        "boiler_plate": """You encounter a curious companion that follows you on your ambitious quest. Their skills will
be useful in the arcane world of vengeful gods and foul demons you need to navigate before transcending to lichdom.
But do not get too attached, they are dispensable, after all.""",
        "fixed_prompts": [
            "What is their name?",
            "What do they look like?",
            "How do you meet?",
            "Why do they ally with you?"
        ],
        "random_prompts": [
            RandomPrompt("Who is this curious character?",
[
    "An undead sorcerer from the time before the Cataclysm, devoid of most memories and powers.",
    """A witch or shaman that talks the language of the dead and can interpret many secrets of the past and
present through old rituals of blood.""",
"The consciousness of an alien creature inhabiting a homunculus, brought here by a ritual between realities."]),
            RandomPrompt("What is special about them?",
[
    "Sent to you by a god of chaos to aid in your quest, but is growing to hate you.",
    "Has been cursed to never find peace again.",
    "Can bring you knowledge you thought was lost forever."])
        ]
    },
    FaceValue.QUEEN: {
        "boiler_plate": """Your dwelling in dark arts and sorcerous research yields fruits in the form of
powerful rituals, rare spells, dangerous agreements with otherworldly entities, or strange incantations lost in
the tides of time. Such arcane powers can be used to trample your path in your search for immortality, but beware of
their cost on your soul.""",
        "fixed_prompts": [
            "How did you learn this evil sorcery?",
            "Why can you only use it once?",
            "What challenge do you overcome with it?"
        ],
        "random_prompts": [
            RandomPrompt("What arcane ritual of power do you use?",
[
    """A foul ritual to summon a demon lord, and many souls to bargain for its assistance - not for its obedience - in
your mortal matters.""",
    """An incantation using the first words of the first mortal to take dominion over the arcane. Forever lost in the
aether between worlds after they are uttered again in this plane.""",
    """A silent agreement with an elder god, who sends a creature of shadow for you to command and destroy your enemies.
A devourer of souls from a plane that no longer exists."""])
        ]
    },
    FaceValue.KING: {
        "boiler_plate":
            "A terrible unnatural event shakes the world or baleful arcane powers are directed towards you.",
        "fixed_prompts": [
            "Did you cause this catastrophe?",
            "How did you escape and what did it cost you?",
            "How did you change after this event?"
        ],
        "random_prompts": [
            RandomPrompt(
                "",
                [
                    """Your mind gets lost during an astral projection or atavistic voyage to distant times.
What were you looking for? How do you return to your body?""",
                    "Your own shadow separates and tries to possess your body with malevolent intent. What caused it?",
                    """You age many years in a mere instant when you risk a ritual unknown to you.
What were you trying to achieve? Where did you find the ritual?""",
                    """The blood moon, an unpredictable event that rarely happens. All those attune to the arcane suffer
terrible pain that can leave them mad.""",
                    """An invasion of tiny invisible demons that disrupt your life and insist on following you.
Why did they come to you?""",
                    """You read the wrong words in a forsaken tome, teleporting you to a far off place where
a terrible beast lurks."""])
        ]
    }
}