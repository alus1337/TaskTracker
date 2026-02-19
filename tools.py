from appdirs import user_data_dir
from datetime import datetime
from enum import Enum
from os_functions import clear
import os
import sys 
import json

class tools(Enum):
    START_NEW_TASK = '1'

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
    current_time = datetime.now()

    task_object = {
        "task": task,
        "goal": goal,
        "Start time": current_time.strftime("%Y-%m-%d %H:%M:%S")
    }

    file = f'{init_data_dir()}/{task}.json'
    print(file)
    
    with open(file, "w") as f:
        json.dump(task_object, f, indent=4) 

    print(task_object)

tools_main()
