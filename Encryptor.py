from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

salt = b'0\x01p^\xb4\xf3Z\x07\xf0\xc5\xbb8\n\xc6\xd08'
password = "mypassword"
key = PBKDF2(password, salt, dkLen=32)

def encrypt(message):
    message = bytes(message, 'utf-8')
    cipher = AES.new(key, AES.MODE_CBC)
    ciphered_data = cipher.encrypt(pad(message, AES.block_size))
    with open("iv.txt", "wb") as f:
        f.write(cipher.iv)
    return ciphered_data

def decrypt(ciphered_data):
    with open("iv.txt", "rb") as f:
        iv = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(ciphered_data), AES.block_size)
    return decrypted_data

