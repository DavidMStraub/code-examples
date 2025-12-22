import data
import numpy as np


input_data = data.day4
rows = input_data.splitlines()
num_rows = len(rows)
num_cols = len(rows[0])

# just to be sure there are no ragged rows
for row in rows:
    assert len(row) == num_cols
# ok good.

print(f"We have {num_rows} rows and {num_cols} columns.")

# 0, 1 array padded on each side with zeros
# (so we don't have any boundary effects to worry about!)
is_roll = np.zeros((num_rows + 2, num_cols + 2), int)
for i, row in enumerate(rows):
    for j, char in enumerate(row):
        if char == "@":
            is_roll[i + 1, j + 1] = 1

# Add all 8 possible shifts (omitting the padding)
num_adjacent_rows = (
    is_roll[2:,1:-1]
    + is_roll[:-2,1:-1]
    + is_roll[1:-1,2:]
    + is_roll[1:-1,:-2]
    + is_roll[2:,2:]
    + is_roll[:-2,:-2]
    + is_roll[2:,:-2]
    + is_roll[:-2,2:]
)

is_accessible = (num_adjacent_rows < 4) & is_roll[1:-1,1:-1]
num_accessible = np.sum(is_accessible)

print(f"The result is: {num_accessible} accessible rolls")
