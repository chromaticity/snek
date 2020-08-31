from tkinter import *
from tkinter.ttk import *
from windows.master_window import MasterWindow;

if __name__ == "__main__":
    master = Tk()
    master.geometry("600x600")

    master_window = MasterWindow(master)
    master_window.open_master_window()
