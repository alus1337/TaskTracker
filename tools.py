from datetime import datetime
from enum import Enum
from os_functions import clear, create_file_path
import os
import sys 
import json

class tools(Enum):
    START_NEW_TASK = '1'

def start_new_task():
    clear()

    task = input("Please provide a short task description. Do not include what or why you are doing this task for just simply what needs to be done\nResponse: ")
    clear()

    goal = input("Please provide a short goal that this task contributes to.\nResponse: ")
    clear()

    current_time = datetime.now()

    task_object = {
        "task": task,
        "goal": goal,
        "Start time": current_time.strftime("%Y-%m-%d %H:%M:%S")
    }

    file = create_file_path(task_object["task"], "json")
    
    with open(file, "w") as f:
        json.dump(task_object, f, indent=4) 

    print(task_object)

    

def tools_main(selection='1'):
    match selection:
        case tools.START_NEW_TASK.value:
            start_new_task()
