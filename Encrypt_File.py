from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def encrypt_file(plaintext_path, public_key_path, ciphertext_path):
   # Load the public key
   with open(public_key_path, 'rb') as f:
       public_key = RSA.importKey(f.read())

   # Load the plaintext file
   with open(plaintext_path, 'rb') as f:
       plaintext_data = f.read()

   # Encrypt the plaintext using PKCS1_OAEP padding
   cipher = PKCS1_OAEP.new(public_key)
   encrypted_data = cipher.encrypt(plaintext_data)

   # Save the encrypted data to a file
   with open(ciphertext_path, 'wb') as f:
       f.write(encrypted_data)

   print(f"File encrypted successfully and saved as {ciphertext_path}")


# Define the paths
plaintext_path = "[File_Path]hashencrypt/DecryptedFiles/plaintext1.txt"
public_key_path = "[File_Path]hashencrypt/PublicKey/public.pem"
ciphertext_path = "[File_Path]hashencrypt/EncryptedFiles/ciphertext2.bin"

# Encrypt the file
encrypt_file(plaintext_path, public_key_path, ciphertext_path)
