from constants import PYTHON_INSTANCE_VERSION
from tools import tools, tools_main
from os_functions import clear
import sys
import time

def main():


    while(True):
        clear()
        print("Hello and welcome to tasktracker :D\n")
        print(f"This instance of tasktracker is being run on python {PYTHON_INSTANCE_VERSION}")

        print(
        """ [TOOLS]
        1. Start new task
        2. List active tasks

        """)

        # get the user input
        selected_tool = input("Selection: ").strip()

        match selected_tool:
            case tools.START_NEW_TASK.value:
                tools_main(tools.START_NEW_TASK.value)

            case tools.LIST_ACTIVE_TASKS.value:
                tools_main(tools.LIST_ACTIVE_TASKS.value)

            





main()