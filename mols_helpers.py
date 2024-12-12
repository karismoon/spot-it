"""
Helper functions to generate the MOLS.
"""

from library import infinity_points

def print_mols(file_names):
    """
    Given a list of symbols, print a human legible output representing the MOLS. 
    
    Args:
        file_names (list): Names of the symbols
    """
    # Print square
    for index in range(9, len(file_names)):
        if index % 8 != 0:
            print(f"{file_names[index]} ", end = "")
        else:
            print(f"{file_names[index]} ")

    print("\n")

    # Print infinity points
    print("Infinity Points")
    for index in range(9):
        print(f"{infinity_points[index]}: {file_names[index]}")

def index_objects(file_names):
    """
    Given a list of objects, assign each of them to a position in an 8x8 MOLS.
    Position is formatted (row, column).

    Args:
        file_names (list): Names of the symbols.

    Returns: 
        A dict representing all of the symbols mapped to their locations in the MOLS including infinity points.
    """
    square = {}

    # Assign infinity points
    for index in range(9):
        square[infinity_points[index]] = file_names[index]

    list_counter = 9

    # Assign rest of symbols to square
    for row in range(8):
        for column in range(8):
            square[(row, column)] = file_names[list_counter]
            list_counter += 1

    return square

def next_square(dimension, square, current):
    """
    Find the next square along the diagonal for a specific dimension of an MOLS.
    
    Args:
        dimension (string or int): Dimension that the diagonal is traveling across, horizontal increment.
        square (int): Size of the MOLS being traveled on.
        current (tuple): Location of symbol that is being traveled away from. 

    Returns: 
        A tuple representing the position of the next symbol in the diagonal.
    """
    if dimension == "horizontal":
        return (current[0], current[1] + 1)

    row = current[0] + 1

    if dimension == "vertical":
        return (row, current[1])

    if current[1] < dimension:
        # Overflow, wrap to other side of square
        overflow = dimension - current[1]
        column = square - overflow
        return (row, column)
    
    return (row, current[1] - dimension)