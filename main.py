from version import get_python_version
from tools import tools, tools_main
import sys

def main():
    print("Hello and welcome to tasktracker :D\n")
    print(f"This instance of tasktracker is being run on python {get_python_version()}")

    print(
    """ [TOOLS]
    1. Start new task

    """)

    while(True):
        # get the user input
        selected_tool = input("Selection: ").strip()
        print(f"you have selected {selected_tool} of type {type(selected_tool)}")

        
        if (selected_tool == tools.START_NEW_TASK.value):
            tools_main()
            





main()