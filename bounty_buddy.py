import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.DEBUG)


class KnockoutTournament:
    """
    basic tournament bones
    """

    BOUNTY_VALUE = 0.4

    def __init__(self, buyin, starting_stack, _format=None):
        self.buyin = float(buyin)
        self.starting_stack = int(starting_stack)
        self._format = _format


mtt = KnockoutTournament(10, 3000, "SKO")

print(mtt)

