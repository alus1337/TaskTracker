import os
import sys
from appdirs import user_data_dir
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def init_data_dir():
    APP_NAME = "TaskTracker"
    APP_AUTHOR = "Alus"

    data_dir = user_data_dir(APP_NAME, APP_AUTHOR)

    try:
        os.makedirs(data_dir, exist_ok=True)
    except Exception as e:
        clear()
        input(f"Error during creating app data directory.\n--\n{e}")
        sys.exit(1)

    return data_dir

def create_file_path(file_name, ex):
    # init data dir returns the app data directory 
    return init_data_dir() + f"/{file_name}.{ex}"
