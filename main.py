from dotenv import load_dotenv
import os
from Crypto.Hash import SHA256
from Crypto.Cipher import AES













load_dotenv(dotenv_path="config")
namefile = os.getenv("namefile")



hashin = input('test: ')
hashrd = bytes(hashin, 'utf-8')

hash_object = SHA256.new()
hash_object.update(hashrd)

hashout = hash_object.digest()
key = hashout

file_in = open(namefile, "rb")
nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)

print(data)

