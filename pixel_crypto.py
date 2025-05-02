from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    encrypted = Image.new(img.mode, img.size)

    for x in range(img.width):
        for y in range(img.height):
            r, g, b = img.getpixel((x, y))
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            encrypted.putpixel((x, y), (r, g, b))

    encrypted.save(output_path)

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    decrypted = Image.new(img.mode, img.size)

    for x in range(img.width):
        for y in range(img.height):
            r, g, b = img.getpixel((x, y))
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            decrypted.putpixel((x, y), (r, g, b))

    decrypted.save(output_path)
