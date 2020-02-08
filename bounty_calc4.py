"""
generic knockout class with the functions, subclass specific ones
"""

import logging

logging.basicConfig(level=logging.INFO)


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
            f"BI ${self.buyin}, ss: {self.starting_stack}, start KO ${self.starting_ko},start bounty chipval {self.starting_bounty_chips}"
        )

    @classmethod
    def get_new_bounty(cls, displayed_bounty: float = None):

        logging.debug(
            f"{cls.__name__} class, with a ${displayed_bounty} displayed bounty"
        )
        cls.displayed_bounty = displayed_bounty or float(
            input("What is the displayed bounty? $")
        )

        logging.debug(
            f"${cls.displayed_bounty} now set as the tournaments displayed bounty"
        )
        return cls.displayed_bounty

    def calculate_bounty(self, bounty=None):
        if not bounty:
            bounty = self.get_new_bounty()
        current_chipvalue_for_ko = (
            bounty / self.starting_ko
        ) * self.starting_bounty_chips
        return current_chipvalue_for_ko

    def __str__(self):
        return f"""
        a Progressive Knockout tournament with a ${self.buyin} buyin. 
        {self.starting_stack} starting chips, ${self.starting_ko} initial bounty,
        ${self.displayed_bounty} currently displayed bounty 
        """


"""working basic generator

Returns:
    class KnockoutTournament():
        filled out the basic requirements -- returns a knockout MTT with specified parameters
"""

# def make_mtt():
#     print("Enter the required information for a tournament")
#     buyin = float(input("Enter the buyin for the tournament : $"))
#     starting_stack = int(input("Enter the starting chip count: "))
#     initial_ko = float(input("Enter the starting KO displayed: $"))
#     return KnockoutTournament(buyin, starting_stack, initial_ko)


# my_tournament = make_mtt()
# print(my_tournament.starting_stack)

# if __name__ == '__main__':
#     make_mtt()
