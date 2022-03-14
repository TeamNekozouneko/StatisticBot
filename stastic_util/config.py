import json

defaultConfig = {
    "token": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",

    "srvId": "000000000000000"
}

loadedConfig = None

def reloadConfig():
    return loadConfig()

def loadConfig():
    with open("config.json", "r") as conf:
        loadedConfig = json.load(conf)
    return loadedConfig

def saveDefaultConfig():
    with open("config.json", "w") as conf:
        json.dump(defaultConfig, conf)
    return