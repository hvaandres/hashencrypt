from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def decrypt_aes(key, ciphertext_path):
    key = bytes.fromhex(key)
    with open(ciphertext_path, 'rb') as f_in:
        ciphertext = f_in.read()
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_data


def decrypt_file(ciphertext_path):
    key = "00112233445566778899aabbccddeeff"
    decrypted_data = decrypt_aes(key, ciphertext_path)
    output_path = "plaintext1.txt"
    with open(output_path, 'wb') as f_out:
        f_out.write(decrypted_data)
    print(f"File decrypted successfully and saved as {output_path}")


# Define the path to the ciphertext file
ciphertext_path = "[File_Path]hashencrypt/EncryptedFiles/ciphertext1.bin"

# Decrypt the file
decrypt_file(ciphertext_path)
