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
    # For each infinity point (each dimension)
    infinity_points_card.append(square[infinity_point]) # Add the infinity point to the card with just infinity points
    # mols_cards.append(f"infinity point: {infinity_point}")
    if infinity_point == "horizontal":
        # For the horizontal cards
        for start_row in range(size):
            # Add each card to the list
            mols_cards.append(find_line((start_row, 0), infinity_point, size, square))
    else:
        # For all non-horizontal cards
        for start_column in range(size):
            # For every possible column to start at
            mols_cards.append(find_line((0, start_column), infinity_point, size, square))

mols_cards.append(infinity_points_card)

for card in mols_cards:
    print(card)