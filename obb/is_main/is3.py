#Run pip install pycryptodome to install necessary packages
#This implementation uses continuous block cipher
from Crypto.Cipher import DES 
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt(plaintext, key):
    init = get_random_bytes(DES.block_size)#For CBC mode generates init combination
    cipher = DES.new(key, DES.MODE_CBC, init)
    ciphertext = cipher.encrypt(plaintext)
    return init + ciphertext #adds initial combination to 

def decrypt(ciphertext, key):
    init = ciphertext[:DES.block_size]#gets initial combination to reverse
    cipher = DES.new(key, DES.MODE_CBC, init)
    plaintext = cipher.decrypt(ciphertext[DES.block_size:])
    return plaintext

key = b'aaaaaaaa'#string length should be 8
plaintext = b'hello world'
ciphertext = encrypt(pad(plaintext,16), key)
print("Encrypted:", ciphertext)
decrypted = unpad(decrypt(ciphertext, key),16)
print("Decrypted:", decrypted)
