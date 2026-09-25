import logging
import os

def logs_exist():
    
    file_log = None
    dir_log  = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data")) # Create the path to the “data” folder

    try:
        if not os.path.exists(dir_log): # We check the data path 
            os.makedirs(dir_log) # If it doesn't exist, we'll create it
    except PermissionError as e: # We handle the error if permissions are missing
        print(f"Error while creating the log dir. : {e}")
        raise

    file_log = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "argos.log")) # Creating the path to the log file
    if not os.path.exists(file_log): # We check to see if the logs file already exists
        try:
            with open(file_log,"a") as f: # If it doesn't exist, we'll create it
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
        except PermissionError as e: # We handle the error if permissions are missing
            print(f"Error while creating the log file. : {e}")
            raise
        except FileNotFoundError as e: # If the file creation fails, the user is notified.
            print(f"The “data” folder does not exist, and an attempt to create it failed. : {e}")
            raise

    return file_log

def level_logger(verbose = False):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        file_log = logs_exist()

        formatter_file = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        formatter_console = logging.Formatter(
            "%(levelname)s - %(message)s"
        )

        h_console = logging.StreamHandler()
        h_console.setFormatter(formatter_console)

        h_fichier = logging.FileHandler(
            file_log,
            encoding="utf-8"
        )
        h_fichier.setFormatter(formatter_file)

        logger.addHandler(h_console)
        logger.addHandler(h_fichier)

    for handler in logger.handlers:
        if isinstance(handler, logging.FileHandler):
            handler.setLevel(logging.DEBUG)
        elif isinstance(handler, logging.StreamHandler):
            handler.setLevel(
                logging.DEBUG if verbose else logging.INFO
            )

    return logger


def get_logger():

    logger = level_logger()

    return logger