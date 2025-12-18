"""Execute this test with `pytest ...`"""

import day2_part2


def test_is_repetition_true():
    assert day2_part2.is_repetition("11", 2)
    assert day2_part2.is_repetition("111", 3)
    assert day2_part2.is_repetition("1111", 2)
    assert day2_part2.is_repetition("1212", 2)


def test_is_repetition_false():
    assert not day2_part2.is_repetition("111", 2)
    assert not day2_part2.is_repetition("12123", 2)


def test_is_id_invalid_true():
    assert day2_part2.is_id_invalid("11")
    assert day2_part2.is_id_invalid("22")
    assert day2_part2.is_id_invalid("111")
    assert day2_part2.is_id_invalid("1188511885")
    assert day2_part2.is_id_invalid("2121212121")

def test_is_id_invalid_false():
    assert not day2_part2.is_id_invalid("5")
    assert not day2_part2.is_id_invalid("12")
    assert not day2_part2.is_id_invalid("113")
    assert not day2_part2.is_id_invalid("1181185")
    assert not day2_part2.is_id_invalid("121812185")
