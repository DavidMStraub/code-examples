import data


def n_times_crossed_zero(start, amount, sign):
    """How often we cross zero given start, amount, and
    direction sign (L=-1, R=+1)."""
    position = start
    n_crossed_zero = 0
    for _ in range(amount):
        position += sign
        position %= 100
        if position == 0:
            n_crossed_zero += 1
    return n_crossed_zero


if __name__ == "__main__":
    position = 50  # starting position
    times_zero = 0  # how often we pointed at 0
    for line in data.day1.splitlines():
        direction = line[0]  # L or R
        amount = int(line[1:])
        if direction == "L":
            sign = -1
        elif direction == "R":
            sign = +1
        else:
            raise ValueError(f"Unable to detect direction in line {line}")
        times_zero += n_times_crossed_zero(position, amount, sign)
        position = position + sign * amount
        # set position modulo 100
        position %= 100

    print(f"Part 2: the dial pointed at zero {times_zero} times.")
