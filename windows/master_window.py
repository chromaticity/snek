from tkinter import *
from tkinter.ttk import *


# Master window for our entire game.
class MasterWindow:

    def __init__(self, root_window) -> None:
        self.root_window = root_window
        root_window.geometry("600x600")
        root_window.title("snek")
        root_window.configure(bg="black")

        # pack actually places the label on the screen.
        self.label = Label(root_window, text="Snake game goes here...")
        self.label.pack()

    def init_game(self) -> None:
        pass
