import main
import functions
import tkinter as tk
from tkinter import *
from tkinter.ttk import *

def load_gui(self):
    #labels
    self.lbl_Fname = tk.Label(self.master, text = "First Name:", fg="black", bg="#99e6ff")
    self.lbl_Fname.grid(row=0, column=0, padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_Lname = tk.Label(self.master, text = "Last Name:", fg="black", bg="#99e6ff")
    self.lbl_Lname.grid(row=2, column=0, padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_Phone = tk.Label(self.master, text = "Phone Number:", fg="black", bg="#99e6ff")
    self.lbl_Phone.grid(row=4, column=0, padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_Email = tk.Label(self.master, text = "Email Address:", fg="black", bg="#99e6ff")
    self.lbl_Email.grid(row=6, column=0, padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_Course = tk.Label(self.master, text = "Current Course:", fg="black", bg="#99e6ff")
    self.lbl_Course.grid(row=8, column=0, padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_Student = tk.Label(self.master, text = "Student:", fg="black", bg="#99e6ff")
    self.lbl_Student.grid(row=0, column=2, padx=(27,0),pady=(10,0),sticky=N+W)

    #textboxes
    self.txt_Fname = tk.Entry(self.master,text = '')
    self.txt_Fname.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_Lname = tk.Entry(self.master,text = '')
    self.txt_Lname.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_Phone = tk.Entry(self.master,text = '')
    self.txt_Phone.grid(row=5,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_Email = tk.Entry(self.master,text = '')
    self.txt_Email.grid(row=7,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_Course = tk.Entry(self.master,text = '')
    self.txt_Course.grid(row=9,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    #listbox and scrollbar
    self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
    self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
    self.lstList1.bind('<<ListboxSelect>>', lambda event: functions.onSelect(self,event))
    self.scrollbar1.config(command=self.lstList1.yview)
    self.scrollbar1.grid(row=1,column=5,rowspan=9, columnspan=1,padx = (0,0),pady=(0,0),sticky=N+E+S+W)
    self.lstList1.grid(row=1,column=2,rowspan=9, columnspan=3,padx = (0,0),pady=(0,0),sticky=N+E+S+W)

    #buttons
    self.btn_add=tk.Button(self.master,width=12,height=2,text='Add', command=lambda: functions.addToList(self))
    self.btn_add.grid(row=10,column=0,padx=(20,0),pady=(40,10),sticky=W)
    self.btn_update=tk.Button(self.master,width=12,height=2,text='Update',command=lambda: functions.onUpdate(self))
    self.btn_update.grid(row=10,column=1,padx=(10,0),pady=(40,10),sticky=W)
    self.btn_delete = tk.Button(self.master,width=12,height=2,text='Delete',command=lambda: functions.onDelete(self))
    self.btn_delete.grid(row=10,column=2,padx=(10,0),pady=(40,10),sticky=W)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close',command=lambda: functions.ask_quit(self))
    self.btn_close.grid(row=10,column=4,columnspan=1,padx=(10,0),pady=(40,10),sticky=E)

    functions.create_db(self)
    functions.onRefresh(self)

if __name__ == "__main__":
    pass