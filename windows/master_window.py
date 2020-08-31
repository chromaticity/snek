from tkinter import *
from tkinter.ttk import *


class MasterWindow:

    def __init__(self, master_window) -> None:
        self.master_window = master_window

    def open_master_window(self) -> None:
        top_level_window = Toplevel(self.master_window)
        top_level_window.title("snek")
        top_level_window.geometry("600x600")
        Label(top_level_window, text="Test Window").pack()

        label = Label(self.master_window)
        mainloop()