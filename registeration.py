from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox 
from PIL import ImageTk,Image
import re
win = Tk()
win.geometry("1000x1000")
win.title("Registration form")
win.configure(background= "#2563b0",relief="solid")

#------------creating menu
def quitt():
    quit() 
def abt():
    messagebox.showinfo("About","The Registration Form\nAuthor:-Utsav pandya")
def passwrd():
    if len(passwd.get()) < 6 or len(passwd.get())>10:
        messagebox.showwarning("Warning","Password should be of length 6 to 10")      
    
def eml():
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if(re.search(regex, emaill.get())):
        messagebox.showinfo("Success!","Welcome")
    else:
        messagebox.showerror("Error","Enter Valid Email address")



menu = Menu(win)
win.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="File",menu=subm1)
subm1.add_command(label="Exit",command=quitt)

subm2 = Menu(menu)
menu.add_cascade(label="Option",menu=subm2)
subm2.add_command(label="About",command=abt)


#-----------------uploading PHOTO
img = Image.open(f"D:\MyPythonFolder\image10x.jpeg")
photo = ImageTk.PhotoImage(img)
lab = Label(image=photo)
lab.pack()

#-----------------creating Labels    
l1 = Label(win,text="Registration form",relief="solid", font =("arial,bold",16),width=50,background="#eba834")
l1.place(x=470,y=200)       

l2 = Label(win,text="First Name", font=("arial,bold,16"),background="#eba834")
l2.place(x=600,y=249)

l3 = Label(win,text="Last Name", font =("arial,bold"),background="#eba834")
l3.place(x=600,y=290)

l4 = Label(win,text="DOB", font =("arial,bold,16"),background="#eba834")
l4.place(x=600,y=331)

l5 = Label(win,text="Country", font = ("arial,bold,16"),background="#eba834")
l5.place(x=600,y=370)

l6 = Label(win,text="Programming Lang", font = ("arial,bold,16"),background="#eba834")
l6.place(x=600,y=410)

l7 = Label(win,text="Gender", font = ("arial,bold,16"),background="#eba834")
l7.place(x=600,y=450)

l10 = Label(win,text="Password", font = ("arial,bold,16"),background="#eba834")
l10.place(x=600,y=490)

l11 = Label(win,text="Email", font = ("arial,bold,16"),background="#eba834")
l11.place(x=600,y=530)
#--------------------creating Entry Button
fn=StringVar()
ln=StringVar()
dob=StringVar()
passwd=StringVar()
emaill=StringVar()


Ent2 = Entry(win,width=20,textvariable=fn,background="#eba834")
Ent2.place(x=800,y=255)

Ent3 = Entry(win,width=20,textvariable=ln,background="#eba834")
Ent3.place(x=800,y=295)

Ent4 = Entry(win,width=20,textvariable=dob,background="#eba834")
Ent4.place(x=800,y=335)

Ent10 = Entry(win,width=20,textvariable=passwd,background="#eba834")
Ent10.place(x=800,y=495)

Ent11 = Entry(win,width=20,textvariable=emaill,background="#eba834")
Ent11.place(x=800,y=535)

#---------------------combobox
var = StringVar()
c_n = ["India","Nepal","China"]
droplist = OptionMenu(win,var,*c_n,)
var.set("Select country")

droplist.configure(width=20,background="#eba834")
droplist.place(x=800,y=370)

#-----------------creating checkbox
var_c1 = BooleanVar()
c1 = Checkbutton(win,text="Java",command=var_c1,background="#eba834")
c1.place(x=800,y=410)

var_c2 = BooleanVar()
c2 = Checkbutton(win,text="Python",command=var_c2,background="#eba834")
c2.place(x=860,y=410)

"""def lang():
    if var_c1==1:
        print("Your Programming Language is Java")
    if var_c2==1:
        print("Your Programming Language is Python")"""

#--------------------radio buttons
r1 = Radiobutton(win,text="Male",value="m",background="#eba834").place(x=800,y=450)
r2 = Radiobutton(win,text="Female",value="f",background="#eba834").place(x=850,y=450)
r3 = Radiobutton(win,text="Other",value="o",background="#eba834").place(x=920,y=450)

#--------------------creating Buttons
def printt():
    firstname = fn.get()
    lastname = ln.get()
    dob1 = dob.get()
    var1 = var.get()
    
    print(f"Your name is {firstname} {lastname}")
    print(f"Your Date of Birth is {dob1}")
    print(f"Your Country is {var1}")
    if var_c1.get()==False:
        print("Your Programming Language is Java")
    if var_c2.get()==False:
        print("Your Programming Language is Python")
    print(f"passward:{passwd.get()}")
    print(f"email:{emaill.get()}")    


    #--------File handling


    f = open("abc.txt","a")
    f.write(f"Your name is {firstname} {lastname}""\n"
    f"Your Date of Birth is {dob1}""\n"
    f"Your Country is {var1}""\n"
    
    f"{passwd.get()}""\n"
    f"{emaill.get()}")
    
    exit()    
def signupp():
    passwrd()
    eml()
    
btn1 = Button(win,text="Login",fg="#12084d",background="#eba834", font = ("arial,bold,16"),command=printt,width=10).place(x=600,y=700)
btn2 = Button(win,text="Quit",fg="#12084d",background="#eba834", font = ("arial,bold,16"),command=quitt,width=10).place(x=830,y=700)
btn2 = Button(win,text="Signup",fg="#12084d",background="#eba834", font =("arial,bold,16"),command=signupp,width=10).place(x=720,y=700)
img = Image.open(f"D:\MyPythonFolder\download (1).jpg") 
photo11 = ImageTk.PhotoImage(img)
b20 = Button(win,text="button",highlightbackground="red",justify="left",image=photo11,height=50,width=150,relief=SOLID).place(x=730,y=610)

win.mainloop()