from enum import Enum
import unittest
from game.cards.card import CardType

MAX_RESOLVE = 4
MIN_RESOLVE = 0


class PlayerStat(Enum):
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

    def increase_doom(self): # Doom does not decrease
        self.doom += 1
        self.resolve = min(self.resolve, MAX_RESOLVE - self.doom)

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
        return "{} of {} resolve, {} doom".format(self.resolve, MAX_RESOLVE - self.doom, self.doom)


    @staticmethod
    def sorted_hand_segment_str(name,lst):
        segment_str = "{} {}".format(len(lst), name)
        for card in lst:
            segment_str = "{}\n{}".format(segment_str, card)
        return segment_str

    def player_hand_str(self):
        truths = []
        influences = []
        companions = []
        plots = []
        scheme_scrys = []

        for card in self.hand:
            match card.cardType:
                case CardType.TRUTH:
                    truths.append(card)
                case CardType.INFLUENCE:
                    influences.append(card)
                case CardType.COMPANION:
                    companions.append(card)
                case CardType.PLOTS_CURSES:
                    plots.append(card)
                case CardType.SCHEME_SCRY:
                    scheme_scrys.append(card)
                case _:
                    raise ValueError("Player had unexpected card in their hand: {}".format(card))
        player_repr_str = ""
        player_repr_str += Player.sorted_hand_segment_str("truths", truths) + "\n"
        player_repr_str += Player.sorted_hand_segment_str("influences", influences) + "\n"
        player_repr_str += Player.sorted_hand_segment_str("companions", companions) + "\n"
        player_repr_str += Player.sorted_hand_segment_str("plots", plots) + "\n"
        player_repr_str += Player.sorted_hand_segment_str("schemes and scrying", scheme_scrys)
        return player_repr_str


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