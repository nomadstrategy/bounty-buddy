from bounty_buddy import Tournament, KnockoutTournament


def test_creating_mtt():
    my_mtt = KnockoutTournament(10, 5000)
    assert my_mtt.buyin == 10
    assert my_mtt.starting_stack == 5000
    my_mtt = KnockoutTournament(333, 10000)
    assert my_mtt.buyin == 333
    assert my_mtt.starting_stack == 10000


def test_creating_new_structure_mtt():
    my_mtt = Tournament(bounty_value=0.75, name="SKO", progressive=True)
    assert my_mtt.bounty_value == 0.75
    assert my_mtt.name == "SKO"
    assert my_mtt.progressive == True
