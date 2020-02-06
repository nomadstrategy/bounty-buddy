"""
test_pko = ProgressiveKO(10000, 10)
pko() 
-> returns value
"""
import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.DEBUG)


@dataclass
class ProgressiveKO:

    buyin: float = 10
    starting_stack: int = 10000
    bounty: float = 4.9
    knockout_rate: float = 0.4
    starting_bounty_chipvalue = starting_stack * knockout_rate

    def bounty_dollars_chipvalue(self, bounty: float = bounty):
        return (bounty / self.bounty) * self.starting_bounty_chipvalue

    def update_bounty(self):
        displayed_bounty = int(input("What is opponents bounty? : $"))
        logging.debug(f"${displayed_bounty} bounty displayed")


test_pko = ProgressiveKO()
logging.debug(
    f"{test_pko.bounty_dollars_chipvalue()} chipvalue with these parameters: \n{test_pko}"
)

test_pko.update_bounty()
