import data


def is_id_invalid(id_str):
    """Check if an ID is invalid."""
    if len(id_str) < 2:
        return False
    for i in range(2, len(id_str) + 1):
        if is_repetition(id_str, num_reps=i):
            return True
    return False


def is_repetition(id_str, num_reps):
    """Check if an ID string is consisting of num_reps repetitions."""
    if len(id_str) % num_reps != 0:
        return False
    parts = []
    len_part = len(id_str) // num_reps
    for i in range(num_reps):
        part = id_str[i * len_part : (i + 1) * len_part]
        parts.append(part)
    for part in parts:
        if part != parts[0]:
            return False
    return True


ids = data.day2.split(",")

sum_invalid_ids = 0
for id_str in ids:
    id1_str, id2_str = id_str.split("-")
    id1 = int(id1_str)
    id2 = int(id2_str)
    for i in range(id1, id2 + 1):
        i_str = str(i)
        if is_id_invalid(i_str):
            sum_invalid_ids += i

print(f"The sum of all invalid IDs is {sum_invalid_ids}")
