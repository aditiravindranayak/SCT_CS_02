!pip install Pillow

from PIL import Image
import numpy as np
from google.colab import files

def encrypt_image(image_path, output_path, key):
    # Open the image
    img = Image.open(image_path)
    img = img.convert("RGB")  # Ensure image is in RGB mode
    pixels = np.array(img)

    # Apply encryption: Swap and modify pixel values
    encrypted_pixels = (pixels + key) % 256  # Basic mathematical operation
    encrypted_img = Image.fromarray(encrypted_pixels.astype('uint8'), 'RGB')

    # Save the encrypted image
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    # Open the encrypted image
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = np.array(img)

    # Apply decryption: Reverse the operation
    decrypted_pixels = (pixels - key) % 256
    decrypted_img = Image.fromarray(decrypted_pixels.astype('uint8'), 'RGB')

    # Save the decrypted image
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

# Upload the image file
uploaded = files.upload()

# Save the file name
image_path = list(uploaded.keys())[0]

# Define output paths
encrypted_path = "encrypted_image.png"
decrypted_path = "decrypted_image.png"
key = int(input("Enter an encryption key (integer value): "))

# Encrypt the image
encrypt_image(image_path, encrypted_path, key)

# Decrypt the image
decrypt_image(encrypted_path, decrypted_path, key)

# Download the encrypted and decrypted images
files.download(encrypted_path)
files.download(decrypted_path)

from google.colab import drive
drive.mount('/content/drive')
