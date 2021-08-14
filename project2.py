from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
# passwordscreen = Tk()
# passwordscreen.geometry("400x200")
# passwordscreen.title("Password")
# passwordscreen.config(bg="white")

# Companyname = Label(passwordscreen,text="PANDYA SOFTWARE ENTERPRISE",font=("Times new roman,bold",14),fg="white",bg="black").pack(fill=BOTH)

# paslabel = Label(passwordscreen,text="Enter Password",font=("Times new roman,bold",16),bg="white").place(x=120,y=40)

# passwordEntry = Entry(passwordscreen,width=60,bg="light grey",justify=CENTER).place(x=20,y=70,height=30)


def Enter():
    # passwordscreen.destroy()
    print("welcome!")
    class main:
        def __init__(self,home):
            self.home = home
            self.home.title("Home")
            self.home.geometry("1000x1000+0+0")
            self.home.config(bg="white")

            self.bg = ImageTk.PhotoImage(file="D:\MyPythonfolder2\candle.jpg")
            bg = Label(self.home,image=self.bg)
            bg.place(x=0,y=0,width=200,height=1000)
            

            Heading = Label(self.home,text="NOTES",font=("Arial,bold",30),relief=RAISED,bg="black",fg="white",width=35,height=4)
            Heading.place(x=200,y=0)

            quote = '"You must do Hardwork to Succeed"\n-George Bell'
            QuoteLabel = Label(self.home,text=quote,font=("Ink free",25),bg="white",fg="black")
            QuoteLabel.place(x=350,y=350,width=500,height=150)

            createbtn = Button(self.home,text="Create",bd=1,font=("arial,16"),command=self.create,width=20,bg="white",fg="black")
            createbtn.place(x=300,y=700,height=50)

            Loginbtn = Button(self.home,text="Login",bd=1,font=("arial,16"),command=self.login,width=20,bg="white",fg="black")
            Loginbtn.place(x=500,y=700,height=50)

            Quitbtn = Button(self.home,text="Quit",bd=1,font=("arial,16"),command=quit,width=20,bg="white",fg="black")
            Quitbtn.place(x=700,y=700,height=50)

        def login(self):
            loginscreen = Tk()
            loginscreen.geometry("400x500")
            loginscreen.config(bg="black")
            
            Userlabel = Label(loginscreen,text="User",font=("Arial Black",27),bg="black",fg="#0080ff")
            Userlabel.place(x=140,y=50)

            UserEntry = Entry(loginscreen,font=("Calibri,bold",17),bg="white")
            UserEntry.place(x=70,y=110)

            passwordlabel = Label(loginscreen,text="Password",font=("Arial Black",27),bg="black",fg="#0080ff")
            passwordlabel.place(x=100,y=150)

            passwordEntry = Entry(loginscreen,font=("Calibri,bold",17),bg="white")
            passwordEntry.place(x=70,y=210)

            loginscreen.title("Login-Screen")
            loginscreen.mainloop()
        def create(self):
            self.note = Tk()
            self.note.geometry("1000x1000")
            self.note.title("Note")

            
            
            self.monthchoosen = ttk.Combobox(self.note, width = 27)
            
            # Adding combobox drop down list
            self.monthchoosen['values'] = (' January', 
                                    'Times new roman',
                                    'Ink free',
                                    ' April',
                                    ' May',
                                    ' June',
                                    ' July',
                                    ' August',
                                    ' September',
                                    ' October',
                                    ' November',
                                    ' December')
            
            self.monthchoosen.pack()
            self.monthchoosen.current()
            
            
            self.text = Text(self.note,font=(f"{self.monthchoosen.get()}",20),bg="black",fg="white")
            self.text.place(x=10,y=60,width=800,height=600)
            def pri():
                print(self.monthchoosen.get())
                print(self.text.get("1.0",END))
            printbtn = Button(self.note,text="Print text",command=pri).pack()
            pribtn = Button(self.note,text="Quit",command=quit).pack()
            self.note.mainloop()

            
    home = Tk()
    obj = main(home)
    home.mainloop()
Enter()
# btn = Button(passwordscreen,text="Enter",width=25,command=Enter).place(x=100,y=100)
# passwordscreen.mainloop()