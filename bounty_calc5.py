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
"""


@dataclass
class BountyTournament:
    """
    generic bounty tournament structure
    """

    buyin: int = 10
    starting_stack: int = 10000
    starting_knockout: float = 4.9
    bounty_value = 0.4
    starting_bounty_chipvalue = starting_stack * bounty_value
    current_conversion = None

    def convert_bounty(self, bounty=None):
        """
        return adjusted chipvalue from a new bounty
        """
        print(self)
        if not bounty:
            bounty = float(input("Enter current bounty displayed:  $ "))

        self.current_conversion = round(
            (bounty / self.starting_knockout) * (self.starting_bounty_chipvalue),
        )
        print(f"${bounty} converts to --> {self.current_conversion} chips")
        return self.current_conversion

    def __str__(self):
        return f"""
        ___________________________________________________________________
        ${self.buyin} Bounty Tournament starting with:
        {self.starting_stack} chips/ ${self.starting_knockout} KO -->
        {self.starting_bounty_chipvalue} initial bounty chipvalue
        {self.current_conversion if self.current_conversion else 'new mtt'}
        ____________________________________________________________________"""


mtt = BountyTournament(buyin=20, starting_stack=10000, starting_knockout=9.8)
mtt.convert_bounty(33)
print(mtt.current_conversion)
