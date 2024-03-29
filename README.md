# lichdom-in-python
This is an implementation of the solo journaling TTRPG Lichdom.  Whereas the base game was designed to be played
with dice, a standard 52-card deck, pens, and paper, this version is (currently) meant to be played through the
python REPL and [obsidian](https://obsidian.md/), a text editor capable of displaying markdown files and showing linkages between them.

I'm hoping this improves some things I found frustrating about the player experience:
* Physically journaling my game made it hard to share with others online
* Maintaining the state of the deck between play sessions was tedious
* Flipping back and forth in the PDF / physical book when drawing cards slowed play

# TODOs
* Pull classes apart into separate python files
* Introduce better package structure
* Clean up text display
* Lift replacement of newlines to string into slug loading or card construction
* Allow for a compelled selection to require user input
* Delete journal entries beyond game state when loading game
* Make save game representation human-readable
* Implement a proper state machine & command / action pattern for game logic

# Outside References

## [License CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

## [Lichdom](https://preview.drivethrurpg.com/en/product/399971/Lichdom--A-solo-RPG-about-the-perilous-journey-of-a-sorcerer-towards-immortality)

* Design & Writing by Adrian Lopez Sanjuan.
* Editing by Noelia Garcia Novas.
* Most of the art by dead people, remnants of another time long
forgotten by mortals. Additional art by Henrik Karppinen.

* Lichdom © 2022 by Adrian Lopez Sanjuan is licensed under
CC BY-SA 4.0. You are free to share and adapt this material as
long as you give attribution and use the same license.

## [Obsidian](https://obsidian.md/)
The output directory for the game is designed to be used as an obsidian vault.  This allows you to cross-reference elements from the journal entries and game elements.  It also provides as pace for you to do whatever creative writing you'd like to do with the game's prompts, and gives you an easy mechanism for sharing that writing with others.