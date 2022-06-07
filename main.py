import json
import os
import time

def lunch():

    global config

    with open('config.json', 'r') as file:
        config = json.load(file)
        file.close()


def save(ver, var, defi):

    if ver != "":
        config[ver][var] = defi

    with open('config.json', 'w') as file:
        json.dump(config, file, sort_keys=True, indent=4)
        file.close()



if config["0"]["active"] == False:

    lunch()
    save("0", "version", "0.1.0")

    print("Initialisation terminer de Main.py")
else:
    print("cc2")