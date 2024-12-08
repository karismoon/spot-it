from PIL import Image
import os

from helper import draw_hexagon

WIDTH = 3024
HEIGHT = 3024

# Define the folder path
folder_path = "/home/laurel/github.com/coxlaurel/spot-it/cards"  # Absolute path
os.makedirs(folder_path, exist_ok=True)  # Ensure the folder exists

faces = ["kdaey", "gan", "caush"]

face_paths = {idx: f"faces/{face}.png" for idx, face in enumerate(faces)}

loaded_faces = {idx: Image.open(path) for idx, path in face_paths.items()}

# Manipulate face img
new_size = (1000,1000)
scaled_faces = {idx: face.resize(new_size) for idx, face in loaded_faces.items()}

rotation_angles = [180, 60, 300]
rotated_faces = {idx: face.rotate(rotation_angles[idx]) for idx, face in scaled_faces.items()}

# Create a blank canvas
canvas = Image.new("RGBA", (WIDTH, HEIGHT), (255,255,255,255))  # White background
draw_hexagon(canvas, (WIDTH/2, HEIGHT/2), 1400, (255,255,255,255), (0,0,0,1))

FACE_WIDTH = rotated_faces[0].width
FACE_HEIGHT = rotated_faces[0].height

# Paste images onto the canvas
canvas.paste(rotated_faces[0], (int(WIDTH/2-FACE_WIDTH/2), int(HEIGHT/2-FACE_HEIGHT)), rotated_faces[0])  # (img, location (x,y), order)
canvas.paste(rotated_faces[1], (int(WIDTH*2/3-FACE_WIDTH/2), int(HEIGHT/2-200)), rotated_faces[1])
canvas.paste(rotated_faces[2], (int(WIDTH/3-FACE_WIDTH/2), int(HEIGHT/2-200)), rotated_faces[2])

# Save the final canvas
file_path = os.path.join(folder_path, "refactor_test.png")
canvas.save(file_path)

print(f"Image saved to {file_path}")