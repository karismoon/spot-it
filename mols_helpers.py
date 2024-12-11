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
    for index in range(9, len(file_names)):
        if index % 8 != 0:
            print(f"{file_names[index]} ", end = "")
        else:
            print(f"{file_names[index]} ")

    print("\n")

    print("Infinity Points")
    for index in range(9):
        print(f"{infinity_points[index]}: {file_names[index]}")

def index_objects(file_names):
    """
    Given a list of objects, assign each of them to a position in an 8x8 MOLS.
    
    Args:
        file_names (list): Names of the symbols.

    Returns: 
        square (dict): All of the symbols mapped to their locations in the MOLS.
    """
    square = {}

    for index in range(9):
        infinity_points[index] = square[file_names(index)]