from PIL import ImageDraw
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
    """
    result = []
    # loop through every list in the BIBD
    for i in bibd_list:
        temp1 = 0
        temp2 = []
        # loop through every item in each BIBD list
        for j in i:
            if j == 1:
                temp2.append(names[temp1])
            temp1 =+ 1
        result.append(temp1)
    return result
    """
