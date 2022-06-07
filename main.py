import json
import os
import time

def lunch(id):

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

    active = config[id]["active"]
    key = config[id]["key"]
    name = config[id]["name"]
    name_link = config[id]["name_link"]
    version = config[id]["version"]
    version_file = config[id]["version_file"]
    version_link = config[id]["version_link"]

def save(id):

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

    config[id]["active"] =active
    config[id]["key"] = key
    config[id]["name"] = name
    config[id]["name_link"] = name_link
    config[id]["version"] = version
    config[id]["version_file"] = version_file
    config[id]["version_link"] = version_link



if config["0"]["active"] == False:


    lunch("0")
    version = "0.1.0"
    save("0")

    print("Initialisation terminer de Main.py")
else:
    print("cc2")