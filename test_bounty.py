from bounty_buddy import BountyTournament
import logging

logging.basicConfig(level=logging.DEBUG)


def test_creating_mtt():
    my_mtt = BountyTournament(10, 5000)
    assert my_mtt.buyin == 10
    assert my_mtt.starting_stack == 5000
    my_mtt = BountyTournament(333, 10000)
    assert my_mtt.buyin == 333
    assert my_mtt.starting_stack == 10000


def test_conversions():
    my_mtt = BountyTournament(10, 10000)
    assert my_mtt.starting_bounty_chipvalue == (
        my_mtt.bounty_value * my_mtt.starting_stack
    )
    assert (
        my_mtt.convert_bounty(10)
        == (10 / my_mtt.starting_knockout) * my_mtt.starting_bounty_chipvalue
    )


"""
# def test_creating_new_structure_mtt():
#     my_mtt = BountyTournament(bounty_value=0.75, name="SKO", progressive=True)
#     assert my_mtt.bounty_value == 0.75
#     assert my_mtt.name == "SKO"
#     assert my_mtt.progressive == True



test calculations and features of the bounty calculator and use cases

User Story: 
user should be able to call tournaments as easily as possible.

#1. Users should be able to create a custom tournament
    *factory function for classes?
    # buyin, starting stack different for each tournament
    # knockout type, value might be consistent between all types 
    # tournament = knockout(bounty_value=0.4, starting_bounty=0.5, bounty_earned=0.5)

#2. Users should be able to easily get bounty conversions

    #   $10 Bounty Tournament starting with:
        10000 chips/ $4.9 KO -->
        10000 initial bounty chipvalue
        ... enter new bounty to get an updated chipvalue (or q, h, n): --> ...
    #

#3. Users should be able to continue working on a tournament until finished
    # while True... break on 'q'

#4  easy to understand syntax. 
# mtt = pko(10,3000) --> progressive knockout with 10 bi, 3000 starting chips
# mtt.calc(30) --> displays pko(10,3000).calc(30) or as needed (30 displayed bounty)

#5 pot-odds including adjusted bounty chipvalue
"""
