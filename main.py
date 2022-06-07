import json
import os
import time

# Importer le dictionaire depui config.json

with open('config.json', 'r') as file:
    config = json.load(file)
    file.close()

# Definire la version du programe

config["0"]["version"] = "0.1.0"

# Enregister le dictionaire dans config.json

with open('config.json', 'w') as file:
    json.dump(config, file, sort_keys=True, indent=4)
    file.close()

if config["0"]["active"] == False:
    print("Initialisation terminer de Main.py")
else:
    print("cc2")