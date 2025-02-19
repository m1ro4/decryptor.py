#!/usr/bin/python3
import sys

blocksize = 16
key = 0xadbeefdeadbeefdeadbeef00  #key used for encryption

def decode_chunk(encoded):
    #decodes a 128-bit integer back into a 16-character string
    chunk = ""
    for i in range(15, -1, -1):
        char = (encoded >> (i * 8)) & 0xFF
        chunk += chr(char)
    return chunk

def decrypt_message(encrypted_hex):
    #decrypts the hex-encoded message using XOR and returns plaintext
    iv = 0
    decrypted_text = ""

    #split the hex string into 32-character chunks (each representing 16 bytes)
    chunks = [encrypted_hex[i:i+32] for i in range(0, len(encrypted_hex), 32)]

    for chunk in chunks:
        iv = (iv + 1) % 255
        current_key = key + iv
        encoded = int(chunk, 16)  # Convert hex to integer
        decrypted_chunk = encoded ^ current_key  #reverse XOR
        decrypted_text += decode_chunk(decrypted_chunk)

    return decrypted_text.rstrip('0')  #removes padding

def main():
    #reads encrypted text from a file and decrypts it
    try:
        with open("encrypted.txt", "r", encoding="utf-8") as file: #change textfile name if needed
            encrypted_hex = file.read().strip()
    except FileNotFoundError:
        print("Error: encrypted.txt not found.")
        sys.exit(1)

    decrypted_message = decrypt_message(encrypted_hex)
    print("Decrypted Message:\n", decrypted_message)

if __name__ == "__main__":
    main()
