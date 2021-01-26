# Python Version:      3.9.1
# Author:              Lyman McBride
#
# Purpose:             Student Tracking System. Similar to the phonebook project,
#                      but self produced. Requirements are outlined, but 
#                      no code is provided.

import tkinter as tk
from tkinter import *
import functions
import gui

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args,**kwargs)

        self.master = master
        self.master.minsize(500,370)
        functions.center_window(self,500,370)
        self.master.title("Student Tracking")
        self.master.configure(bg='#99e6ff')
        self.master.protocol("WM_DELETE_WINDOW", lambda: functions.ask_quit(self))

        gui.load_gui(self)

if __name__ == "__main__":
    root=tk.Tk()
    App = ParentWindow(root)
    root.mainloop()