import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3
import main
import gui

def center_window(self, w,h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo

def ask_quit(self):
    if messagebox.askokcancel("Exit program?"):
        self.master.destroy()
        os._exit(0)

#create database
def create_db(self):
    conn = sqlite3.connect('db_students.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_students( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT, \
            col_course TEXT \
            );")
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    #data = ('John','Doe','John Doe','111-111-1111','jdoe@email.com', 'Linear Algebra')
    conn = sqlite3.connect("db_students.db")
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_students (col_fname,col_lname,col_fullname,col_phone,col_email,col_course) VALUES (?,?,?,?,?,?)""", ('John', 'Doe', 'John Doe', '111-111-1111','jdoe@email.com','Linear Algebra'))
            conn.commit()
    conn.close()

def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_students""")
    count = cur.fetchone()[0]
    return cur,count


#button functions

def onSelect(self,event):
    varList = event.widget
    select = varList.curselection()[0]
    value=varList.get(select)
    conn=sqlite3.connect('db_students.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email,col_course FROM tbl_students WHERE col_fullname = (?)""", [value])
        varBody = cursor.fetchall()
        for data in varBody:
            self.txt_Fname.delete(0,END)
            self.txt_Fname.insert(0,data[0])
            self.txt_Lname.delete(0,END)
            self.txt_Lname.insert(0,data[1])
            self.txt_Phone.delete(0,END)
            self.txt_Phone.insert(0,data[2])
            self.txt_Email.delete(0,END)
            self.txt_Email.insert(0,data[3])
            self.txt_Course.delete(0,END)
            self.txt_Course.insert(0,data[4])

def addToList(self):
    var_Fname = self.txt_Fname.get().strip().title()
    var_Lname = self.txt_Lname.get().strip().title()
    var_Fullname = ("{} {}".format(var_Fname, var_Lname))
    print("var_fullname: {}".format(var_Fullname))
    var_Phone = self.txt_Phone.get().strip()
    var_Email = self.txt_Email.get().strip()
    var_Course = self.txt_Course.get().strip().title()
    if (len(var_Fname) > 0) and (len(var_Lname) > 0) and (len(var_Phone) > 0) and (len(var_Email) > 0): #user provides all necessary data
        conn = sqlite3.connect('db_students.db')
        with conn:
            cursor = conn.cursor()
            #check database for fullname, if it exists alert user and disregard request
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_students WHERE col_fullname = '{}'""".format(var_Fullname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0:
                print("chkName: {}".format(chkName))
                cursor.execute("""INSERT INTO tbl_students (col_fname,col_lname,col_fullname,col_phone,col_email,col_course) VALUES (?,?,?,?,?,?)""", (var_Fname,var_Lname,var_Fullname,var_Phone,var_Email,var_Course))
                self.lstList1.insert(END, var_Fullname) #update listBox with new full name
                onClear(self) # call the function to clear all of th textboxes
            else:
                messagebox.showerror("Name Error","'{}' already exists in the database! Please choose a different name.".format(var_Fullname))
                onClear(self) #call the function to clear all of the textboxes
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error","Please ensure that there is data in all four fields.")

def onUpdate(self):
    try:
        var_select = self.lstList1.curselection()[0] #index of list selection
        var_value = self.lstList1.get(var_select) #list selection's text value
    except:
        messagebox.showinfo("Missing selection","No name was selected from the list box. \nCancelling the Update request.")
        return
    # The user will only be allowed to update changes for phone and emails.
    # for name changes, the user will need to delete the entire record and start over.
    var_Phone = self.txt_Phone.get().strip()
    var_Email = self.txt_Email.get().strip()
    var_Fname = self.txt_Fname.get().strip().title()
    var_Lname = self.txt_Lname.get().strip().title()
    var_Fullname = ("{} {}".format(var_Fname, var_Lname))
    var_Course = self.txt_Course.get().strip().title()
    if (len(var_Phone) > 0) and (len(var_Email) > 0 and (len(var_Course) > 0)): #must be data present
        conn = sqlite3.connect('db_students.db')
        with conn:
            cur = conn.cursor()
            #count records to see if the user's changes are alread in
            #the database... meaning there are no changes to update.
            cur.execute("""SELECT COUNT(col_phone) FROM tbl_students WHERE col_phone = '{}'""".format(var_Phone))
            count_phone = cur.fetchone()[0]
            print(count_phone)
            cur.execute("""SELECT COUNT(col_email) FROM tbl_students WHERE col_email = '{}'""".format(var_Email))
            count_email = cur.fetchone()[0]
            print(count_email)
            cur.execute("""SELECT COUNT(col_course) FROM tbl_students WHERE col_course = '{}'""".format(var_Course))
            count_course = cur.fetchone()[0]
            print(count_course)
            cur.execute("""SELECT COUNT(col_fullname) FROM tbl_students WHERE col_fullname = '{}'""".format(var_Fullname))
            count_fullname = cur.fetchone()[0]
            print(count_fullname)
            if count_fullname == 0:
                response = messagebox.showerror("Error: Name Edited", "First and Last Name may not be updated. \nIf you would like to update the name, please create a new entry.")
            elif count_phone == 0 or count_email == 0 or count_course == 0:
                response = messagebox.askokcancel("Update Request","The following changes ({}), ({}), and ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_Phone,var_Email,var_Course,var_value))
                if response:
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""UPDATE tbl_students SET col_phone = '{0}', col_email = '{1}', col_course = '{2}' WHERE col_fullname = '{3}'""".format(var_Phone,var_Email,var_Course,var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request","No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected","({}), ({}), and ({}) \nare already in the database for this name. \n\nYour update request has been cancelled.".format(var_Phone,var_Email,var_Course))
            onClear(self)
        conn.close()
    else:
        messagebox.showerror("Missing information","Please select a name from the list. \nThen edit the phone or email information.")
    onClear(self)

def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection()) #Listbox's selected value
    conn = sqlite3.connect('db_students.db')
    with conn:
        cur = conn.cursor()
        # check count to ensure that this is not the last record in the database...
        # cannot delete last record or we will get an error
        cur.execute("""SELECT COUNT (*) FROM tbl_students""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with, ({}) \nwill be permanently deleted from the database. \n\nProceed with the deletion request?".format(var_select))
            if confirm:
                conn = sqlite3.connect('db_students.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_students WHERE col_fullname = '{}'""".format(var_select))
                onDeleted(self) #clears all textboxes
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first before you can delete ({}).".format(var_select,var_select))
    conn.close()

def onDeleted(self):
    onClear(self)
    ## onrefresh(self) # update the listbox of the changes
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    self.txt_Fname.delete(0,END)
    self.txt_Lname.delete(0,END)
    self.txt_Phone.delete(0,END)
    self.txt_Email.delete(0,END)
    self.txt_Course.delete(0,END)

def onRefresh(self):
    #populate the listbox, coinciding with the database
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('db_students.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_students""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
            cursor.execute("""SELECT col_fullname FROM tbl_students""")
            varList = cursor.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0,str(item))
                i+=1
    conn.close()

if __name__ == "__main__":
    pass