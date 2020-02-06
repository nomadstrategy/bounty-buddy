"""
test_pko = ProgressiveKO(10000, 10)
pko() 
-> returns value
"""
import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.DEBUG)
# 1:23 yd


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
        try:
            displayed_bounty = float(input("What is opponents bounty? : $"))
            logging.debug(f"${displayed_bounty} bounty displayed")
        except:
            print("You must pass a number > 0")
            self.update_bounty()


test_pko = ProgressiveKO()
test_pko.update_bounty()
logging.debug(
    f"{test_pko.bounty_dollars_chipvalue()} chipvalue with these parameters: \n{test_pko}"
)
