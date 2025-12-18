"""Execute this test with `pytest ...`"""

import day2_part1


# Note: this could be done more elegantly with pytest.mark.parametrize
def test_is_id_invalid_false():
    assert not day2_part1.is_id_invalid("1")
    assert not day2_part1.is_id_invalid("12")
    assert not day2_part1.is_id_invalid("12123")

def test_is_id_invalid_true():
    assert day2_part1.is_id_invalid("11")
    assert day2_part1.is_id_invalid("22")
    assert day2_part1.is_id_invalid("2323")
    assert day2_part1.is_id_invalid("35893589")
