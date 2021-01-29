import tkinter
from tkinter import *
import webbrowser #necessary for launching the browser



class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.title('Check files')
        self.master.minsize(530,200)

        #Top label with instructions
        self.lbl_title = Label(self.master, justify = "left", text="You are editing the Summer sale webpage for our company!\nEnter the text and information for the sale below.")
        self.lbl_title.grid(row = 0, column = 0, padx = (10,10), pady = (10,10), columnspan = 2)
        self.lbl_title.config(font = ("Garamond", 15))

        #This is the text area where you input what you want. It can only insert body text, meaning on the html doc it goes inbetween <p> tags
        self.txt_body = Text (self.master, font = ("Garamond", 11), width = 60, height = 7)
        self.txt_body.grid(row = 1, column = 0, padx = (10,10), pady = (10,10), rowspan = 3, columnspan = 2)

        #in the create button, I replace all \n python syntaxes with the html <br> so that a multiline entry can be achieved. 
        self.btn_create = Button(self.master, text = "Create", width = 12, height = 2, command = lambda:self.write_file(self.txt_body.get('1.0', 'end').replace("\n","<br>")))
        self.btn_create.grid(row = 5, column = 0, padx = (5,5), pady=(5,5))

        self.close = Button(self.master, text = "Close Program", width = 12, height = 2, command = lambda:self.quit())
        self.close.grid(row=5, column=1, padx = (5,5), pady=(5,5), sticky=W)

        
    def write_file(self, content):
        f = open("summer_sale.html", "w") #This will create the document if it doesn't exist. I could build this out to allow the person to make a new file if desired, meaning it would need another parameter. 
        f.write(  #This writes the entire webpage, using content as a parameter to insert what they write.
"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Summer Sales!</title>
</head>
<body>
    <p>"""+content+"""</p>  
</body>
</html>""")
        f.close()
        webbrowser.open("file:///C:/Users/Lyman/Desktop/coding/portfolio_pieces/tech_academy_projects/tech-academy-python-projects/html_challenge/summer_sale.html", new=2)

    def quit(self):
        self.master.destroy()


if __name__ == "__main__":
    root = Tk()
    app = ParentWindow(root)
    root.mainloop()