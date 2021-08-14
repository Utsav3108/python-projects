from tkinter import *          #==========PROGRAM STARTS
from mysql.connector import *
from tkinter import messagebox
from PIL import ImageTk,Image
root = Tk()
root.geometry("700x700")
root.config(bg="white")
root.title("Registration")

#==============BACKGROUND IMAGE
img = Image.open(f"D:\MyPythonfolder2\pixabay.jpg")
ic = ImageTk.PhotoImage(img)
l = Label(root,image=ic).pack()

#-------------------LABEL
login = Label(root,text="Registration",font=("verdana",22),width=39,justify=CENTER,bg="#ed7300",fg="white",relief="raised")
login.place(x=0,y=70)

Uname = Label(root,text="User name",font=("verdana",16),width=12,border=1,bg="#ed7300",fg="white",relief="raised")
Uname.place(x=150,y=150)

name = Label(root,text="Name",font=("verdana",16),width=12,border=1,bg="#ed7300",fg="white",relief="raised")
name.place(x=150,y=200)

passwd = Label(root,text="Set Password",font=("verdana",16),width=12,border=1,bg="#ed7300",fg="white",relief="raised")
passwd.place(x=150,y=250)

email = Label(root,text="Email",font=("verdana",16),width=12,border=1,bg="#ed7300",fg="white",relief="raised")
email.place(x=150,y=300)

age = Label(root,text="Age",font=("verdana",16),width=12,border=1,bg="#ed7300",fg="white",relief="raised")
age.place(x=150,y=350)

gender = Label(root,text="Gender",font=("verdana",16),width=12,border=1,bg="#ed7300",fg="white",relief="raised")
gender.place(x=150,y=400)

#---------------RADIOBUTTON
mm = BooleanVar()
mgender = Radiobutton(root,text="Male",value=1,variable=mm,bg="white")
mgender.place(x=400,y=400)

fgender = Radiobutton(root,text="female",value=0,variable=mm,bg="white")
fgender.place(x=450,y=400)
def f():      #============LOGIC FOR GETTING VALUE FROM RADIOBUTTON 
    genF=""
    genM=""                
    if mm.get()==True:
        genM = genM + "Male"
        return genM
    else:
        genF = genF + "Female"
        return genF
    
#----------------ENTRY
def entf(event):
    fnameE.config(relief=RAISED)
def leff(event):
    fnameE.config(relief=GROOVE)    
fnE = StringVar()                  #============fnE == USERNAME
fnameE = Entry(root,width=23,textvariable=fnE)
fnameE.place(x=400,y=150)
fnameE.bind("<Enter>",entf)
fnameE.bind("<Leave>",leff)

def entl(event):
    lnameE.config(relief=RAISED)
def lefl(event):
    lnameE.config(relief=GROOVE)
lnE = StringVar()                  #============lnE == NAME    
lnameE = Entry(root,width=23,border=1,textvariable=lnE)
lnameE.place(x=400,y=200)
lnameE.bind("<Enter>",entl)
lnameE.bind("<Leave>",lefl)

def entP(event):
    passwdE.config(relief=RAISED)
def lefP(event):
    passwdE.config(relief=GROOVE)
pwd = StringVar()
passwdE = Entry(root,width=23,border=1,textvariable=pwd)
passwdE.place(x=400,y=250)
passwdE.bind("<Enter>",entP)
passwdE.bind("<Leave>",lefP)

def entEm(event):
    emailE.config(relief=RAISED)
def lefEm(event):
    emailE.config(relief=GROOVE)
emE = StringVar()    
emailE = Entry(root,width=23,border=1,textvariable=emE)
emailE.place(x=400,y=300)
emailE.bind("<Enter>",entEm)
emailE.bind("<Leave>",lefEm)

def entA(event):
    ageE .config(relief=RAISED)
def lefA(event):
    ageE .config(relief=GROOVE)
ageS = IntVar()    
ageE = Entry(root,width=23,border=1,textvariable=ageS)
ageE.place(x=400,y=350)
ageE.bind("<Enter>",entA)
ageE.bind("<Leave>",lefA)

def entquit(event):
    QuitB.config(bg="#ff7f3b")
def leftquit(event):
    QuitB.config(bg="#ed7300")
QuitB = Button(root,text="Quit",command=quit,width=12,font=("verdana",10),bg="#ed7300",fg="white",relief="raised")
QuitB.place(x=370,y=500)
QuitB.bind("<Enter>",entquit)
QuitB.bind("<Leave>",leftquit)
#==================================SAVE button
def save():
    mydb = connect(host="localhost",user="root",passwd="123456789",database="utsavdb")
    mycursor = mydb.cursor()
    sql = f"SELECT * FROM Login WHERE Firstname='{fnE.get()}'"   
    mycursor.execute(sql)
    data = mycursor.fetchone()
    print(data)

    if fnE.get()=="" or lnE.get()=="" or ageS.get()==0 or ageS.get()=="" or pwd.get()=="" or f()=="" or emE.get()=="":
        messagebox.showerror("Error","All Fields are Required!")
    elif data!=None:
        messagebox.showerror("Error","User Exist! Try Another User Name")
    else :
        mydb = connect(host="localhost",user="root",passwd="123456789",database="utsavdb")
        mycursor = mydb.cursor()
        sqlform = "Insert into login(firstname,lastname,age,password,gender,email) value(%s,%s,%s,%s,%s,%s)"
        loginn = [(fnE.get(),lnE.get(),ageS.get(),pwd.get(),f(),emE.get())] #===INSERTING USER DATA TO DATABASE
        mycursor.executemany(sqlform,loginn)
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Succes","Data Successfully Saved!")
        print(f"firstname:{fnE.get()}\n"
            f"lastname:{lnE.get()}\n"
            f"age:{ageS.get()}\n"
            f"Email:{emE.get()}\n"
            f"Password:{pwd.get()}\n"
            f"gender:{f()}\n")
def entsave(event):
    Save.config(bg="#ff7f3b")
def leftsave(event):
    Save.config(bg="#ed7300")
Save = Button(root,text="Save",font=("verdana",10),bg="#ed7300",fg="white",relief="raised",command=save,width=12)
Save.place(x=270,y=500)
Save.bind("<Enter>",entsave)
Save.bind("<Leave>",leftsave)
#===========================================DELETE button
def dlte():
    mydb = connect(host="localhost",user="root",passwd="123456789",database="utsavdb")
    mycursor = mydb.cursor()
    if fnE.get()=="":
        messagebox.showinfo("Error","Kindly enter Firstname to delete Data!")
    else :
        mycursor.execute(f"DELETE FROM login where FirstName='{fnE.get()}'") #==DELETE USER DATA FROM DATABASE
        mydb.commit()
        mydb.close()
def entdel(event):
    delete.config(bg="#ff7f3b")
def leftdel(event):
    delete.config(bg="#ed7300")
delete = Button(root,text="Delete",font=("verdana",10),bg="#ed7300",fg="white",relief="raised",command=dlte,width=12)
delete.place(x=170,y=500)
delete.bind("<Enter>",entdel)
delete.bind("<Leave>",leftdel)

#================================FOR LOGIN 
def login_verify():
    class verify:
        def __init__(self,win):     #======TO INITIALIZE LOGIN WINDOW
            self.win = win
            self.win.geometry("600x400")
            self.win.title("Login")

            Lab = Label(self.win,text="Login",font=("calibri",30),bg="black",fg="white",width=30)
            Lab.pack(fill=BOTH)

            Lab = Label(self.win,text="User",font=("calibri",30),width=30)
            Lab.pack()

            self.Entre = Entry(self.win,width=40,justify=CENTER)
            self.Entre.pack()

            Lab1 = Label(self.win,text="password",font=("calibri",30))
            Lab1.pack()

            self.Entre1 = Entry(self.win,width=40,justify=CENTER)
            self.Entre1.pack()

            self.Nextbutton = Button(self.win,text="Next->",font=("calibri",12),width=20,command=self.ver)
            self.Nextbutton.pack()
            
            self.ForgetPasswordbutton = Button(self.win,text="Forget Password",font=("calibri",12),width=20,command=self.Forget_password)
            self.ForgetPasswordbutton.pack()

            self.closebutton = Button(self.win,text="Close",font=("calibri",12),width=20,command=self.win.destroy)
            self.closebutton.pack()

            self.Quitbutton = Button(self.win,text="Quit",font=("calibri",12),width=20,command=quit)
            self.Quitbutton.pack()
        def Forget_password(self):        #=====FORGET_PASSWROD WINDOW
            Usr = self.Entre.get()
            if Usr=="":
                messagebox.showerror("Error","Enter Username",parent=self.win)
            else :
                self.resetscreen = Tk()
                self.resetscreen.geometry("500x300")
                self.resetscreen.title("Resetpassword")

                resetlab = Label(self.resetscreen,text="Reset Password",font=("Calibri,bold",20),bg="black",fg="white").pack(fill=BOTH)
                
                self.emaillabel = Label(self.resetscreen,text=f"Hey {Usr},Enter your Email",font=("Calibri,bold",17)).pack()
                self.Ent = Entry(self.resetscreen,width=40,justify=CENTER)
                self.Ent.pack()

                passlabel = Label(self.resetscreen,text="New Password",font=("Calibri,bold",17)).pack()
                
                self.pas = Entry(self.resetscreen,width=40,justify=CENTER)
                self.pas.pack()
            
                mydb = connect(host="localhost",user="root",passwd="123456789",database="utsavdb")
                mycursor = mydb.cursor()
                sql = f"SELECT * FROM Login WHERE Firstname='{Usr}'"
                mycursor.execute(sql)
                data = mycursor.fetchone()
                print("data:",data[2])

                def resett():
                    print("pas",self.pas.get())
                    print("Email:",self.Ent.get())

                    if self.Ent.get()==data[2]:       #=============RESET PASSWORD
                        updatequery = f"UPDATE login SET password = '{self.pas.get()}'  WHERE email = '{self.Ent.get()}'"
                        mycursor.execute(updatequery)
                        mydb.commit()
                        mydb.close()
                        messagebox.showinfo("Success",f"{Usr},Your Password Successfully Reset!",parent=self.win)
                    else :
                        messagebox.showerror("Error",f"{Usr},Please Enter your Correct Email!",parent=self.resetscreen)
                    
                btn = Button(self.resetscreen,text="Reset",width=20,command=resett,font=("calibri",12)).pack()
                btn = Button(self.resetscreen,text="close",width=20,font=("calibri",12),command=self.resetscreen.destroy).pack()
                
                self.resetscreen.mainloop()
        def ver(self):     #=================USER PASSWORD VERIFIER
            User = self.Entre.get()
            passs = self.Entre1.get()
            print("pass:",passs)
            print("name:",User)
            if User=="" and passs=="":          #========VALIDATION
                messagebox.showerror("Error","Enter User name and Password",parent=self.win)
            elif User=="" and passs!="":
                messagebox.showerror("Error","Enter User name",parent=self.win)
            elif User!="" and passs=="":
                messagebox.showerror("Error","Kindly enter your Password!",parent=self.win)
            else:
                mydb = connect(host="localhost",user="root",passwd="123456789",database="utsavdb")
                mycursor = mydb.cursor()
                sql = f"SELECT * FROM Login WHERE Firstname='{User}'"
                mycursor.execute(sql)
                data = mycursor.fetchone()
                print("tuple",data)
                if data==None:
                    messagebox.showerror("Error","User not Found!")
                else :
                    print("data pass",data[4])
                    if data[4]!=passs:
                        messagebox.showerror("Error","Enter Correct Password",parent=self.win)
                    else :         
                        wn = Tk()    #==========USER DASHBOARD WINDOW
                        wn.geometry("700x700")
                        wn.title("User Dashboard")

                        mydb = connect(host="localhost",user="root",passwd="123456789",database="utsavdb")
                        mycursor = mydb.cursor()
                        sql = f"SELECT * FROM Login WHERE Firstname='{User}' "
                        mycursor.execute(sql)
                        data = mycursor.fetchone()

                        print(data[0])      #===========PRINTING ALL FETCHED USER DATA
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

                        nmelabel = Label(wn,text=f"{data[0]}",font=("Calibri,bold",20)).place(x=300,y=100)
                        psswrdlabel = Label(wn,text=f"{data[4]}",font=("Calibri,bold",20)).place(x=300,y=150)
                        aglabel = Label(wn,text=f"{data[3]}",font=("Calibri,bold",20)).place(x=300,y=200)
                        gndrlabel = Label(wn,text=f"{data[5]}",font=("Calibri,bold",20)).place(x=300,y=250)
                        emillabel = Label(wn,text=f"{data[2]}",font=("Calibri,bold",20)).place(x=300,y=300)

                        quitbtn = Button(wn,text="Quit",command=quit,width=20,font=("calibri",16)).place(x=150,y=350)
                        closebtn = Button(wn,text="Close",command=wn.destroy,width=20,font=("calibri",16)).place(x=150,y=410)
                        editbtn = Button(wn,text="Edit",command=self.edit,width=20,font=("calibri",16)).place(x=150,y=470)
                        
                        wn.mainloop()

    
    win = Tk()
    obj = verify(win)
    win.mainloop()
def ent1login(event):
    Login_btn.config(bg="#ff7f3b")
def leftLogin(event):
    Login_btn.config(bg="#ed7300")
Login_btn = Button(root,text="Login",font=("verdana",10),bg="#ed7300",fg="white",relief="raised",command=login_verify,width=12)
Login_btn.place(x=273,y=528)                                                     #ENTER LOGIN WINDOW
Login_btn.bind("<Enter>",ent1login)
Login_btn.bind("<Leave>",leftLogin)

root.mainloop()     #================PROGRAM ENDS