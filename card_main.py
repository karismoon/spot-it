import os

from card_helpers import card_symbols, make_card, make_page
from library import file_names, bibd

# Define the folder path
folder_path = "/home/user/spot-it/pages"  # Absolute path to desired save location
os.makedirs(folder_path, exist_ok=True)  # Ensure the folder exists

face_location = "/home/user/spot-it/faces" # Absolute path to desired symbols

bibd_with_names = card_symbols(bibd, file_names)

# Make cards and pages following bibd_with_names
idx = 0
while idx < 72:
    cards = []
    for card in bibd_with_names[idx:idx+6]: # Create 6 cards
        new_card = make_card(card, face_location)
        cards.append(new_card)
    new_page = make_page(cards) # Make page with 6 cards
    file_path = os.path.join(folder_path, f"page{idx}.png") # Create save file path
    new_page.save(file_path) # Save page to file path
    idx += 6
    print(f"Page saved to {file_path}")
# Create last card and put on page
new_card = make_card(bibd_with_names[72], face_location)
new_page = make_page([new_card])
file_path = os.path.join(folder_path, f"page{idx}.png")
new_page.save(file_path)
print(f"Page saved to {file_path}")
