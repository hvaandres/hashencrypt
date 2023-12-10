file_path = "/Users/hvaandres/Documents/Git/securehashencrypt/EncryptedFiles/ciphertext1.bin"

try:
    with open(file_path, "rb") as file:
        print("At the moment, this file is encrypted. No data is visible.")
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
# file for testing