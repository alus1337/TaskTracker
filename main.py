from constants import PYTHON_INSTANCE_VERSION
from tools import tools, start_new_task, list_active_tasks, add_task_steps
from menu import Menu
from os_functions import clear
from rich import print
from rich.prompt import Prompt
from rich.panel import Panel
from rich.align import Align
from rich.console import Group
from state import CONSOLE
import sys
import time

from enum import Enum
from state import init

def main():
    init()

    panel_group = Group(
        Panel(Align.center("[black]TOOLS[/black]"), style="on white"),
        Panel(Align.left("[black]start new task[/black]"), style="on white"),
        Panel(Align.left("[black]List active task[/black]"), style="on white"),
        Panel(Align.left("[black]Add task steps[/black]"), style="on white")
    )
    menu = Menu(panel_group)

    while(True):
        selected_option = menu.run()

        match selected_option[0]:
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