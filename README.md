# Image Encryption Tool

This repository contains a simple image encryption tool using pixel manipulation. The tool supports operations like swapping pixel values or applying a basic mathematical operation to each pixel.

## Features

- **Encrypt Image:** Encrypts an image by applying a mathematical operation to each pixel value.
- **Decrypt Image:** Decrypts the image by reversing the applied mathematical operation.
- **Supports RGB Images:** Ensures that the images are in RGB format for processing.
- **Handles Non-Image Files Gracefully:** Ignores non-image files during upload.

## Usage

### Prerequisites

- Python 3.x
- Pillow library

### Installation

1. **Install Pillow:**

    ```bash
    pip install Pillow
    ```

2. **Run the Script:**

    Use the provided script to upload an image, encrypt it, and then decrypt it.

### Instructions

1. **Upload the Image:**

    Use the `files.upload()` function from the `google.colab` module to upload an image file.

2. **Run the Script:**


3. **Download Encrypted and Decrypted Images:**

    The encrypted and decrypted images will be available for download after the script runs.

### Example

- **Encrypting Image:**
  - **Image Path:** `input_image.jpg`
  - **Encrypted Path:** `encrypted_image.png`
  - **Decrypted Path:** `decrypted_image.png`
  - **Key:** `50`

