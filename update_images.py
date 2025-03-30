import os
import json

# Change this to point to the current directory (where your images are located)
image_folder = "."  # Refers to the current folder (MyPosters'Gallery)
images = [f for f in os.listdir(image_folder) if f.endswith(("png", "jpg", "jpeg"))]

with open("images.json", "w") as file:
    json.dump(images, file, indent=4)

print("images.json updated successfully!")
