# CC-BY-SA 4.0 Jordan Thayer, 2024
# Python-aided Lichdom Solo RPG

from game.action import directory_path_prompt
from game.game import Game

if __name__ == "__main__":
    target_dir = directory_path_prompt()
    instance = Game(target_dir)
    instance.play()
