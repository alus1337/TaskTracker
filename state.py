from pathlib import Path
from constants import USER_DATA_DIRECTORY
from os_functions import init_data_dir

def init():
    init_data_dir()

def get_active_tasks():
    #   each task has its own json file
    directory_contents = Path(USER_DATA_DIRECTORY)

    #   [0] is used to access the name of the 
    return [f.stem for f in directory_contents.iterdir() if f.is_file()]

def selection(options):
    for option in range(0, len(options)):
        print(f"{option + 1}: {options[option]}")
    
    selection = int(input("Selection: ")) - 1
    return options[selection]

