from mysql.connector import *
from tkinter import *
from tkinter import messagebox
mydb = connect(host="localhost",user="root",passwd="123456789",database="utsavdb")



win = Tk()
win.geometry("500x500")

# nameL = Label(win,text="First name",font=("verdana",16),width=10,border=1,bg="#ed7300",fg="white",relief="raised")
# nameL.place(x=10,y=10)

# nE = StringVar()
# nameE = Entry(win,width=15,textvariable=nE)
# nameE.place(x=50,y=10)



# passwdL = Label(win,text="Password",font=("verdana",16),width=10,border=1,bg="#ed7300",fg="white",relief="raised")
# passwdL.place(x=10,y=50)

# psswdE = StringVar()
# passwdE = Entry(win,width=15,textvariable=psswdE)
# passwdE.place(x=50,y=50)



def fet():
    mycursor = mydb.cursor()
    myresult=mycursor.execute("SELECT * FROM login where Firstname='ved'")
    for row in myresult:
        print(row)
fet()        
        
f= StringVar()
l = Text(win,width=20,height=20)
l.pack()
b = Button(win,text="xyz",command=lambda:l.insert(END,fet())).pack()

def signin():
    if psswdE.get()==myresult[1]:
        messagebox.showinfo("Success","Successfully Signed in")
    else :
        messagebox.showerror("Error","Wrong Password")
btn = Button(win,text="Sign in",font=("verdana",10),bg="#ed7300",fg="white",relief="raised",command=signin,width=12)
btn.place(x=90,y=90)

# win.mainloop()



