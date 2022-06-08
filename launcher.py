import json
import threading

import requests as req
import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

global config
global active
global key
global name
global name_link
global version
global version_file
global version_link


def lunch(fid):
    global config

    global active
    global key
    global name
    global name_link
    global version
    global version_file
    global version_link

    with open('config.json', 'r') as file:
        config = json.load(file)
        file.close()

    active = config[fid]["active"]
    key = config[fid]["key"]
    name = config[fid]["name"]
    name_link = config[fid]["name_link"]
    version = config[fid]["version"]
    version_file = config[fid]["version_file"]
    version_link = config[fid]["version_link"]


def save(fid):
    global config

    global active
    global key
    global name
    global name_link
    global version
    global version_file
    global version_link

    with open('config.json', 'w') as file:
        json.dump(config, file, sort_keys=True, indent=4)
        file.close()

    config[fid]["active"] = active
    config[fid]["key"] = key
    config[fid]["name"] = name
    config[fid]["name_link"] = name_link
    config[fid]["version"] = version
    config[fid]["version_file"] = version_file
    config[fid]["version_link"] = version_link


def config_cheker():
    if not os.path.exists("config.json"):
        print("Warnig, config.json na pas etais trouver, des bug peuves aparaitre")

        try:
            file = req.get("https://raw.githubusercontent.com/Simaire/pylauncher/main/config.json",
                           allow_redirects=True)
            open("config.json", 'wb').write(file.content)


        except:
            print("Error, Erreur de connection !")
            quit()
    else:
        print("Config ok")


def update():
    global name
    global name_link

    if os.path.exists(name):
        os.remove(name)

    try:
        file = req.get(name_link, allow_redirects=True)
        open(name, 'wb').write(file.content)


    except:
        print("Error, Erreur de connection !")

    if not os.path.exists(name):
        print("Error, Une erreur est survenu lors du tellechargement de " + name)

    else:
        print("Tellechargement de " + name + " reusit !")


def initialisation(fid):
    global active
    global name

    lunch(fid)
    active = False
    save(fid)

    if os.path.exists(name):
        exec(open(name).read())

    if not os.path.exists(name):
        update(fid)


def tellechargement_version():
    global version_link
    global version_file

    if not os.path.exists('versions/'):
        os.mkdir('versions')

    if os.path.exists('versions/' + version_file):
        os.remove('versions/' + version_file)

    try:
        file = req.get(version_link, allow_redirects=True)
        open('versions/' + version_file, 'wb').write(file.content)

    except:
        print("Error, Erreur de connection !")

    if not os.path.exists("versions/" + version_file):
        print("Error, Une erreur est survenu lors du tellechargement de " + version_file)

    else:
        print("Tellechargement de " + version_file + " reusit !")


def verification():
    global version
    global version_file
    global key
    global name
    global ajour

    if os.path.exists("versions/" + version_file):

        try:
            hashin = key
            hashrd = bytes(hashin, 'utf-8')

            hash_object = SHA256.new()
            hash_object.update(hashrd)
            key2 = hash_object.digest()

            file_in = open('versions/' + version_file, "rb")
            nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]
            cipher = AES.new(key2, AES.MODE_EAX, nonce)
            data = cipher.decrypt_and_verify(ciphertext, tag)

            bversion = bytes(version, 'utf-8')

            if data == bversion:
                print("Le logiciel " + name + " est â jour !")
                ajour = True

            else:
                print("Le logiciel " + name + " n'est pas â jour !")
                ajour = False

        except:
            print("Error, Erreur lors du dechiffrement de " + version_file)

    else:
        print("Error, Le fichier " + version_file + " est introuvable !")


config_cheker()
lunch("0")
initialisation("0")
tellechargement_version()
# verification("0")

# if ajour == False:
#    update("0")
#    verification("0")

# if ajour == False:
#    print("Error, erreur lors de la mis a jour")

# if ajour == True:

lunch("0")
active = True
save("0")
exec(open(name).read())
