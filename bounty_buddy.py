import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.DEBUG)


"""
Generic KO tournaments easily generated
example:
mtt = BountyTournament(buyin=10, starting_stack=10000, starting_knockout=4.9)
(Default settings)

mtt.convert_bounty() --> prompts for displayed opponent bounty, converts
mtt.convert_bounty(9.8) --> converts $9.8 displayed bounty to chipvalue

start 10k chips
starting bounty: 22
10k * 40% = 4k
4k per starting bounty
"""


class BountyTournament:
    """
    generic bounty tournament structure
    adjusting values below sets defaults
    """

    def __init__(self, starting_stack, starting_bounty, bounty_rate=0.4):
        self.starting_stack = starting_stack
        self.starting_bounty = starting_bounty
        self.bounty_rate = bounty_rate
        self.initial_bounty_value = round(self.starting_stack * self.bounty_rate)

    def convert_bounty(self, displayed_bounty=None):
        if not displayed_bounty:
            displayed_bounty = float(input("Enter the displayed bounty... $"))
        bounty_value = self.initial_bounty_value * (
            displayed_bounty / self.starting_bounty
        )
        print(
            f"{self}\ncurrent bounty ${displayed_bounty} is worth \
            {bounty_value} chips"
        )
        return bounty_value

    def __str__(self):
        return f"""
        ___________________________________________________________________
        Bounty Tournament starting with:
        {self.starting_stack} chips/ ${self.starting_bounty} KO -->
        {self.initial_bounty_value} initial bounty chipvalue
        ____________________________________________________________________"""


my_mtt = BountyTournament(10000, 22)
# print(my_mtt.initial_bounty_value)
# print(my_mtt)

# my_mtt.convert_bounty(44)


def get_pot_odds(tournament=None):
    """
    Enter a tournament to add bounty chips to pot when opponent at risk.
    """
    current_pot = int(input("Enter current pot size: "))
    facing_bet = int(input("Enter the cost to call: "))
    total_pot = current_pot + facing_bet
    if tournament:
        total_pot += tournament.convert_bounty()

    logging.debug(f"cost: {facing_bet}, total pot: {total_pot}")
    pot_odds = (facing_bet / total_pot) * 100
    logging.debug(pot_odds)
    print(f"{round(pot_odds)}% equity needed to call")
    return pot_odds


print(get_pot_odds(my_mtt))
