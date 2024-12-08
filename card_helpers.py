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
