"""
generic knockout class with the functions, subclass specific ones
"""

import logging

logging.basicConfig(level=logging.DEBUG)


class KnockoutTournament:
    """
    A generic knockout tournament with 40% of bounties counting towards chipvalue
    """

    BOUNTY_VALUE = 0.4  # 40%

    def __init__(self, buyin: float, start_chips: int, start_ko: int):
        self.buyin = float(buyin)
        self.starting_stack = int(start_chips)
        self.starting_ko = float(start_ko)
        self.starting_bounty_chips = self.BOUNTY_VALUE * self.starting_stack
        logging.debug(
            f"{self.buyin}, {self.starting_stack}, {self.starting_ko}, {self.starting_bounty_chips}"
        )

    @classmethod
    def calculate_bounty(cls, displayed_bounty: float = None):
        logging.debug(
            f"{cls.__name__} class, with a ${displayed_bounty} displayed bounty"
        )
        cls.updated_bounty = displayed_bounty or float(
            input("What is the displayed bounty? $")
        )
        logging.debug(f"${cls.updated_bounty} updated bounty")

    def __str__(self):
        return f"""
        a Progressive Knockout tournament with a ${self.buyin} buyin. 
        {self.starting_stack} starting chips, ${self.starting_ko} initial bounty 
        """


test_ko = KnockoutTournament(10, 10000, 4.9)

test_ko.calculate_bounty(4.9)

# for test_displayed_bounty in range(5, 100, 5):
#     print(test_ko.calculate_bounty(test_displayed_bounty))

