import unittest
import sys

sys.path.append(".")
from game.player import Player, MIN_RESOLVE, MAX_RESOLVE

class PlayerTests(unittest.TestCase):

    def test_increase_doesnt_exceed_cap(self):
        player = Player()
        self.assertEqual(player.resolve, MAX_RESOLVE)
        player.increase_resolve()
        self.assertEqual(player.resolve, MAX_RESOLVE)

    def test_decrease_doesnt_exceed_min(self):
        player = Player()
        while not player.decrease_resolve():
            continue
        self.assertEqual(player.resolve, MIN_RESOLVE)
        player.decrease_resolve()
        self.assertEqual(player.resolve, MIN_RESOLVE)


if __name__ == "__main__":
    unittest.main()