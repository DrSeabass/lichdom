# lichdom-in-python
This is an implementation of the solo journaling TTRPG Lichdom.  Whereas the base game was designed to be played
with dice, a standard 52-card deck, pens, and paper, this version is (currently) meant to be played through the
python REPL.

I'm hoping this improves some things I found frustrating about the player experience:
* Physically journaling my game made it hard to share with others online
* Maintaining the state of the deck between play sessions was tedious
* Flipping back and forth in the PDF / physical book when drawing cards slowed play

# TODOs
* Some RandomPrompts have no base string, and only selections.  Change how they are emitted.
* Allow for a compelled selection to require user input
* Clean up text display
* Make save game representation human-readable
* Add ability to flush text prompts into some archival format
* Implement a proper state machine & command / action pattern for game logic

# Outside Refrences

## [License CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

## [Lichdom](https://preview.drivethrurpg.com/en/product/399971/Lichdom--A-solo-RPG-about-the-perilous-journey-of-a-sorcerer-towards-immortality)

* Design & Writing by Adrian Lopez Sanjuan.
* Editing by Noelia Garcia Novas.
* Most of the art by dead people, remnants of another time long
forgotten by mortals. Additional art by Henrik Karppinen.

* Lichdom © 2022 by Adrian Lopez Sanjuan is licensed under
CC BY-SA 4.0. You are free to share and adapt this material as
long as you give attribution and use the same license.