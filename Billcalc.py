from tkinter import *
from tkinter import messagebox
from mysql.connector import *
import datetime

root = Tk()
root.geometry("350x500+300+300")
root.title("Bill_Calculation")
#****************SQLdatabase********************
mydb = connect(host="localhost",user="root",passwd="123456",port='3307',database="utsavdb")
mycursor = mydb.cursor()

titlelabel = Label(root,text="*******Light and Water Bill Calculation******* ",font=("verdana,22"))
titlelabel.pack()
#*******************Label*******************
Lmlabel = Label(root,text="Enter Last Month Unit:",font=("verdana",10))
Lmlabel.place(x=60,y=30)

Tmlabel = Label(root,text="Enter This Month Unit:",font=("verdana",10))
Tmlabel.place(x=60,y=55)

Usedlabel = Label(root,text="Enter Used unit:",font=("verdana",10))
Usedlabel.place(x=60,y=80)

Lightlabel = Label(root,text="Enter this month Light bill:",font=("verdana",10))
Lightlabel.place(x=60,y=105)

Waterlabel = Label(root,text="Enter Water bill:",font=("verdana",10))
Waterlabel.place(x=60,y=130)
#******************ENTRY****************
Lm = IntVar()
LmEntry = Entry(root,textvariable=Lm,width=10)
LmEntry.place(x=250,y=30)

tm = IntVar()
tmEntry = Entry(root,textvariable=tm,width=10)
tmEntry.place(x=250,y=55)

Usedunit = IntVar()
usedunit = Entry(root,textvariable=Usedunit,width=10)
usedunit.place(x=250,y=80)

lightbill = IntVar()
lbl = Entry(root,textvariable=lightbill,width=10)
lbl.place(x=250,y=105)

waterbill = IntVar()
wbl = Entry(root,textvariable=waterbill,width=10)
wbl.place(x=250,y=130)
details = StringVar()
def clicked():
    global details
    rent_unit = eval("tm.get()-Lm.get()")

    #myunit = Used_unit - rent_unit
    myunit = Usedunit.get() - rent_unit

    #r_per_unit = Total_lightbill/Used_unit
    if Usedunit.get()==0:
        messagebox.showerror("Error","Enter Valid Used unit")
    else :
        r_per_unit = lightbill.get()/Usedunit.get()

        #rent_bill = rent_unit*r_per_unit
        rent_bill = rent_unit*r_per_unit

        #mybill = myunit*r_per_unit  
        #myunit = Used_unit - rent_unit
        #myunit =  Usedunit.get() - rent_unit 
        mybill = myunit*r_per_unit

        #Total_bill = mybill + rent_bill
        Total_bill = mybill + rent_bill

        waterb = waterbill.get()/2
    
        details.set(f"Rent Light bill :{rent_bill}\nYour Light bill:{mybill}\nWater bill:{waterb}\nTotal Light Bill(rent+yours):{Total_bill}")
        f = open("myfile.txt","a")
        f.write(f"\n-------------------------------------------\n"
        f"Rent Light bill :{rent_bill}\n"
        f"Your Light bill:{mybill}\n"
        f"Water bill:{waterb}\n"
        f"Total Light Bill(rent+yours):{Total_bill}"
        f"\n-------------------------------------------\n")


        sqlform = "Insert into bcal2(Date, Rentbill, Yourbill, Waterbill) values(%s,%s,%s,%s)"
        bilcal = [(f'{datetime.date.today()}',rent_bill,mybill,waterb)]

        mycursor.executemany(sqlform,bilcal)
        mydb.commit()


    label = Label(root,textvariable=details,relief=SOLID,font=("Times new Roman,Bold",12),width=40,border=1)
    label.place(x=0,y=250)
def enter(event):
    button.config(background="light grey")
def left(event):
    button.config(background="white")

button = Button(root,text="Calculate",width=10,command=clicked,bg="white")
button.place(x=150,y=170)
button.bind("<Enter>",enter)
button.bind("<Leave>",left)


def enterr(event):
    button1.config(background="light grey")
def leftt(event):
    button1.config(background="white")
button1 = Button(root,text="Quit",width=10,command=quit,bg="white")
button1.place(x=150,y=200)
button1.bind("<Enter>",enterr)
button1.bind("<Leave>",leftt)


root.mainloop()