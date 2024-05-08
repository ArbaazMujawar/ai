from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random

random_generator = Random.new().read
key = RSA.generate(2048, random_generator)
public_key = key.publickey()
private_key = key

print("Public key:")
print(public_key.export_key().decode())
print("Private key:")
print(private_key.export_key().decode())

message = input("Enter the Text: ").encode()
cipher = PKCS1_OAEP.new(public_key)
ciphertext = cipher.encrypt(message)
print("Ciphertext:", ciphertext.hex())

# Decrypt the message using the private key
cipher = PKCS1_OAEP.new(private_key)
decrypted_message = cipher.decrypt(ciphertext)
print("Decrypted message:", decrypted_message.decode())
