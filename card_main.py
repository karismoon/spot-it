import os

from card_helpers import make_card

# Define the folder path
folder_path = "/home/laurel/github.com/coxlaurel/spot-it/cards"  # Absolute path
os.makedirs(folder_path, exist_ok=True)  # Ensure the folder exists

one_faces = ["amere", "kdaey", "gan", "cayus", "tdani", "cmalv", "fdext", "peddy", "pisha"]

card_one = make_card(one_faces)

# Save the final canvas
file_path = os.path.join(folder_path, "card_two.png")
card_one.save(file_path)

print(f"Image saved to {file_path}")