import data


input_data = data.day4
rows = input_data.splitlines()
num_rows = len(rows)
num_cols = len(rows[0])

# just to be sure there are no ragged rows
for row in rows:
    assert len(row) == num_cols
# ok good.

print(f"We have {num_rows} rows and {num_cols} columns.")

def num_roll_neighbors(lines, i, j):
    """Count the number of neighbouring rolls"""
    num_rows = len(lines)
    num_cols = len(lines[0])
    num = 0
    # top
    if i > 0:
        num += lines[i - 1][j] == "@"
    # bottom
    if i < num_rows - 1:
        num += lines[i + 1][j] == "@"
    # left
    if j > 0:
        num += lines[i][j - 1] == "@"
    # right
    if j < num_cols - 1:
        num += lines[i][j + 1] == "@"
    # top left
    if i > 0 and j > 0:
        num += lines[i - 1][j - 1] == "@"
    # bottom left
    if i < num_rows - 1 and j > 0:
        num += lines[i + 1][j - 1] == "@"
    # top right
    if i > 0 and j < num_cols - 1:
        num += lines[i - 1][j + 1] == "@"
    # bottom right
    if i < num_rows - 1 and j < num_cols - 1:
        num += lines[i + 1][j + 1] == "@"
    return num

num_accessible = 0
for i, row in enumerate(rows):
    for j, char in enumerate(row):
        if char != "@":
            continue
        if num_roll_neighbors(rows, i, j) < 4:
            num_accessible += 1

print(f"The result is: {num_accessible} accessible rolls")
