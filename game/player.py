from enum import Enum
from game.cards.card import CardType, Card

MAX_RESOLVE = 4
MIN_RESOLVE = 0


class PlayerStat(Enum):
    Resolve = 0
    Doom = 1

    def __str__(self):
        self.name


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
    
    def dehydrate(self):
        return {
            "resolve": self.resolve,
            "doom": self.doom,
            "marks_of_corruption": self.marks_of_corruption,
            "hand": [ card.dehydrate() for card in self.hand ]
        }
    
    @staticmethod
    def hydrate(data):
        player = Player()
        player.resolve = data["resolve"]
        player.doom = data["doom"]
        player.marks_of_corruption = data["marks_of_corruption"]
        player.hand = [ Card.hydrate(card_data) for card_data in data["hand"] ]
        return player
