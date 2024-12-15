import os

from card_helpers import make_card, make_page
from library import file_names, bibd

# Define the folder path
folder_path = "/home/laurel/github.com/coxlaurel/spot-it/pages"  # Absolute path
os.makedirs(folder_path, exist_ok=True)  # Ensure the folder exists

# one_faces = ["amere", "kdae", "gan", "cayus", "tdani", "cmalv", "fdext", "peddy", "pisha"]

# card_one = make_card(one_faces)

# # Save the final canvas
# file_path = os.path.join(folder_path, "card_three.png")
# card_one.save(file_path)

# print(f"Image saved to {file_path}")

# page_cards = [card_one, card_one, card_one, card_one, card_one, card_one]
# new_page = make_page(page_cards)

# file_path = os.path.join(folder_path, "newpage.png")
# new_page.save(file_path)

idx = 0
while idx < len(bibd):
    card = 0 + idx
    cards = []
    while card < (6 + idx):
        faces = []
        for face in bibd[card]:
            faces.append(file_names[face])
        new_card = make_card(faces)
        cards.append(new_card)
        card += 1
    new_page = make_page(cards)
    file_path = os.path.join(folder_path, f"page{idx}.png")
    new_page.save(file_path)
    idx += 6

print(f"Page saved to {file_path}")
