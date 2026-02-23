class Menu:
    def __init__(self, panels):
        self._currently_selected = 2
        self._panels = panels
        self._renderables = panels.renderables

        self.set_highlight()

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

    def selected_option(self):
       if self._currently_selected in range(1, len(self._renderables) + 1):
          return self._currently_selected

    

