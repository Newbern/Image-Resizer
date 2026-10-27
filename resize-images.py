from PIL import Image
from tkinter import Tk, filedialog
from datetime import datetime
import os

# Hide tkinter window
root = Tk()
root.withdraw()

# Select source folder
input_folder = filedialog.askdirectory(title="Select Folder Containing Images")

if not input_folder:
    print("No folder selected.")
    root.destroy()
    quit()

# Output folder next to script
script_dir = os.path.dirname(os.path.abspath(__file__))
output_root = os.path.join(script_dir, "resized_output")

# Create date/time subfolder
date_folder = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_folder = os.path.join(output_root, date_folder)

os.makedirs(output_folder, exist_ok=True)

# Resize settings
max_width = 800

# Supported image formats
extensions = (".png", ".jpg", ".jpeg", ".bmp", ".webp", ".gif", ".tiff")

count = 0

for filename in os.listdir(input_folder):
    if filename.lower().endswith(extensions):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            with Image.open(input_path) as img:

                # Skip resizing images already smaller than target width
                if img.width <= max_width:
                    img.save(output_path)
                    print(f"Copied: {filename}")
                else:
                    # Preserve aspect ratio
                    ratio = max_width / img.width
                    new_height = int(img.height * ratio)

                    resized = img.resize(
                        (max_width, new_height),
                        Image.Resampling.LANCZOS
                    )

                    resized.save(output_path)
                    print(f"Resized: {filename}")

                count += 1

        except Exception as e:
            print(f"Failed: {filename} - {e}")

root.destroy()

print(f"\nFinished! {count} images processed.")
print(f"Saved to:\n{output_folder}")

input("\nPress Enter to exit...")
