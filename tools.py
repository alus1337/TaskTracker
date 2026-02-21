from datetime import datetime
from enum import Enum
from os_functions import clear, create_file_path 
from constants import USER_DATA_DIRECTORY
from state import get_active_tasks, selection
import json

class tools(Enum):
    START_NEW_TASK = '1'
    LIST_ACTIVE_TASKS = '2'
    ADD_TASK_STEPS = '3'
    WORK_ON_TASK = '4'

def start_new_task():
    clear()

    task = input("Please provide a short task description. Do not include what or why you are doing this task for just simply what needs to be done\nResponse: ")
    clear()

    goal = input("Please provide a short goal that this task contributes to.\nResponse: ")
    clear()

    current_time = datetime.now()

    #this is the issue it is double encoded with the final dump
    task_object = {
                    "task": task,
                    "goal": goal,
                    "Start time": current_time.strftime("%Y-%m-%d %H:%M:%S")
                    }

    file = create_file_path(task, "json")
    
    with open(file, "w") as f:
        json.dump(task_object, f, indent=4) 

    print(f"{task_object}\nWas printed to {file}")

def list_active_tasks():
    #   [0] is used to access the name of the 
    task_files = get_active_tasks()

    clear()  
    for task in task_files:
        print(task)
    input("Press any key to exit...")

def add_task_steps():
    clear()

    # retrief the current .json file for the task and add a steps key with tuples of steps the tuple is the step and true or false to mark commpletion
    task = selection(get_active_tasks())
    clear()

    task_object = json.load(open(f"{USER_DATA_DIRECTORY}/{task}.json", "r"))

    if "steps" not in task_object:
        task_object["steps"] = {}

    while True:
        step = input("Please provide a short step.\nAnswer: ")
        clear()

        # creates step and sets completion to false
        task_object["steps"][step] = 0
        
        if input("Create another step? Yes or No\nAnswer: ").lower() == "no":
            break

    clear()
    print(f"Updated steps\n---\n{task_object["steps"]}\n---")

    if input("Add these steps? Yes or No\nAnswer: ").lower() == "No":
        return None
    
    with open(f"{USER_DATA_DIRECTORY}/{task}.json", "w") as f:
        json.dump(task_object, f)

        


    

