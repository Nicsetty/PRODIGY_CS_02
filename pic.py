import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageOps

def encrypt_image(image, key):
    """Encrypt the image by adding the key to each pixel value."""
    encrypted_image = Image.new('RGB', image.size)
    pixels = encrypted_image.load()
    original_pixels = image.load()

    for x in range(image.width):
        for y in range(image.height):
            r, g, b = original_pixels[x, y]
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            pixels[x, y] = (r, g, b)
    return encrypted_image

def decrypt_image(image, key):
    """Decrypt the image by subtracting the key from each pixel value."""
    decrypted_image = Image.new('RGB', image.size)
    pixels = decrypted_image.load()
    original_pixels = image.load()

    for x in range(image.width):
        for y in range(image.height):
            r, g, b = original_pixels[x, y]
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            pixels[x, y] = (r, g, b)
    return decrypted_image

def open_image():
    """Open an image file and display it."""
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not file_path:
        return

    global image, original_image
    image = Image.open(file_path)
    original_image = image.copy()

    image_tk = ImageTk.PhotoImage(image)
    image_label.config(image=image_tk)
    image_label.image = image_tk

def save_image(img, title):
    """Save the processed image to a file."""
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")], title=title)
    if file_path:
        img.save(file_path)

def encrypt():
    """Encrypt the image and display it."""
    try:
        key = int(key_entry.get())
        encrypted_img = encrypt_image(original_image, key)
        image_tk = ImageTk.PhotoImage(encrypted_img)
        image_label.config(image=image_tk)
        image_label.image = image_tk
        save_image(encrypted_img, "Save Encrypted Image As")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer for the key.")

def decrypt():
    """Decrypt the image and display it."""
    try:
        key = int(key_entry.get())
        decrypted_img = decrypt_image(image, key)
        image_tk = ImageTk.PhotoImage(decrypted_img)
        image_label.config(image=image_tk)
        image_label.image = image_tk
        save_image(decrypted_img, "Save Decrypted Image As")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer for the key.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Simple Image Encryption Tool")

# Create and place widgets
tk.Button(root, text="Open Image", command=open_image).pack(pady=10)
tk.Label(root, text="Enter Key:").pack(pady=5)
key_entry = tk.Entry(root)
key_entry.pack(pady=5)

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.pack(side=tk.LEFT, padx=20, pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.pack(side=tk.RIGHT, padx=20, pady=10)

image_label = tk.Label(root)
image_label.pack(pady=10)

# Run the application
root.mainloop()
