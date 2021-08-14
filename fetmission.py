from mysql.connector import *
from tkinter import *
from tkinter import messagebox
win = Tk()
mydb = connect(host="localhost",user="root",passwd="123456789",database="utsavdb")
# mycursor = mydb.cursor()



nameL = Label(win,text="First name",font=("verdana",16),width=10,border=1,bg="#ed7300",fg="white",relief="raised")
nameL.place(x=10,y=10)

nE = StringVar()
nameE = Entry(win,width=15,textvariable=nE)
nameE.place(x=50,y=10)

passwdL = Label(win,text="Password",font=("verdana",16),width=10,border=1,bg="#ed7300",fg="white",relief="raised")
passwdL.place(x=10,y=50)

psswdE = StringVar()
passwdE = Entry(win,width=15,textvariable=psswdE)
passwdE.place(x=50,y=50)


def fetch_all():
    query = "select * from login where firstname='shreya'"
    cur = mydb.cursor()
    cur.execute(query)
    
    
    # return row[0],row[4]
    # print("FirstName:",row[0])
    # print("LastName:",row[1])
    # print("Email:",row[2])
    # print("Age:",row[3])
    # print("Password:",row[4])
    print("pe:",psswdE.get())
    # print("Gender:",row[5])
    # print()
    # print()
        
    # if f"{psswdE.get()}"==f"{fetch_all()[1]}":
    #     messagebox.showinfo("Success","Successfully Signed in")
    # else :
    #     messagebox.showerror("Error","Wrong Password")            

btn = Button(win,text="Sign in",font=("verdana",10),bg="#ed7300",command=fetch_all,fg="white",relief="raised",width=12) #command=fetch_all
btn.place(x=90,y=90)

win.mainloop()