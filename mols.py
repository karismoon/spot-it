"""
Generate a spot it deck using MOLS.
"""

from library import file_names
from mols_helpers import (
    print_mols,
    index_objects
)

dimension = 8
square = index_objects(file_names)
print_mols(square, dimension)
