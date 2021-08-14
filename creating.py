# from mysql.connector import *

# mydb = connect(host="localhost",user="root",passwd="123456789",database="utsavdb")
# mycursor = mydb.cursor()

# mycursor.execute("Create table login(FirstName varchar(200),LastName varchar(200),Email varchar(200),Age int(20),Password varchar(200),Gender varchar(200))")
import tkinter
from tkinter import messagebox
def func():
    a=54
    b = ""
    if a==0:
        pass
    

    elif not isinstance(a,(int,float)) or not isinstance(b,(int,float))  :
        messagebox.showerror("Error","a and b should be Number!")
    else:
        messagebox.showinfo("Success","a and b is int or float")
func()
