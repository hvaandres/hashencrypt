from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import hashlib

def compute_md5(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
        return hashlib.md5(data).hexdigest()

def decrypt_file(ciphertext_path, public_key_path, decrypted_path):
    # Load public key
    with open(public_key_path, 'rb') as public_key_file:
        public_key = RSA.import_key(public_key_file.read())

    # Compute MD5 hash of the encrypted file
    md5_hash = compute_md5(ciphertext_path)
    print("MD5 Hash:", md5_hash)

    # Decrypt the file
    try:
        with open(ciphertext_path, 'rb') as cipher_file:
            ciphertext = cipher_file.read()
            cipher = PKCS1_OAEP.new(public_key)
            decrypted_data = cipher.decrypt(ciphertext)
            
        # Save the decrypted data
        with open(decrypted_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)

        print("File decrypted successfully.")
    except FileNotFoundError:
        print(f"The file '{ciphertext_path}' could not be found.")
    except ValueError:
        print("Error: Ciphertext with incorrect length.")
    except Exception as e:
        print("An error occurred during decryption:", str(e))

# Paths
ciphertext_path = '[file_path]EncryptedFiles/ciphertext1.bin'
public_key_path = '[file_path]PublicKey/public.pem'
decrypted_path = '[file_path]DecryptedFiles/decrypted.txt'

# Decrypt the file
decrypt_file(ciphertext_path, public_key_path, decrypted_path)
# file and test