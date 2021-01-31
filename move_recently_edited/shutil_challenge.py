import shutil #used for moving files
import os
import datetime

import gui_challenge

#set source
#destination = "C:\\Users\\Lyman\\Desktop\\Folder_A\\"
today_datetime = datetime.datetime.now() #You can compare datetimes using simple comparison operators
yesterday_datetime = today_datetime - datetime.timedelta(days = 1) #process for getting datetimes in the past. timedelta is a change in time. then you subtract the change in time from today. 

#source = 'C:\\Users\\Lyman\\Desktop\\coding\\portfolio_pieces\\tech_academy_projects\\tech-academy-python-projects\\Folder_B\\'

def move_files(source, destination): #paramters are necessary since this comes from out of the file
    fileNames = os.listdir(source) #getting a list of the files in the source folder
    source += "\\" #This is necessary because when you select a folder it doesn't end with a slash. 
    destination += "\\"
    for i in fileNames:
        source_path = source+i
        mod_timestamp = os.path.getmtime(source_path) #This is the timestamp, seconds from epoch
        file_datetime = datetime.datetime.fromtimestamp(mod_timestamp) #this converts to a datetime

        if file_datetime >= yesterday_datetime: #simple comparison operator that works on datetime objects. Remember that datetimes are objects!
            shutil.move(source_path, destination) #moves the file

if __name__ == "__main__":
    pass
