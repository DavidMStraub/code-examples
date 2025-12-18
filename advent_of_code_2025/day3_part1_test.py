import day3_part1


def test_find_largest_joltage():
    assert day3_part1.find_largest_joltage("77") == 77
    assert day3_part1.find_largest_joltage("177") == 77
    assert day3_part1.find_largest_joltage("771") == 77
    assert day3_part1.find_largest_joltage("717") == 77
    assert day3_part1.find_largest_joltage("78") == 78
    assert day3_part1.find_largest_joltage("178") == 78
    assert day3_part1.find_largest_joltage("781") == 81
    assert day3_part1.find_largest_joltage("718") == 78
