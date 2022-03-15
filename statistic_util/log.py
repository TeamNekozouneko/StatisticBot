import datetime, os

def info(txt: str):
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

def err(txt: str):
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

def warn(txt: str):
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