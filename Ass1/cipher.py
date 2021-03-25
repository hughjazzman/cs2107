from Crypto.Cipher import AES
from binascii import hexlify, unhexlify, b2a_base64, a2b_base64

IV = "helloworldcs2107"

def pad_key(key: str):
    """Pad the key with 0s"""

    # Variables
    length = len(key)
    default_length = 32

    # Check if key exceeds length
    if length > 32:
        raise ValueError("Key value too long")

    # Padding for Cipher
    if length < default_length:
        key += '0' * (default_length - length)

    # Return the padded key
    return key

def create_cipher(key, iv):
    """Create the cipher to decode the text"""
    return AES.new(key.encode(), AES.MODE_CBC, iv.encode())

def encrypt(key: str, iv:str, message: str):
    """Encrypt the text with iv"""
    cipher = create_cipher(key, iv)

    # Cipher text in base64
    return b2a_base64(cipher.encrypt(message.encode())).decode()

def decrypt(key: str, iv:str, cipher_text: str):
    """Decrypt the text with iv"""
    ct = a2b_base64(cipher_text)
    cipher = create_cipher(key, iv)
    return cipher.decrypt(ct).decode()


if __name__ == '__main__':

    with open('flag') as file:
        flag = file.read()

    with open('password') as file:
        key = pad_key(file.read().strip())

    with open('ciphertext', 'w') as file:
        file.write(encrypt(key, IV, flag))

#BJYls89CuTmSw/hivpp/5t66L1k3O1b8p6ugmBh0Ivg=
