import json
import os
import time

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


if config["0"]["active"] == False:

    lunch("0")
    version = "0.1.0"
    save("0")

    print("Initialisation terminer de Main.py")
else:
    print("cc2")
