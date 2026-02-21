from constants import PYTHON_INSTANCE_VERSION
from tools import tools, start_new_task, list_active_tasks, add_task_steps
from os_functions import clear
from rich import print
from rich.prompt import Prompt
from rich.panel import Panel
from rich.align import Align
from state import CONSOLE
import sys
import time
from enum import Enum
from state import init

def main():
    init()

    while(True):
        clear()
        print("Hello and welcome to tasktracker :D\n")
        print(f"This instance of tasktracker is being run on python {PYTHON_INSTANCE_VERSION}")

        class ToolMenu(Enum):
            header = Panel(Align.center("[black]TOOLS[/black]"), style="on white")
            start_new_task = Panel(Align.left("[black]TOOLS[/black]"), style="on white")

        selection_controller = lambda ToolMenu: {

        }

        while(True):
            CONSOLE.print(
                Panel(Align.center("[black]TOOLS[/black]"), style="on white"),
                input()
            )

            CONSOLE.print(
                    Panel()
            )



        print(
            Panel.fit("[red]TOOLS[/red]", highlight=True),
            """
            1. Start new task
            2. List active tasks
            3. Add task steps
            4. Work on task
            """
        )
        
        # get the user input
        selected_tool = input("Selection: ").strip()

        match selected_tool:
            case tools.START_NEW_TASK.value:
                start_new_task()

            case tools.LIST_ACTIVE_TASKS.value:
                list_active_tasks()

            case tools.ADD_TASK_STEPS.value:
                add_task_steps()

            case tools.WORK_ON_TASK.value:
                print("[italic red]Hello[/italic red]:red_heart-emmoji:")
                time.sleep(3)
 
            





main()