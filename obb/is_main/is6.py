import hashlib

message = input("Enter the Text: ").encode('utf-8')
md5 = hashlib.md5()
md5.update(message)
digest = md5.digest()
hex_digest = digest.hex()

print("Message:", message.decode('utf-8'))
print("MD5 Digest:", hex_digest)
