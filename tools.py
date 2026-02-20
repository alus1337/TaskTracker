from datetime import datetime
from enum import Enum
from os_functions import clear, create_file_path 
from pathlib import Path
from constants import USER_DATA_DIRECTORY
import json

class tools(Enum):
    START_NEW_TASK = '1'
    LIST_ACTIVE_TASKS = '2'
    ADD_TASK_STEPS = '3'

def start_new_task():
    clear()

    task = input("Please provide a short task description. Do not include what or why you are doing this task for just simply what needs to be done\nResponse: ")
    clear()

    goal = input("Please provide a short goal that this task contributes to.\nResponse: ")
    clear()

    current_time = datetime.now()

    task_object = json.dumps({
                            "task": task,
                            "goal": goal,
                            "Start time": current_time.strftime("%Y-%m-%d %H:%M:%S")
                            },
                            indent=4)

    file = create_file_path(task, "json")
    
    with open(file, "w") as f:
        json.dump(task_object, f) 

    print(f"{task_object}\nWas printed to {file}")

def list_active_tasks():
    #   each task has its own json file
    directory_contents = Path(USER_DATA_DIRECTORY)

    #   [0] is used to access the name of the 
    task_files = [f.stem for f in directory_contents.iterdir() if f.is_file()]

    clear()  
    for task in task_files:
        print(task)
    input("Press any key to exit...")

def add_task_steps():
    pass

