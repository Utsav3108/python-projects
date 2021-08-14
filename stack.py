from tkinter import*
from tkinter import messagebox
import mysql.connector
import time
import datetime
import random

w = 300
h = 2

def register_user():

    global username_info
    global password_info

    if len(username.get()) == 0 and len(password.get()) == 0:
        print("Please fill in the Missing Info")

    if len(username.get()) == 0 and len(password.get()) != 0 :
            print("Please Enter a Username")
    elif len(username.get()) != 0 and len(password.get()) == 0:
                    print("Please enter a Password")


    else:
        username_info = username.get()
        password_info = password.get()

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123456789",
            database="utsavdb"
        )
        mycursor = mydb.cursor()
        sqlFormula = "INSERT INTO users (Username, Password) VALUES (%s, %s)"
        insertvar = (username_info, password_info)
        user1 = ("Joshua", "Cuyugan")
        mycursor.execute(sqlFormula, insertvar)
        mydb.commit()

        username.set("")
        password.set("")

def register():
    global screen1

    screen.withdraw()
    screen1 = Toplevel(screen)
    screen1.title("Registration")
    screen1.geometry("500x250+700+350")

    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()

    Label(screen1, text = " Please Enter Your Details Below", bg = "black", width = w , height = h, font = ("Calibri", 20) , fg = "white").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username").place(x=220, y=85)
    username_entry = Entry(screen1, textvariable = username, width="50").place(x=100, y=110)
    Label(screen1, text = "Password").place(x=220, y=135)
    password_entry = Entry(screen1, textvariable = password, width="50").place(x=100, y=160)
    Button(screen1, text= "Register", height="1", width="20", command = register_user).place(x=80, y=200)
    Button(screen1, text="Cancel", height="1", width="20", command= on_closereg).place(x=270, y=200)


    screen1.protocol("WM_DELETE_WINDOW", on_closereg)



def login():
    global screen2

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="123456789",
        database="utsavdb"
    )
    mycursor = mydb.cursor()
    sql_select_Query = "select * from users"
    mycursor.execute(sql_select_Query)
    records = mycursor.fetchall()
    for row in records:
        print("Username" , row[1],)
        print("Password", row[2], "\n" )
        mycursor.close()

    screen.withdraw()
    screen2 = Toplevel(screen)
    screen2.title("HOT or SUPER HOT")
    screen2.geometry("800x600+550+220")


    screen2.protocol("WM_DELETE_WINDOW", on_close)

def checker():
    if len(username.get()) == 0 and len(password.get()) == 0:
        print("Please fill in the Missing Info")


def on_close():
    screen2.withdraw()
    screen.update()
    screen.deiconify()
    screen.lift()

def on_closereg():
    screen1.withdraw()
    screen.update()
    screen.deiconify()
    screen.lift()

def verify():
    global name
    global userlogcred
    global userpascred

    userlogcred = username_verify.get()
    userpascred = password_verify.get()

    loadname = ("SELECT Username FROM users WHERE Username =%s")
    loadpass = ("SELECT Password FFROM users WHERE Password =%s")

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="123456789",
        database="utsavdb"
    )
    mycursor = mydb.cursor()

    if len(username_verify.get()) == 0 and len(password_verify.get()) == 0:
        print("Please fill in the Missing Info")
    if len(username_verify.get()) == 0 and len(password_verify.get()) != 0 :
        print("Please Enter a Username")
    elif len(username_verify.get()) != 0 and len(password_verify.get()) == 0:
        print("Please enter a Password")

    else:
        mycursor.execute(loadname, userlogcred)
        mycursor.execute(loadpass, userpascred)
        logincheck = mycursor.fetchone()
        loginpasscheck = mycursor.fetchone()
        if logincheck is None:
            print("Sorry, could not find you in the database\nOr it just isn't working")
        if logincheck is not None and loginpasscheck is None:
            print("Please Enter your Password")
        elif logincheck is None and loginpasscheck is not None:
            print("Please enter Your Username")
        else:
            print("pass\nSuccessfully loaded {} from the database".format(username_verify.get()))



def main_Screen():

    global screen

    screen = Tk()
    screen.geometry("600x300+650+350")
    screen.title("Login System")


    Label(text = "Login System" , bg = "black", width = w , height = h, font = ("Calibri", 20) , fg = "white").pack()
    Label(text = "").pack()
    Button(text = "Login", height = h, width = "30", command = verify).place(x=50 , y=200)
    Label(text = "").pack()
    Button(text = "Register" ,height = h, width = "30", command = register).place(x=320 , y=200)


    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()
    Label(screen, text = "Username").place(x=265, y = 90)
    username_entry1 = Entry(screen, textvariable = username_verify, width = "80").place(x=57, y=110)
    Label(screen, text="Password").place(x=267, y=140)
    password_entry1 = Entry(screen, textvariable = password_verify, width = "80").place(x=57, y=160)

    screen.mainloop()


main_Screen()

print("Hello World")