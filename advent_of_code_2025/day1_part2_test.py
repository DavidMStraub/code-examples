"""Execute this test with `pytest ...`"""

import day1_part2


# Note: this could be done more elegantly with pytest.mark.parametrize
def test_n_times_crossed_zero_positive():
    assert day1_part2.n_times_crossed_zero(start=1, amount=1, sign=1) == 0
    assert day1_part2.n_times_crossed_zero(start=0, amount=1, sign=1) == 0
    assert day1_part2.n_times_crossed_zero(start=1, amount=98, sign=1) == 0
    assert day1_part2.n_times_crossed_zero(start=1, amount=99, sign=1) == 1
    assert day1_part2.n_times_crossed_zero(start=0, amount=100, sign=1) == 1
    assert day1_part2.n_times_crossed_zero(start=-1, amount=100, sign=1) == 1
    assert day1_part2.n_times_crossed_zero(start=-1, amount=101, sign=1) == 2
    assert day1_part2.n_times_crossed_zero(start=50, amount=1000, sign=1) == 10


def test_n_times_crossed_zero_negative():
    assert day1_part2.n_times_crossed_zero(start=-1, amount=1, sign=-1) == 0
    assert day1_part2.n_times_crossed_zero(start=0, amount=1, sign=-1) == 0
    assert day1_part2.n_times_crossed_zero(start=-1, amount=98, sign=-1) == 0
    assert day1_part2.n_times_crossed_zero(start=-1, amount=99, sign=-1) == 1
    assert day1_part2.n_times_crossed_zero(start=0, amount=100, sign=-1) == 1
    assert day1_part2.n_times_crossed_zero(start=1, amount=100, sign=-1) == 1
    assert day1_part2.n_times_crossed_zero(start=1, amount=101, sign=-1) == 2
    assert day1_part2.n_times_crossed_zero(start=-50, amount=1000, sign=-1) == 10
