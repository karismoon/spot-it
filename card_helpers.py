from PIL import ImageDraw, Image
import math


def draw_hexagon(image, center, radius, fill_color, outline_color):
    """
    Draw a regular hexagon on the given image.

    Args:
        image (PIL.Image.Image): The image on which to draw.
        center (tuple): Coordinates (x, y) for the hexagon's center point.
        radius (int): The distance from the center to a vertex of the hexagon.
        fill_color (str or tuple): Color to fill the hexagon.
        outline_color (str or tuple): Color for the hexagon's outline.
    """
    # Calculate the vertices of the hexagon
    cx, cy = center
    points = []
    for i in range(6):
        # Calculate each vertex's position using trigonometric functions
        angle = 2 * math.pi * i / 6  # Divide the full circle (360°) into 6 equal parts
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        points.append((x, y))

    # Draw the hexagon on the image
    draw = ImageDraw.Draw(image)
    draw.polygon(points, fill=fill_color, outline=outline_color)


def card_symbols(bibd_list, names):
    """
    Function that takes a bibd and peoples' names and creates a spot it deck.
    
    Args:
        bibd_list: This is a list of lists, with each individual lists
    representing a bibd largly populated by 0s with the occasional 1. Each list
    has the same number of 1s.
        names: This is a list with the name of everyone in Discrete in the spot
    it deck.

    Returns:
        A list of lists, where each individual list is a card in our deck and
    has the names of the people going on that card.
    """

    result = []
    for i in bibd_list:
        temp = []
        for j in i:
            temp.append(names[j])
        result.append(temp)
    return result


def make_card(faces, path):
    """
    Function to create a card.

    Args:
        faces: A list with 9 string elements representing the names of faces to use
        path: A string representing absolute path to desired faces.
    
    Return:
        A PIL canvas with final created card
    """
    WIDTH = 1200
    HEIGHT = 1200

    face_paths = {idx: path for idx, face in enumerate(faces)} # Create dictionary for faces

    loaded_faces = {idx: Image.open(path) for idx, path in face_paths.items()} # Load images

    # Manipulate face img
    new_size = (200,200)
    scaled_faces = {idx: face.resize(new_size) for idx, face in loaded_faces.items()}

    rotation_angles = [180, 60, 300, 135, 195, 270, 90, 330, 45]
    rotated_faces = {idx: face.rotate(rotation_angles[idx]) for idx, face in scaled_faces.items()}

    # Create a blank canvas
    card = Image.new("RGBA", (WIDTH, HEIGHT), (255,255,255,255))  # White background
    draw_hexagon(card, (WIDTH/2, HEIGHT/2), 500, (255,255,255,255), (0,0,0,1)) # Add hexagon shape to card

    FACE_WIDTH = rotated_faces[0].width
    FACE_HEIGHT = rotated_faces[0].height

    # Paste images onto the card
    card.paste(rotated_faces[0], (int(WIDTH/2-FACE_WIDTH/2), int(HEIGHT/2-FACE_HEIGHT)), rotated_faces[0])
    card.paste(rotated_faces[1], (int(WIDTH*2/3-FACE_WIDTH/2-80), int(HEIGHT/2-20)), rotated_faces[1])
    card.paste(rotated_faces[2], (int(WIDTH/3-FACE_WIDTH/2+80), int(HEIGHT/2-20)), rotated_faces[2])
    card.paste(rotated_faces[3], (int(WIDTH*2/3-FACE_WIDTH/2), int(HEIGHT/2-2*FACE_HEIGHT)), rotated_faces[3])
    card.paste(rotated_faces[4], (int(WIDTH/3-FACE_WIDTH/2), int(HEIGHT/2-2*FACE_HEIGHT)), rotated_faces[4])
    card.paste(rotated_faces[5], (int(WIDTH/3-FACE_WIDTH*1.25), int(HEIGHT/2-FACE_HEIGHT/2)), rotated_faces[5])
    card.paste(rotated_faces[6], (int(WIDTH*2/3+FACE_WIDTH*.25), int(HEIGHT/2-FACE_HEIGHT/2)), rotated_faces[6])
    card.paste(rotated_faces[7], (int(WIDTH/3-FACE_WIDTH/2), int(HEIGHT/2+FACE_HEIGHT)), rotated_faces[7])
    card.paste(rotated_faces[8], (int(WIDTH*2/3-FACE_WIDTH/2), int(HEIGHT/2+FACE_HEIGHT)), rotated_faces[8])

    return card

def make_page(cards):
    """
    Combine 4 cards onto an 8.5x11 inch page for printing.

    Args:
        cards: A list of PIL Image objects representing the cards.

    Returns:
        A PIL Image canvas with cards arranged on a page.
    """
    # Standard page size in pixels (8.5x11 inches at 300 DPI)
    width = 2550
    height = 3300

    # Create a blank page with a black background
    page = Image.new("RGBA", (width, height), (0, 0, 0, 255))

    # Position and paste cards on the page
    positions = [
        (0,0),
        (1200, 0),
        (0,1100),
        (1200,1100),
        (0, 2200),
        (1200,2200)
    ]

    # Paste card on page
    for card, pos in zip(cards, positions):
        page.paste(card, pos, card)

    return page
