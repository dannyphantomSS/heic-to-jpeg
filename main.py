from PIL import Image
import pillow_heif
import os

# Register the HEIF plugin
pillow_heif.register_heif_opener()

input_folder = "path_to_heic_folder"
output_folder = "path_to_output_folder"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".heic"):
        heic_path = os.path.join(input_folder, filename)
        jpg_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")
        try:
            with Image.open(heic_path) as img:
                img.save(jpg_path, "JPEG")
            print(f"Converted {filename} to JPEG.")
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")

print("Conversion completed!")
