import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.DEBUG)

"""
example: Starting 10k chips
40% of starting stack for starting bounty
10k * 40 % = 4k chips for starting bounty 


"""


@dataclass
class ProgressiveKO:
    """
    start by displaying default KO and then ask to adjust chips then display that and ask to adjust again till quit
    """

    starting_chips: int = 10000
    buyin: float = 10
    starting_knockout_dollars: float = 4.9
    starting_knockout_chips = starting_chips * 0.4
    logging.debug(
        f"{starting_knockout_chips} chip value of starting bounty with {starting_chips} starting stack"
    )

    # knockout_chips_per_dollar = (
    #     starting_chips * buyin * starting_knockout_dollars
    # )  # holder

    def get_displayed_bounty(self):
        print(f"placeholder: {self}. Press 'Q' to exit and start a new tournament")
        try:
            self.opponent_bounty_dollars: float = float(
                input("Opponents displayed bounty : $")
            )
        except ValueError:
            # if opponent_bounty_dollars.upper() == 'Q'
            print(
                f"Please enter in whole integers only, no symbols, fractions, or decimal values"
            )
            return self.get_displayed_bounty()

        # todo handle float, $ sign, test

        logging.debug(f"${self.opponent_bounty_dollars} opponent_bounty_dollars")
        return self.opponent_bounty_dollars

    def adjust_bounty(self):
        opponent_bounty = self.get_displayed_bounty()

        logging.debug(f"{str(opponent_bounty)}, opponent bounty")

    def __str__(self):
        return f"a Progressive Knockout tournament: ${self.buyin} -- starting with {self.starting_chips} chips, and a ${self.starting_knockout_dollars} initial KO value"


test_pko = ProgressiveKO(10000, 10)
# logging.debug(f"${test_pko.opponent_bounty_dollars} bounty displayed for opponent")
test_pko.adjust_bounty()


def calculate_chip_value(tournament):
    print("***", tournament)


calculate_chip_value(test_pko)


# test_pko.adjust_bounty()

# @dataclass
# class FlatKO:
#     pass


# @dataclass
# class SuperKO:
#     # might be 50% bounties, 75%, variable
#     pass

