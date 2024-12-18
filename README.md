# spot-it
Our goal was to create a Spot-it! card deck that has 73 cards, 9 symbols per card, and 1 matching symbol between any pair of cards. The symbols we used in our deck were the faces of people and in our code we refer to those as "face(s)". This code follows strict requirements to run, see Set Up.

# Set up
1. We first made a normalized set of square face images (PNG format) and kept them in a folder. Note file path.
2. In `library.py`, we made a variable called `file_names` which contained a list of the names of every face image.

# Dependencies
Pillow: [https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.rotate](https://pillow.readthedocs.io/en/stable/installation/basic-installation.html)
* Purpose is to visualize cards.
