from mysql.connector import *

resetscreen = Tk()
User = self.Entre.get()
mydb = connect(host="localhost",user="root",passwd="123456789",database="utsavdb")
mycursor = mydb.cursor()
sql = f"SELECT * FROM Login WHERE Firstname='{User}'"
mycursor.execute(sql)
data = mycursor.fetchone()
print(data[2])
resetlab = Label(resetscreen,text="Reset Password",font=("Calibri,bold",20),bg="black",fg="white").pack()
emaillabel = Label(resetscreen,text="Name:",font=("Calibri,bold",20)).pack()
strr = StringVar()
emailent = Entry(resetscreen,width=30,textvariable=strr).pack()

print(strr.get())
if strr.get()==data[2]:
    passlabel = Label(resetscreen,text="Name:",font=("Calibri,bold",20)).pack()
    strrr = StringVar()
    passent = Entry(resetscreen,width=30,textvariable=strrr).pack()
    print(strrr.get())
    updatequery = f"UPDATE login SET password = '{strrr.get()}',  WHERE email = '{strr.get()}'"
    mycursor.execute(updatequery)
    mydb.commit()
    mydb.close()
else :
    messagebox.showerror("Error","Enter Correct Email")
btn = Button(resetscreen,text="Close",command=close()).pack()    
resetscreen.mainloop()
