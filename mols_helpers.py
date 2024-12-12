"""
Helper functions to generate the MOLS.
"""

from library import (
    infinity_points,
    infinity_points_print
)

def print_mols(square, size):
    """
    Given a square, print a human legible output representing the MOLS. 
    
    Args:
        square (dict): Representation of the MOLS
        size (int): Size of the square
    """
    # Print square
    for location in square:
        if isinstance(location, tuple):
            print(f"{square[location]} ", end = "")
            if location[1] == size - 1:
                print()

    print("\n")

    # Print infinity points
    print("Infinity Points")
    for location in square:
        if isinstance(location, str):
            print(f"{location}: {square[location]}")
        if location in infinity_points_print:
            print(f"{infinity_points_print[location]}: {square[location]}")


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

def next_square(dimension, size, current):
    """
    Find the next square along the diagonal for a specific dimension of an MOLS.
    WILL go out of the square.
    
    Args:
        dimension (string or int): Dimension that the diagonal is traveling across, horizontal increment.
        size (int): Size of the MOLS being traveled on.
        current (tuple): Location of symbol that is being traveled away from. 

    Returns: 
        A tuple representing the position of the next symbol in the diagonal.
    """
    if dimension == "horizontal":
        if current[1] < size - 1:
            return (current[0], current[1] + 1)
        return (current[0], 0)

    row = current[0] + 1

    if dimension == "vertical":
        if current[0] < size - 1:
            return (row, current[1])
        return (0, current[1])

    if current[1] < dimension:
        # Overflow, wrap to other side of square
        overflow = dimension - current[1]
        column = size - overflow
        return (row, column)
    
    return (row, current[1] - dimension)

def convert_to_object(square, locations):
    """
    Convert locations into object names.
    
    Args:
        square (dict): Representation of MOLS.
        locations (list): Locations of objects.
        
    Returns:
        A list of the objects.
    """
    objects = []
    for location in locations:
        objects.append(square[location])

    return objects
        
def find_line(start, dimension, size, square):
    """
    Given the starting position of the line, find all the objects in the line.
    
    Args:
        start (tuple): Location of the starting object.
        dimension (string or int): Dimension that the diagonal is traveling across, horizontal increment.
        size (int): Size of the MOLS being traveled on.
        square (dict): Representation of MOLS.

    Returns:
        A list of all the objects in the line. 
    """
    positions = [start]
    
    for count in range(1,size):
        positions.append(next_square(dimension, size, positions[count - 1]))

    objects = []
    for position in positions:
        objects.append(square[position]) 
    objects.append(square[dimension])

    return objects