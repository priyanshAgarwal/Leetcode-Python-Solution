import pandas as pd
import requests
import hashlib

# Fetch data from your table (assuming it's in a Pandas DataFrame `df`)
# df = pd.read_sql_query(
#     f"SELECT PinID, ImageURL FROM your_table WHERE date = '{your_selected_date}'",
#     your_database_connection
# )

# Calculate hashes
import hashlib

def get_image_hash(image_path):
    """Calculates the SHA-256 hash of an image from its local file path."""

    try:
        with open(image_path, 'rb') as f:
            image_data = f.read()   # Read the entire file contents
            return hashlib.sha256(image_data).hexdigest()
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error reading image file {image_path}: {e}")
        return None  # or raise an exception, depending on your error handling strategy


from PIL import Image
import imagehash

def get_image_has_pil(image_path):
    """Calculates the perceptual hash of an image."""
    try:
        img = Image.open(image_path)
        hash = imagehash.phash(img)
        return hash
    except (FileNotFoundError, PermissionError, OSError) as e:  # Catch more image-related errors
        print(f"Error reading image file {image_path}: {e}")
        return None  


import hashlib

def calculate_hashes(image_path):
    """Calculates aHash, dHash, pHash, and wHash for an image."""
    try:
        img = Image.open(image_path)

        # Calculate Hashes
        ahash = imagehash.average_hash(img)
        dhash = imagehash.dhash(img)
        phash = imagehash.phash(img)
        whash = imagehash.whash(img)

        return {
            'aHash': str(ahash),
            'dHash': str(dhash),
            'pHash': str(phash),
            'wHash': str(whash)
        }
    except (FileNotFoundError, PermissionError, OSError) as e:
        print(f"Error processing file {image_path}: {e}")
        return None

print(calculate_hashes("Leetcode-Python-Solution/Python-Leetcode/Images/pinterest.jpeg"))
print(calculate_hashes("Leetcode-Python-Solution/Python-Leetcode/Images/pinterest-1.0.jpeg"))
print(calculate_hashes("Leetcode-Python-Solution/Python-Leetcode/Images/pinterest-2.0.jpeg"))
print(calculate_hashes("Leetcode-Python-Solution/Python-Leetcode/Images/pinterest-3.0.png"))
print(calculate_hashes("Leetcode-Python-Solution/Python-Leetcode/Images/pinterest-4.0.jpeg"))
print(calculate_hashes("Leetcode-Python-Solution/Python-Leetcode/Images/pinterest-5.0.png"))


# df['ImageHash'] = df['ImageURL'].apply(get_image_hash)
