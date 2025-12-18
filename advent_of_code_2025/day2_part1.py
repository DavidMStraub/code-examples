import data


def is_id_invalid(id_str):
    if len(id_str) % 2 != 0:
        return False
    # length is even!
    half_length = len(id_str) // 2
    first_half = id_str[:half_length]
    second_half = id_str[half_length:]
    return first_half == second_half
    

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
