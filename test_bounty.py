from bounty_calc5.py import *

def test_generic_knockout_tournament_creation():
    assert KnockoutTournament() creates defaults when no arguments passed
    assert KnockoutTournament(10, 5000, 4.9) == default no-arg

def test_easy_call():
    """
    mtt.pko.calc(5) at most 
    pko.calc() and 
    calc(5) would be ideal
    """