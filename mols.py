"""
Generate a spot it deck using MOLS.
"""

from library import file_names
from mols_helpers import (
    print_mols,
    index_objects
)

print_mols(file_names)
square = index_objects(file_names)