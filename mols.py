import random

from pic_library import (
    file_names,
    infinity_points,
)

for index in range(9, len(file_names)):
    if index % 8 != 0:
        print(f"{file_names[index]} ", end = "")
    else:
        print(f"{file_names[index]} ")

print("\n")

print("Infinity Points")
for index in range(9):
    print(f"{infinity_points[index]}: {file_names[index]}")