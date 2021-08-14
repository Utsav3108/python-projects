from mysql.connector import *
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
def User_dashboard():

    wn = Tk()
    wn.geometry("700x700")

    mydb = connect(host="localhost",user="root",passwd="123456789",database="utsavdb")
    mycursor = mydb.cursor()
    sql = f"SELECT * FROM Login WHERE Firstname='srikant' "
    mycursor.execute(sql)
    data = mycursor.fetchone()
    print(data[0])
    print(data[1])
    print(data[2])
    print(data[3])
    print(data[4])
    print(data[5])


    Loginlabel = Label(wn,text="User Dashboard ",font=("Calibri,bold",20),bg="black",fg="white").pack(fill=BOTH)

    
    
    namelabel = Label(wn,text="Name:",font=("Calibri,bold",20)).place(x=100,y=100)
    passwordlabel = Label(wn,text="Password:",font=("Calibri,bold",20)).place(x=100,y=150)
    agelabel = Label(wn,text="Age:",font=("Calibri,bold",20)).place(x=100,y=200)
    genderlabel = Label(wn,text="Gender:",font=("Calibri,bold",20)).place(x=100,y=250)
    emaillabel = Label(wn,text="Email:",font=("Calibri,bold",20)).place(x=100,y=300)

    namelabel = Label(wn,text=f"{data[0]}",font=("Calibri,bold",20)).place(x=300,y=100)
    passwordlabel = Label(wn,text=f"{data[4]}",font=("Calibri,bold",20)).place(x=300,y=150)
    agelabel = Label(wn,text=f"{data[3]}",font=("Calibri,bold",20)).place(x=300,y=200)
    genderlabel = Label(wn,text=f"{data[5]}",font=("Calibri,bold",20)).place(x=300,y=250)
    emaillabel = Label(wn,text=f"{data[2]}",font=("Calibri,bold",20)).place(x=300,y=300)
    wn.mainloop() 
User_dashboard()    