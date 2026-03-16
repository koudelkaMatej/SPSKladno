import os
from PIL import Image

TARGET_HEIGHT = 410
FOLDERS = [
    r"C:\Programovani_Koudelka\SPSKladno\PyGame\Fire And Water_IT3\Assets\ohen a voda\boy_right",
    r"C:\Programovani_Koudelka\SPSKladno\PyGame\Fire And Water_IT3\Assets\ohen a voda\boy_still"
]

def normalize_image_height(image_path):
    img = Image.open(image_path)
    width, height = img.size

    # Resize image to target height, keep aspect ratio
    new_width = int(width * TARGET_HEIGHT / height)
    img_resized = img.resize((new_width, TARGET_HEIGHT), Image.LANCZOS)

    # Create new image with target height and original width, centered
    canvas = Image.new("RGBA", (new_width, TARGET_HEIGHT), (0, 0, 0, 0))
    canvas.paste(img_resized, (0, 0))

    # If you want to center horizontally in a fixed width, set FIXED_WIDTH here
    # FIXED_WIDTH = max_width_of_all_images
    # left = (FIXED_WIDTH - new_width) // 2
    # canvas = Image.new("RGBA", (FIXED_WIDTH, TARGET_HEIGHT), (0, 0, 0, 0))
    # canvas.paste(img_resized, (left, 0))

    canvas.save(image_path)

for folder in FOLDERS:
    for filename in os.listdir(folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder, filename)
            normalize_image_height(image_path)