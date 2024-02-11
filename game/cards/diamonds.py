from game.cards.card import FaceValue, RandomPrompt

card_slugs = {
    FaceValue.ACE: {
        "boiler_plate":
            """A truth of this world that gives you power over death and places you above all other mortals,
            giving you a chance at immortality.
            """,
        "fixed_prompts": [],
        "random_prompts": [
            RandomPrompt(
                "Where do you find it?",
                [
                    """The fundamental secrets of reality, whispered to the first mage to ever walk this world. A gift
                    hidden in the firmament.""",
                    """Revealed by the ancient traditions and legends of a disappearing tribe. You had to submit
                    them to your will to reveal their secrets.""",
                    """Discovered by alchemical research and bloody experimentation at the cost of many lives."""]),
            RandomPrompt("What is it?", [
                """Rejuvenate your ageing body by consuming the flesh of the youthful under a blood moon.""",
                """Life force can be extracted from mortals from the distillation of their humours, producing pure
                life essence that will extend your life and give you strength.""",
                """Elder trees never die, their roots extend below ground and control the undying cycle of nature.
                You learn the reason for their eternal existence, or fi nd a way to merge your body
                into the immortal tree."""
            ])
        ]
    },
    FaceValue.TWO: {
        "boiler_plate":
            """Treacherous thieves tried to steal one of your most precious artefacts, shrouded by the darkness of a
            moonless night. You are disturbed and impressed that they managed to bypass all your mundane and
            arcane precautions, and you suspect they had help. Their admirable efforts, however, turned out to be
            fruitless when you sensed their presence and found them within your tower. They had no escape, and so they
            died in terrible agony; their screams uttering the name of whom you now seek with a vengeful heart.""",
        "fixed_prompts": [
            "What did they try to steal and why is it important?",
            "What precautions did you have in place and why did they fail?",
            "Who helped or guided them in their failed quest?",
            "Was it an established enemy or treachery within your own household?"
        ],
        "random_prompts": [
            RandomPrompt("Who sent the thieves?",
                         [
                             """The Circle of Sequestered Mystics, collectors of ancient wonders that practice restraint in magic.""",
                             """The Mercantile Guild, who seeks profit above all else.""",
                             """Nobody. A thief with an ambition reaching further than his skills. You like him, but failure has a price"""])
        ]
    },
    FaceValue.THREE: {
        "boiler_plate": """The vile abomination you created escaped from its foul pit of death. It killed and
        consumed many of your servants in a rampage of hate, blood, and desperation. It was amusing at first,
        but you had to finally kill it before it wrecked havoc beyond repair. The experiment can be considered
        a failure, as the creature could not be controlled reliably to do your bidding, but at least you gained 
        a wealth of non-sorcerous knowledge on the inner workings of several species, alchemical concoctions,
        and surgery.""",
        "fixed_prompts": [
            "What abomination did you create?",
            "How was this monster contained and how did you kill it?",
            "Was this creature your only organic experiment, or one of many in your laboratory?"
        ],
        "random_prompts": [
            RandomPrompt("Why did you create it?",
                         [
                             """To learn and understand secrets that could extend your own life in the future through unnatural means.""",
                             """As a stealthy and faithful killer; a creature unclouded by conscience, remorse, or delusions of morality to send
    against your enemies.""",
                             """To clone key powerful fi gures that you planned on supplanting by your mind controlled puppets."""])
        ]
    },
    FaceValue.FOUR: {
        "boiler_plate":
            """The bloodthirsty heir of an old ruling dynasty has come to power by treachery and murder, and
            you helped or failed to prevent it. Discontent spreads and revolution is imminent, but the iron fist
            of the new ruler keeps the population in check with ruthless practices and well paid mercenaries,
            while the coffers of the kingdom are wasted in bribes and steel.""",
        "fixed_prompts": [
            "Why did you help or oppose the change? Are you an associate of the new or old regime?",
            "Why did you get involved? Do you owe any favours or made a deal for your own benefit?"
            "How do you ensure the new rulers stay in power or how do you remove them from the throne?",
            "Do you face any consequences for it?"
        ],
        "random_prompts": [
            RandomPrompt("Who is the new ruler?",
                         [
                             """Salome, who took the throne from her sister with lies and tricks. She worships
                             a dreaded god and sacrifices citizens to its avatar.""",
                             """Yyrkoon, who had the support of other noble dynasties and declared
                             the rightful ruler an outlaw.""",
                             """Numedides, who had the support of a neighbouring kingdom and help from rare
                            and ancient sorcery."""])
        ]
    },
    FaceValue.FIVE: {
        "boiler_plate":
            """A noble house or warlord seeks your help to curse their enemies with crippling pain and horrible death.
            They can’t openly move against their foes, and so they depend on your sorcery to achieve their
            ambitious goals. Curses should not be used lightly, as you may call forces diffi cult to control, but either
            for your own benefit or the pain of your common enemies, you decide to employ your dark arts
            to end a dynasty.""",
        "fixed_prompts": [
            "Who needs your help and why do you help them?",
            "What do you claim in return? Simple riches or a blind eye on your activities in their domain?",
            "What ritual do you use and who dies in the process?",
            "Why do they need to use horrible sorcery?"
        ],
        "random_prompts": [
            RandomPrompt("How do you curse their enemies with foul sorcery?",
                         [
                             """A disease that rots the mind and turns them mad with agony.
                             Death is their only escape to their personal hell.""",
                             """A curse on their family. All descendants die horribly before adulthood and
                             the continuity of their noble line is at dire risk.""",
                             """Their lands dry to ash and financial ruin shatters their long legacy."""])
        ]
    },
    FaceValue.SIX: {
        "boiler_plate": """You use violence to obtain valuable information. You learn about the plans and hopes of
        other parties from the insatiable greed or unbearable torture of their followers; whispered secrets and
        screamed weaknesses that you can now use to your advantage.""",
        "fixed_prompts": [
            "What do you learn that gives you hope?",
            "What do you scheme to profi t from what you have learned?",
            "Who dies as a result of your spying and scheming? Was it a planned move?",
            "Who else is an accomplice of your schemes? Do they owe you a favour or are they acting on self-interest?",
        ],
        "random_prompts": [
            RandomPrompt("How do you learn it?",
                         [
                             """From the loose tongue of a disgruntled servant, willing to exchange
                             the invaluable secrets of their master for common gold. Fool.""",
                             """Promises yelled under torture by a spy uncovered in your own household; but can you
                             trust the secrets screamed in her horrifying agony?""",
                             """Threats to clerks and scribes of the Mercantile Guild, who reveal secrets whispered in 
                             confidential meetings held under the Jade Spire of the ancient city of Lagash."""])
        ]
    },
    FaceValue.SEVEN: {
        "boiler_plate":
            """You face a legendary beast of tremendous power. Folk tales shroud the creature in mysticism and fear,
            and history books tell the story of heroic mortals that perished in their attempt to destroy
            its dark soul.""",
        "fixed_prompts": [
            "Who dies in the fight?",
            "Where do you fi ght it?"
        ],
        "random_prompts": [
            RandomPrompt("Why do you confront this beast?", [
                """It protects the Iron Eye of the Blind God, an artefact that allows strong minds to embark
                on a dangerous atavistic voyage.  What horrors do you see in the distant past?""",
                """You awakened it from its slumber of ages to find answers. What do you ask when you defeat it?""",
                """You need its black and poisonous heart for a sorcerous concoction. What alchemy are you trying to 
                create?"""]),
            RandomPrompt("What is this creature?", [
                """A serpent-demon with a tongue of stone and eyes that see into several realities.""",
                """A tentacled horror beyond this world that consumes flesh and light with its demonic maw.""",
                """An intelligent and terrifying chimera escaped from the laboratory of a sorcerer."""])
        ]
    },
    FaceValue.EIGHT: {
        "boiler_plate":
            """Assassins are sent against you by your most hated enemies. You have been suspecting their intentions for
            a long time, but never thought they would dare to openly move against you. Especially in such a crude way.
            You have no option but to retaliate; but you won’t fail, and their screams will reverberate in the vaults
            and corridors of your domain for many long days.""",
        "fixed_prompts": [
            "Who sent them against you and why?",
            "How did you survive and how did you take revenge?",
        ],
        "random_prompts": [
            RandomPrompt("How did they attempt murder?", [
                """They poisoned your food, but someone else tried it first and died in agony.""",
                """Trespassers revealed by their furtive steps in the night and the glimmer of murderous blades.""",
                """A shadow demon hidden in the body of a servant tried to steal your soul."""]),
            RandomPrompt("How did they get close to you?", [
                """Someone helped them to defeat your protections with sorcerous knowledge.""",
                """They infiltrated your household long ago pretending to be servants.""",
                """On your way to the court of a noble. They knew you were coming"""])
        ]
    },
    FaceValue.NINE: {
        "boiler_plate":
            """Your dark arts attract the attention of a famous warrior set on ending your life. The clever warrior 
            seeks you relentlessly carrying some protection against magic. Only powerful sorcery can help you
             to defeat this enemy.""",
        "fixed_prompts": [
            "Why does the warrior want your death?",
            "Where do you meet? Do you prepare for the encounter?",
            "What is the nature of the warrior’s magical protection?"
        ],
        "random_prompts": [
            RandomPrompt("Who is this warrior?", [
                """A lonely steel wielding barbarian with gigantic melancholies and gigantic mirth.""",
                """An iron-clad knight who wanders the land with a faithful squire.""",
                """A head hunter of an uncivilised tribe beyond the great gorge that splits the Plains of Ash."""]),
            RandomPrompt("Why is the warrior coming to kill you?", [
                """Revenge, either misplaced or justified, guides their path towards you.""",
                """Sworn to destroy all dark sorcery in the name of a temple of good and light.""",
                """The glory that comes from claiming your head and the profitable loot to be found."""])
        ]
    },
    FaceValue.TEN: {
        "boiler_plate": """Enemies conspire against you and plot your failure, striking at a critical moment.""",
        "fixed_prompts": [
            "Who conspired against you and why?",
            "How is violence involved in the treachery?"
        ],
        "random_prompts": [
            RandomPrompt("Who works against you?", [
                """The Mercantile Guild, seeking retribution over an old grudge that nobody remembers, but bureaucracy
                is slow and due revenge comes late.""",
                """The Temple of the Undying Light, too ambitious to let pass an opportunity to hurt you and
                increase their influence.""",
                """The Company of the Purple Heart, a daring band of mercenaries hired by an old enemy to disrupt your
                plans."""]),
            RandomPrompt("How did they conspire?", [
                """A hired killer is sent against you and your servants, forcing you to deal with it before it becomes
                a bigger problem.""",
                """The assault of your tower and theft of an artefact you need to achieve your goals,
                leaving a trail of death.""",
                """A murder of a minor ally from which you expected service at a critical moment."""])
        ]
    },
    FaceValue.JACK: {
        "boiler_plate": """You encounter a mortal companion that follows you on your ambitious quest. Their skills will
        be useful in the mundane world of violence and threats you need to navigate before transcending to lichdom.
        But do not get too attached, they are mortal and dispensable, after all.        """,
        "fixed_prompts": [
            "What is their name?",
            "What do they look like?",
            "How do you meet?",
            "Why do they ally with you?"
        ],
        "random_prompts": [
            RandomPrompt("Who is this curious character?", [
                "A seasoned warrior, a captain veteran of many slaughters and a natural leader when blades shine.",
                "An assassin who sold their soul to a terrible god to become as silent as the shadow of death itself.",
                "A fallen knight of a religious order, full of shame and greed."""]),
            RandomPrompt("What is special about them?", [
                """Came back from death and is compelled to aid you by ancient sorcery, but he truly hates you.""",
                """Has many contacts in the higher casts of society, where she is feared as an envoy of death.""",
                """Has been exiled from her land and seeks revenge."""])
        ]
    },
    FaceValue.QUEEN: {
        "boiler_plate": """Someone powerful owes you a favour or takes your coin to do your bidding. Valuable help from
        simple minded mortals, no more than a tool to be used and discarded in your quest for immortality. Peons on
        a game of gods that have the power to decide who enslaves them.""",
        "fixed_prompts": [
            "What did you do for them or how much do you pay for their services?",
            "Do they fear the horrifying consequences of not being faithful to their obligations?",
            "How do they help you to overcome a challenge?",
            "What happens to them if they fail?"
        ],
        "random_prompts": [
            RandomPrompt("Who owes you a favour or takes your coin?", [
                """The Silent Death, a secretive guild of assassins that pride themselves on their obscure traditions
                and efficiency. You suspect someone you know is behind the organisation.""",
                """The Blades of the Purple Heart, a mercenary company with the ruthlessness to make your dark bidding
                without moral quarrels or remorse.""",
                "You have evidence, either true or fabricated, to blackmail an aggressive but simple minded warlord."])
        ]
    },
    FaceValue.KING: {
        "boiler_plate":
            "A terrible mundane event that shakes your place in the world, political landscape and society.",
        "fixed_prompts": [
            "Did you cause this catastrophe?",
            "How did you escape and what did it cost you?",
            "How did you change after this event?"
        ],
        "random_prompts": [
            RandomPrompt("", [
                """War ravages the land, crops go unharvested, fire consumes cities and blood feeds the soil.
                How are you involved?""",
                """You are ambushed on your way to another place. Where were you headed? Who or what attacks you?""",
                """The people rise in arms against their masters; a revolution spreads like wildfire across the land
                and many of your servants decide to join in. How did it start?""",
                """A meeting in a far off place with whom you thought to be an ally becomes a deathly trap.
                Who is the traitor?""",
                """Something valuable is stolen from you, such a tome of forgotten lore or an artefact from before
                the Cataclysm. Who did it? What was stolen?""",
                """You are attacked in your own home by an angry mob, cultists, or soldiers paid by an old enemy.
                How do you defend yourself?"""])
        ]
    }
}
