import json

class config:
    

    defaultConfig = {
        "token": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",

        "srvId": "000000000000000"
    }

    loadedConfig = None

    @classmethod
    def reloadConfig(self):
        return self.loadConfig()

    @classmethod
    def loadConfig(self) -> dict:
        with open("config.json", "r") as conf:
            loadedConfig = json.load(conf)
        return loadedConfig

    @classmethod
    def saveDefaultConfig(self):
        with open("config.json", "w") as conf:
            json.dump(self.defaultConfig, conf)
        return