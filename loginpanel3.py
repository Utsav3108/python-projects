from tkinter import *
from mysql.connector import *
from tkinter import messagebox
from PIL import ImageTk,Image
class verify:
    def __init__(self,win):
        self.win = win
        self.win.geometry("600x400")
        self.win.title("verification")

        Lab = Label(self.win,text="Login",font=("calibri",30))
        Lab.pack()

        self.Entre = Entry(self.win,width=30)
        self.Entre.pack()

        Lab1 = Label(self.win,text="password",font=("calibri",30))
        Lab1.pack()

        self.Entre1 = Entry(self.win,width=30)
        self.Entre1.pack()

        self.but = Button(self.win,text="Verify",width=20,command=self.ver)
        self.but.pack()

    def ver(self):
        print()
        ved = self.Entre.get()
        passs = self.Entre1.get()
        print("pass:",passs)
        print("name:",ved)
        mydb = connect(host="localhost",user="root",passwd="123456789",database="utsavdb")
        mycursor = mydb.cursor()
        sql = f"SELECT * FROM Login WHERE Firstname='{ved}' "
        mycursor.execute(sql)
        data = mycursor.fetchone()
        print(data[4])
        if data[4]==passs:
            messagebox.showinfo("success","Success")
        else :
            messagebox.showerror("Error","Enter Correct Password")
win = Tk()
obj = verify(win)
win.mainloop()
