import  enum
import unittest

MAX_RESOLVE = 4
MIN_RESOLVE = 0


class PlayerStat(enum):
    Resolve = 0
    Doom = 1

    def __str__(self):
        match self:
            case PlayerStat.Resolve:
                return "Resolve"
            case PlayerStat.Doom:
                return "Doom"
            case _:
                raise ValueError("Got Unknown Value in PlayerStat: {}".format(self))


class Player:
    resolve: int
    doom: int
    marks_of_corruption: list
    hand = []

    def __init__(self):
        self.resolve = 4
        self.doom = 0
        self.marks_of_corruption = []
        self.hand = []

    def increase_resolve(self):
        self.resolve = min(self.resolve + 1, MAX_RESOLVE - self.doom)

    def game_over(self):
        return self.resolve == MIN_RESOLVE

    def decrease_resolve(self):
        """
        decreases the player's resolve and checks for game over condition
        :return: True if the game is over
        """
        self.resolve = max(MIN_RESOLVE, self.resolve - 1)
        return self.game_over()

    def player_state_str(self):
        return "{} of {}resolve, {} doom".format(self.resolve, MAX_RESOLVE - self.doom, self.doom)



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