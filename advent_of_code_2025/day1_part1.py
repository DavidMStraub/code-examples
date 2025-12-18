import data


position = 50  # starting position
times_zero = 0  # how often we pointed at 0
for line in data.day1.splitlines():
    direction = line[0]  # L or R
    amount = int(line[1:])
    if direction == "L":
        position -= amount
    elif direction == "R":
        position += amount
    else:
        raise ValueError(f"Unable to detect direction in line {line}")
    # set position modulo 100
    position %= 100
    if position == 0:
        times_zero += 1

print(f"Part 1: the dial pointed at zero {times_zero} times.")
