# Python Version:      3.9.1
# Author:              Lyman McBride
#
# Purpose:             Phonebook project. Uses OOP, Tkinter GUI module,
#                      Tkinter Parent and Child relationships


#imports: tkinter, and other two modules created by me
from tkinter import *
import tkinter as tk
import phonebook_gui
import phonebook_functions

# Frame is the tkinter frame class.
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #master frame config
        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)
        #CenterWindow method centers the app on the user's screen
        phonebook_functions.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Project")
        self.master.configure(bg="#f0f0f0")
        #Tkinter built-in method to catch if they click the close x top right
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_functions.ask_quit(self))

        # loading gui widgits from other module
        phonebook_gui.load_gui(self)
        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
