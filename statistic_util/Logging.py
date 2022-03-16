import datetime, os

class LogLevel:
        INFO: str = "_info"
        WARN: str = "_warn"
        ERR: str = "_error"

        # aliases
        ERROR: str = "_error"
        WARNING: str = "_warn"
        INFORMATION: str = "_info"

class log:
    """
    ## ログ機能群
    `logging`というモジュールあるのにめんどくて使わなくて自作したアホ用の機能です。

    ### 使用方法の例
    ```py
    from statistic_util import log

    log.info("Example text")
    
    # [xx/xx 00:00:00 INFO] Example text
    """

    @classmethod
    def log(self, level: str, txt: str):
        """info()とかerr()とかwarn()使いたくないならこれ"""
        if (level == LogLevel.ERR or level == LogLevel.ERROR):
            return self.err(txt)
        elif (level == LogLevel.INFO or level == LogLevel.INFORMATION):
            return self.info(txt)
        elif (level == LogLevel.WARN or level == LogLevel.WARNING):
            return self.warn(txt)
        else:
            raise NameError("そんなログレベルないぞ")

    @classmethod
    def info(self, txt: str):
        """
        ログの案内情報をログに記録します。
        """
        dt = datetime.datetime.now()
        tx = f"[{dt.strftime('%m/%d %H:%M:%S')} INFO] {txt}"

        if (not os.path.exists("log/")):
            os.mkdir("log")

        if (not os.path.exists(f"log/{dt.strftime('%m-%d')}.log")):
            with open(f"log/{dt.strftime('%m-%d')}.log", "w", encoding="utf-8", newline="\n") as log:
                log.write(tx)
        else:
            with open(f"log/{dt.strftime('%m-%d')}.log", "a", encoding="utf-8", newline="\n") as log:
                log.write("\n"+tx)

        print(tx)
    
    @classmethod
    def err(self, txt: str):
        """
        ログのエラー情報をログに記録します。
        """
        dt = datetime.datetime.now()
        tx = f"\033[31m[{dt.strftime('%m/%d %H:%M:%S')} ERR] {txt}\033[0m"

        if (not os.path.exists("log/")):
            os.mkdir("log")

        if (not os.path.exists(f"log/{dt.strftime('%m-%d')}.log")):
            with open(f"log/{dt.strftime('%m-%d')}.log", "w", encoding="utf-8", newline="\n") as log:
                log.write(f"[{dt.strftime('%m/%d %H:%M:%S')} ERR] {txt}")
        else:
            with open(f"log/{dt.strftime('%m-%d')}.log", "a", encoding="utf-8", newline="\n") as log:
                log.write(f"\n[{dt.strftime('%m/%d %H:%M:%S')} ERR] {txt}")

        print(tx)
    
    @classmethod
    def warn(self, txt: str):
        """
        ログの警告情報をログに記録します。
        """
        dt = datetime.datetime.now()
        tx = f"\033[33m[{dt.strftime('%m/%d %H:%M:%S')} WARN] {txt}\033[0m"

        if (not os.path.exists("log/")):
            os.mkdir("log")

        if (not os.path.exists(f"log/{dt.strftime('%m-%d')}.log")):
            with open(f"log/{dt.strftime('%m-%d')}.log", "w", encoding="utf-8", newline="\n") as log:
                log.write(f"[{dt.strftime('%m/%d %H:%M:%S')} WARN] {txt}")
        else:
            with open(f"log/{dt.strftime('%m-%d')}.log", "a", encoding="utf-8", newline="\n") as log:
                log.write(f"\n[{dt.strftime('%m/%d %H:%M:%S')} WARN] {txt}")

        print(tx)
    
    @classmethod
    def append_log(self, txt: str):
        dt = datetime.datetime.now()

        if (not os.path.exists("log/")):
            os.mkdir("log")

        if (not os.path.exists(f"log/{dt.strftime('%m-%d')}.log")):
            with open(f"log/{dt.strftime('%m-%d')}.log", "w", encoding="utf-8", newline="\n") as log:
                log.write("\n"+txt)
        else:
            with open(f"log/{dt.strftime('%m-%d')}.log", "a", encoding="utf-8", newline="\n") as log:
                log.write("\n"+txt)