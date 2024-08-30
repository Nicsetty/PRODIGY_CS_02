# Simple Pixel Manipulation for Image creation

This is a simple GUI-based image encryption and decryption tool built with Python. The tool uses basic pixel manipulation techniques to encrypt and decrypt images. Users can load an image, apply a simple encryption by altering the pixel values, and then save the encrypted image. Decryption is also supported by reversing the pixel manipulation process.

## Features

- **Encrypt Images**: Modify the pixel values of an image using a user-defined key.
- **Decrypt Images**: Reverse the encryption process to restore the original image.
- **GUI Interface**: A simple and intuitive graphical user interface built with Tkinter.

## Requirements

- Python 3.x
- `Pillow` library for image processing

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/simple-image-encryption-tool.git
    cd simple-image-encryption-tool
    ```

2. Install the required dependencies:
    ```bash
    pip install pillow
    ```

## Usage

1. Run the tool:
    ```bash
    python image_encryption_tool.py
    ```

2. **Open an Image**:
   - Click the "Open Image" button and select the image file you want to encrypt or decrypt.

3. **Enter a Key**:
   - Enter an integer value in the "Enter Key" field. This key will be used for both encryption and decryption.

4. **Encrypt**:
   - Click the "Encrypt" button to encrypt the image. The encrypted image will be displayed in the GUI.
   - You can save the encrypted image by following the file dialog prompt.

5. **Decrypt**:
   - Click the "Decrypt" button to decrypt the image using the same key you used for encryption.
   - The decrypted image will be displayed, and you can save it using the file dialog prompt.

## Example

Here’s a quick example of how the tool works:

- **Original Image**: Load an image from your system.
- **Encrypted Image**: Encrypt the image with a key (e.g., 42).
- **Decrypted Image**: Decrypt the image with the same key (e.g., 42) to get back the original image.

## Screenshots

(Add screenshots of the tool in action here)

## Contributing

If you want to contribute to this project, feel free to fork the repository and submit a pull request. 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
