class Menu:
    def __init__(self, panels):
        self._currently_selected = 2
        self.panels = panels
        self.renderables = panels.renderables

        self.set_highlight()

    def current_panel(self):
       return self.renderables[self._currently_selected]

    def remove_current_highlight(self):
        self.current_panel().style = "on white"      

    def set_highlight(self):
       self.current_panel().style = "on red"

    def move_up(self):
       if self._currently_selected > 1: 
        self.remove_current_highlight()
        self._currently_selected -= 1
        self.set_highlight()

    

