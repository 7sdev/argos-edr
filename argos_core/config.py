import json
import os


def load_config(): 
    data = {}
    current_dir =  os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "config.json"))

    if(os.path.exists(current_dir)):
        try:
            with open(current_dir) as f:
                data = json.load(f)
                for key in data.keys():
                    if key == "watch":
                        for path in data["watch"]:
                            if(os.path.exists(path) == False):
                                print("The directory to monitor (set to “watch” in config.json) cannot be found or is unreadable") 

        except json.JSONDecodeError as e:
            print(f"The “config.json” files are not valid JSON documents.\n Error : {e}")
            raise
        except UnicodeDecodeError as e:
            print(f"“config.json” does not contain any data encoded in UTF-8, UTF-16, or UTF-32.\n Error : {e}")   
            raise
    else:
        print("“config.json” not found")
    
    return data
    




