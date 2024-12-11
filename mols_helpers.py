"""
Helper functions to generate the MOLS.
"""

from pic_library import infinity_points

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
        dimension (string or int): Dimension that the diagonal is traveling across.
        square (dict): Representation of the MOLS being traveled on.
        current (string): Name of symbol that is being traveled away from. 

    Returns: 
        A string representing the next symbol in the diagonal.
    """
    if dimension == "horizontal":
        next_location = (square[current](0, square[current](1) + 1)
        
    if square[current](1) < dimension:
        # Overflow, wrap to other side of square
        