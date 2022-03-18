import json

class config:    

    # 初期の設定ファイルの内容です。
    defaultConfig = {
        "token": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",

        "msg": {
            "bot": False,
            "blackList": {
                "id": [],
                "startsWith": [],
                "endWith": [],
                "in": [],
                "name": []
            }
        },

        "database": {
            "prefix": "StatisticBot_"
        }
    }

    # 読み込んだ設定ファイルの内容
    loadedConfig = None

    @classmethod
    def reloadConfig(self, fp: str = "config.json"):
        # reloadConfig()の存在異議とは??????????????
        """設定ファイルを再読み込みします。"""
        return self.loadConfig(fp)

    @classmethod
    def loadConfig(self, fp: str = "config.json") -> dict:
        """設定ファイルを読み込みます"""
        with open(fp, "r") as conf:
            loadedConfig = json.load(conf)
        return loadedConfig

    @classmethod
    def saveDefaultConfig(self, fp: str = "config.json"):
        """設定ファイルをリセットします。"""
        with open(fp, "w") as conf:
            json.dump(self.defaultConfig, conf, indent=4)
        return