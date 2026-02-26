from os_functions import clear
from rich.panel import Panel
from rich import print
import readchar

class Menu:
    # IMPORTANT: callback functions must be in a list that matches there index to the index of the option

    def __init__(self, panels):
        self._currently_selected = 1
        self._panels = panels
        self._renderables = panels.renderables

        self.set_highlight()

    def run(self):
        # run will run all of the provided panels excluding the first one (header) to as options    
        clear()

        while(True):
            print(Panel(self.get_panels()))

            match readchar.readkey():
                case readchar.key.UP:
                    self.move_up()
                case readchar.key.DOWN:
                    self.move_down()
                case readchar.key.ENTER:
                    break
                case readchar.key.BACKSPACE:
                    # created a tuple with the last index stating if this should be deleted
                    return (self._currently_selected, 1)
            clear()
            # created a tuple with the last index stating if this should be deleted
        return (self._currently_selected, 0)
    
    def get_panels(self):
        return self._panels

    def current_panel(self):
        return self._renderables[self._currently_selected]

    def remove_current_highlight(self):
        self.current_panel().style = "on white"

    def set_highlight(self):
        self.current_panel().style = "on red"

    def move_up(self):
        if self._currently_selected > 1:
            self.remove_current_highlight()
            self._currently_selected -= 1
            self.set_highlight()

    def move_down(self):
        if self._currently_selected < len(self._renderables) - 1:
            self.remove_current_highlight()
            self._currently_selected += 1
            self.set_highlight()
        
    # naughty naughty impure functions :D
        

   