import logging
import os

def logs_exist():
    
    file_log = None
    dir_log  = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))

    try:
        if not os.path.exists(dir_log):
            os.makedirs(dir_log)
    except PermissionError as e:
        print(f"Error while creating the log dir. : {e}")
        raise

    file_log = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "argos.log"))
    if not os.path.exists(file_log):
        try:
            with open(file_log,"a") as f:
                f.write("""/*
   ▄▄▄▄▄▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄▄▄▄▄▄        ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
 ▄▀            ▀▄  ▄              ▀▄   ▄▀         ░ ░▒▓░  ▄▀            ▀▄   ▄▀▀             ░
▐▌              ▐▌ █               ▐▌ ▐▌             ░▒▒ ▐▌              ▐▌ ▐▌     ▄▄▄▄     ▒▒
▓               ░█ ▓      ▒▀▀░     ░█ ▓               ░▓ ▓      █▀▀▒     ░█ █      ░  ░     ░▓
▒      █▀▀▄      █ ▒      ░  ▒     ▐▌ ▒      ▄▄▄▄▄▄▄▄▄▄█ ▒      █  ░      █ ▒      ▒  ▀▀▀▀▀▀▀▀
░      █▄▄▒    ┼┼█ ░      ▀▀▀▀    ▄▀  ░┼     █   ▄▄▄▄▄▄▄ ░      █  █▄     █ ▐▌      ▀▄▄▄▄▄▄   
█┼            ┼┼┼█ █┼     █▀▀▀▄   ▀▄  █┼     █   ▓┼┼  ┼░ █┼     █   ░    ┼░  ▀▄▄         ┼┼▀▄ 
█┼┼   ┼█▀▀█┼   ┼┼█ █┼┼   ┼░   █    ▐▌ █┼┼   ┼█▄▄▄▒┼┼┼ ┼░ █┼┼┼┼ ┼█   ▒┼  ┼┼▒     ▀▀▀▀▀▄▄┼├├┼├├▌
█┼┼┼┼┼┼░  █┼┼┼ ┼┼░ █┼┼┼┼┼┼░   ░   ┼┼░ █┼┼┼ ┼┼┼┼┼┼┼┼┼┼┼┼░ █┼┼┼┼┼┼█   ▓┼┼ ┼┼▓ ▀▀▀▀▀▀▀░  ▒┼├├┼├├▓
█┼┼┼┼┼┼▒  █┼┼┼┼┼┼▒ █┼┼┼┼┼┼▒   ▒┼┼ ┼┼▒ ▐▌┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼▒ ▐▌┼┼┼┼┼█▄▄▄▀┼┼┼┼▐▌ ▒┼┼├┼┼┼▒▄▄▓┼┼├┼┼▐▌
█┼┼┼┼┼┼▓  █┼┼┼┼┼┼▓ █┼┼┼┼┼┼▓   ▓┼┼┼┼┼▓  ▀▄┼┼┼┼┼┼┼┼┼┼┼┼┼┼▓  ▀▄┼┼┼┼┼┼┼┼┼┼┼┼▄▀  ░┼├┼┼┼┼┼┼┼┼┼┼┼┼▄▀ 
▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀     ▀▀▀▀▀▀▀▀▀▀▀▀    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀   
   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   
 ▄▀        ░ ░▒▓░ ▄              ▀▄  ▄              ▀▄ 
▐▌            ░▒▒ █               ▐▌ █               ▐▌
█              ░▓ ▓      ▒▀▀░     ░█ ▓      ▒▀▀░     ░█
▓       ▄▄▄▄▄▄▄▄█ ▒      ░  ▒      █ ▒      ░  ▒     ▐▌
░       ▓▄▄▄▄ ·   ░      █  █▄     █ ░      ▀▀▀▀    ▄▀ 
█ ┼     ▄▄▄▄▒   · █┼┼    █   ░    ┼░ █┼     █▀▀▀▄   ▀▄ 
█┼┼┼   ┼▓▄▄▄▄▄▄▄▄ █┼┼┼┼ ┼█   ▒  ┼┼┼▒ █┼┼   ┼░   █    ▐▌
█┼┼┼ ┼┼┼┼┼┼┼┼┼┼┼░ █┼┼┼┼┼┼█   ▓┼┼┼┼┼▓ █┼┼┼┼┼┼░   ░   ┼┼░
▐▌┼┼┼┼┼┼┼┼┼┼┼┼┼┼▒ █┼┼┼┼┼┼█▄▄▄▀┼┼┼┼▐▌ █┼┼┼┼┼┼▒   ▒┼┼ ┼┼▒
·▀▄┼┼┼┼┼┼┼┼┼┼┼┼┼▓ █┼┼┼┼┼┼┼┼┼┼┼┼┼┼▄▀  █┼┼┼┼┼┼▓   ▓┼┼┼┼┼▓
   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀    ▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀
*/
""")
        except PermissionError as e:
            print(f"Error while creating the log file. : {e}")
            raise
        except FileNotFoundError as e:
            print(f"The “data” folder does not exist, and an attempt to create it failed. : {e}")
            raise

    return file_log

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    file_log = logs_exist()   
    file_handler = logging.FileHandler(file_log, encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger