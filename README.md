# hashencrypt
This program is used to encrypt and decrypt files using the SHA256 algorithm. It is written in Python 3.6.4 and uses the hashlib library.

## Prerequisites:
- Python 3.6.4
- hashlib library
- pycrypto library

## Usage
- We can try to display the info from the Encrypted values by running the file "displayInfo.py" You have to keep in mind that the data will not display because is encrypted.

- We can get the MD5 by running the decrypt file "decrypt_MD5_Hash.py" We only need to enter the file paths:

```
ciphertext_path = '[file_path]'
public_key_path = '[file_path]'
decrypted_path = '[file_path]'
```

- We can get the values by using the file "decrypt_Values.py" We only need to enter the Algortihm and the Key. These values are the following:

```
Algorithm: aes-128-ecb
Key: 00112233445566778899aabbccddeeff
```

## Results
- The results of the MD5 Hash are the following:

```
baa3ae2935a244f268e1fd5da6f157d2
```

- The results of the Values are the following:

```
You did it. Well Done !
```

## Author
- **Alan Haro** - *Blog* - [Alan Haro](https://medium.com/@ithvaandres)

