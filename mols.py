"""
Generate a spot it deck using MOLS.
"""

from library import (
    file_names,
    infinity_points
)

from mols_helpers import (
    print_mols,
    index_objects,
    next_square,
    find_line
)

size = 8
# Generate the MOLS
square = index_objects(file_names)
print_mols(square, size)

mols_cards = []
infinity_points_card = []

for infinity_point in infinity_points:
    infinity_points_card.append(square[infinity_point])
    mols_cards.append(f"infinity point: {infinity_point}")
    if infinity_point == "horizontal":
        for start_row in range(size):
            mols_cards.append(find_line((start_row, 0), infinity_point, size, square))
    else:
        for start_column in range(size):
            mols_cards.append(find_line((0, start_column), infinity_point, size, square))

mols_cards.append(infinity_points_card)

# print(find_line((0, 1), "horizontal", size, square))

# for infinity_point in infinity_points:
#     print(infinity_point)
#     print(find_line((0, 1), infinity_point, size, square))


# Testing next_square function

# first_tuple = (1, 6)
# print(f"{first_tuple}: {square[first_tuple]}")
# next_tuple = next_square("vertical", size, first_tuple)
# print(f"{next_tuple}: {square[next_tuple]}")