from mysql.connector import *
from tkinter import *

win = Tk()
class login():
    def __init__(self):
        
        self.fn = Entry(win,width=20).pack()
    def buttn():
        mydb = connect(host="localhost",user="root",passwd="123456789",database="utsavdb")
        mycursor = mydb.cursor()
        
        mycursor.execute(f"Select * from login where Firstname='{fn.get()}'")

        myresult = mycursor.fetchone()
        print(myresult)
btn = Button(win,command=buttn).pack()
win.mainloop()

