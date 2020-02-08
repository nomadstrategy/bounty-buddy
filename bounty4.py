import logging

logging.basicConfig(level=logging.DEBUG)

from dataclasses import dataclass


@dataclass
class ProgressiveKO:
    """
    start by displaying default KO and then ask to adjust chips then display that and ask to adjust again till quit
    """

    DEFAULT_BOUNTY_VALUE_PERCENT = 0.4

    starting_chips: int = 10000
    buyin: float = 10
    starting_knockout_dollars: float = 4.9
    # lastly to update percent value of bounty (ie:
    # $10 entry, $4.9 bounties, 10,000 starting stack, defaults to DEFAULT_BOUNTY_VALUE_PERCENT = 0.4)
    # the default bounty % means an initial KO is worth 10000*0.4 = 4000 chips
    bounty_value_percent: float = DEFAULT_BOUNTY_VALUE_PERCENT

    """
    chips from bounty: (current bounty / initial bounty) * bounty value  * starting stack
    """

    def convert_bounty(self, current_bounty: float = None):
        if current_bounty:
            self.current_bounty = current_bounty
            logging.debug(self.current_bounty)
        else:
            self.current_bounty = float(input("Enter displayed bounty: $"))

        logging.debug(self.current_bounty)


a = ProgressiveKO(5000, 25, 12.5)

print(a.current_bounty)
