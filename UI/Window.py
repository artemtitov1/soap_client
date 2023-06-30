import tkinter as tk
from UI.StateManager import StateManager


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Books client')
        self.state_manager = StateManager(self)
