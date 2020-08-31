from tkinter import *
from tkinter.ttk import *
from windows.master_window import MasterWindow;

if __name__ == "__main__":
    root_window = Tk()
    master_window = MasterWindow(root_window)
    root_window.mainloop()