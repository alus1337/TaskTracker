<<<<<<< HEAD
from appdirs import user_data_dir
from datetime import datetime
from enum import Enum
from os_functions import clear
=======
from datetime import datetime
from enum import Enum
from os_functions import clear, create_file_path
>>>>>>> 8790970 (added start task)
import os
import sys 
import json

class tools(Enum):
    START_NEW_TASK = '1'

<<<<<<< HEAD
def init_data_dir():
    APP_NAME = "TaskTracker"
    APP_AUTHOR = "Alus"

    data_dir = user_data_dir(APP_NAME, APP_AUTHOR)
    os.makedirs(data_dir, exist_ok=True)

    return data_dir
    

def tools_main():
    clear()

    task = input("Please provide a short task description. Do not include what or why you are doing this task for just simply what needs to be done")
    goal = input("Please provide a short goal that this task contributes to.")
=======
def start_new_task():
    clear()

    task = input("Please provide a short task description. Do not include what or why you are doing this task for just simply what needs to be done\nResponse: ")
    clear()

    goal = input("Please provide a short goal that this task contributes to.\nResponse: ")
    clear()

>>>>>>> 8790970 (added start task)
    current_time = datetime.now()

    task_object = {
        "task": task,
        "goal": goal,
        "Start time": current_time.strftime("%Y-%m-%d %H:%M:%S")
    }

<<<<<<< HEAD
    file = f'{init_data_dir()}/{task}.json'
    print(file)
=======
    file = create_file_path(task_object["task"], "json")
>>>>>>> 8790970 (added start task)
    
    with open(file, "w") as f:
        json.dump(task_object, f, indent=4) 

    print(task_object)

<<<<<<< HEAD
tools_main()
=======
    

def tools_main(selection='1'):
    match selection:
        case tools.START_NEW_TASK.value:
            start_new_task()
>>>>>>> 8790970 (added start task)
