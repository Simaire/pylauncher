from tkinter import *
import os
from Crypto.Cipher import AES
from dotenv import load_dotenv
from Crypto.Hash import SHA256


acces = False
n = 0
tenta = 0

def verife():
    try:
        load_dotenv(dotenv_path="config")
        verif = os.getenv("verif")
        print("variable ok")

        key = b'\x0bV\xd0\xf0\x1e\xbb\xbe\xb1]z\xcd\xb1(\xf6#:\x1c\x0b\x85\xcdTI\x1cP\x9dp\xcbS\xee\xfe\x84)'
        file_in = open(verif, "rb")
        nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]
        cipher = AES.new(key, AES.MODE_EAX, nonce)
        data = cipher.decrypt_and_verify(ciphertext, tag)

        print(data)
        print("Fichier dechifrer")



    except:
        print("error")
        quit()

    if data != b'ok':
        print("data error")
        quit()


verife()

if os.path.exists("lock.bin"):
    os.remove("lock.bin")
else:
    quit()


def fenetre(n = 0):
    global wid
    global wpsd

    if n == 0:
        window = Tk()

        window.title("[PyLauncher] Login")
        window.geometry("600x600")
        window.minsize(600, 600)
        window.maxsize(600, 600)
        window.iconbitmap("asset/login.ico")
        window.config(background='#C8F5FF')

        wid = Entry(window)
        wpsd = Entry(window)

        wid.grid(row=10, column=10)
        wpsd.grid(row=12, column=10)


        window.mainloop()


def idverif(id, pasword):
    global tenta
    global acces

    try:
        print(id)
        print(pasword)

        hashin = pasword
        hashrd = bytes(hashin, 'utf-8')

        hash_object = SHA256.new()
        hash_object.update(hashrd)

        hashout = hash_object.digest()

        load_dotenv(dotenv_path="user")
        psd = os.getenv(id)



    except:
        print("error")

    if str(hashout) == str(psd):
        print("ok")
        acces = True
    else:
        print("acces deny")
        acces = False
        tenta = tenta + 1


fenetre(0)
idverif(wid, wpsd)

if acces == True:
    n = 1


while tenta <= 3 and acces == False:
    print(tenta)
    if acces == False and tenta <= 3:
        idverif(input("id: "), input("pas: "))


if acces == False and tenta > 3:
    quit()

print("ok")
