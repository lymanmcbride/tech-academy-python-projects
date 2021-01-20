#   Assignment: Making a database and adding new data to that database
#   Name:       Lyman McBride
#   Date:       1/20/2021


import sqlite3 as sl
fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
print("Files with the .txt extension:")
conn = sl.connect('txt-files.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtFiles( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileNames TINYTEXT)")
    conn.commit()
conn.close()

conn = sl.connect('txt-files.db')
with conn:
    cur = conn.cursor()
    for file in fileList:
        if '.txt' in file:
            cur.execute("INSERT INTO tbl_txtFiles(col_fileNames) VALUES (?)", (file,))
            conn.commit()
            print(file)
        else:
            continue
conn.close()
    


