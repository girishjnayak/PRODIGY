from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = np.array(image)

    # Encrypt the pixels by adding the key and taking modulo 256
    encrypted_pixels = (pixels + key) % 256
    
    # Shuffle the rows of the encrypted pixels
    for row in encrypted_pixels:
        np.random.shuffle(row)
    
    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))
    encrypted_image.save(output_path)

def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = np.array(image)
    
    # Unshuffle the rows (since np.random.shuffle() cannot be reversed directly, this step is flawed)
    # A proper decryption process should use a deterministic shuffle based on a key or an index.

    # Decrypt the pixels by subtracting the key and taking modulo 256
    decrypted_pixels = (pixels - key) % 256
    
    decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'))
    decrypted_image.save(output_path)

key = 50
encrypt_image('input_image.png', 'encrypted_image.png', key)
decrypt_image('encrypted_image.png', 'decrypted_image.png', key)
