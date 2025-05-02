import tkinter as tk
from tkinter import filedialog, messagebox
from pixel_crypto import encrypt_image, decrypt_image
import os

def browse_file():
    file_path.set(filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")]))

def browse_output():
    output_path.set(filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")]))

def encrypt():
    try:
        key_val = int(key.get())
        encrypt_image(file_path.get(), output_path.get(), key_val)
        messagebox.showinfo("Success", "Image encrypted successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decrypt():
    try:
        key_val = int(key.get())
        decrypt_image(file_path.get(), output_path.get(), key_val)
        messagebox.showinfo("Success", "Image decrypted successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Pixel Image Encryption Tool")
root.geometry("450x250")
root.resizable(False, False)

file_path = tk.StringVar()
output_path = tk.StringVar()
key = tk.StringVar()

tk.Label(root, text="Select Image:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
tk.Entry(root, textvariable=file_path, width=40).grid(row=0, column=1)
tk.Button(root, text="Browse", command=browse_file).grid(row=0, column=2)

tk.Label(root, text="Save As:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
tk.Entry(root, textvariable=output_path, width=40).grid(row=1, column=1)
tk.Button(root, text="Browse", command=browse_output).grid(row=1, column=2)

tk.Label(root, text="Encryption Key:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
tk.Entry(root, textvariable=key).grid(row=2, column=1)

tk.Button(root, text="Encrypt", width=15, bg="lightblue", command=encrypt).grid(row=3, column=1, pady=10, sticky="w")
tk.Button(root, text="Decrypt", width=15, bg="lightgreen", command=decrypt).grid(row=3, column=1, pady=10, sticky="e")

root.mainloop()
