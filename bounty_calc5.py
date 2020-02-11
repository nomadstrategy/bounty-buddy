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
    adjusting values below sets defaults
    """

    buyin: int = 10
    starting_stack: int = 10000
    starting_knockout: float = 4.9
    bounty_value = 0.4
    starting_bounty_chipvalue = (starting_stack * bounty_value) / (
        buyin / starting_knockout
    )
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

    def pot_odds(self):
        pass

    def __str__(self):
        return f"""
        ___________________________________________________________________
        ${self.buyin} Bounty Tournament starting with:
        {self.starting_stack} chips/ ${self.starting_knockout} KO -->
        {self.starting_bounty_chipvalue} initial bounty chipvalue
        {self.current_conversion if self.current_conversion else 'new mtt'}
        ____________________________________________________________________"""


@dataclass
class ProgressiveSuperKnockout(BountyTournament):
    buyin: float = 33
    starting_stack: int = 3000
    starting_knockout: float = buyin / 2


@dataclass
class SuperKnockout(BountyTournament):
    buyin: float = 10
    starting_stack: int = 10000
    starting_knockout = buyin / 2
    bounty_value = 0.5
    starting_bounty_chipvalue = starting_stack


@dataclass
class FlatKnockout(BountyTournament):
    buyin: float = 10
    starting_stack: int = 10000


def pot_odds(mtt_instance, current_pot=None, price_to_call=None):
    logging.debug(mtt_instance)
    if not current_pot:
        current_pot = int(input("Enter current potsize:  "))

    if not price_to_call:
        price_to_call = int(input("Enter cost to call:  "))

    final_pot = current_pot + price_to_call  + mtt_instance.convert_bounty()
    pot_odds = price_to_call / final_pot * 100
    return f"pot odds: {round(pot_odds)}%"


a = SuperKnockout()

print(pot_odds(a))
