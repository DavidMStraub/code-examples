import data

banks = data.day3.split()


def find_largest_joltage(bank):
    for i in range(99, 9, -1):
        i_str = str(i)
        first_digit, second_digit = i_str
        pos_first_digit = bank.find(first_digit)
        if pos_first_digit < 0:
            continue
        # we don't want to use that instance of the digit twice
        bank_modified = bank.replace(first_digit, "X", 1)
        # position from the back! -> last instance
        pos_second_digit = bank_modified[::-1].find(second_digit)
        if pos_second_digit < 0:
            continue
        pos_second_digit = len(bank) - pos_second_digit
        if pos_second_digit > pos_first_digit:
            return i
    return -1  # this should be unreachable!


output_joltage = 0
for bank in banks:
    largest_joltage = find_largest_joltage(bank)
    output_joltage += largest_joltage


print(f"The output joltage is {output_joltage}.")
