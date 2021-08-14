from tkinter import *
from tkinter import ttk
from mysql.connector import *

mydb = connect(host="localhost",user="root",password="123456789",database="utsavdb")
mycursor = mydb.cursor()
query = "SELECT * FROM sdbms"
mycursor.execute(query)
dataa = mycursor.fetchall()
print(dataa)





student_info = Tk()
student_info.geometry("1540x900+0+0")
student_info.title("Student Info")
student_info.config(bg="white")
resultboard = Label(student_info,text="Student-Info",font=("Century Gothic",35),bg="#00c489",fg="white").pack(fill=BOTH)

searchlabel = Label(student_info,text="Search by Rollno.",font=("Century Gothic",25),bg="#00c489",fg="white").place(x=260,y=70)
searchEntry = Entry(student_info,font=("Century Gothic",25),bg="white",fg="#00c489")
searchEntry.place(x=560,y=70)

query1 = "SELECT * FROM sdbms WHERE Roll_no = '40'"
mycursor.execute(query1)
data2 = mycursor.fetchone()
print("===========================================")
print(data2)

my_tree = ttk.Treeview(student_info)
my_tree['column'] = ("Name","Rollno.","Standard","Maths1","English1","Hindi1","Social-science1","Science1","Maths2","English2","Hindi2","Social-science2","Science2","s1_total","s2_total","s1_per(%)","s2_per(%)","Grade")

my_tree.column("#0",width=0,stretch=NO,)
my_tree.column("Name",anchor=W,width=120)
my_tree.column("Rollno.",anchor=W,width=60)
my_tree.column("Standard",anchor=W,width=60)

my_tree.column("Maths1",anchor=W,width=60)
my_tree.column("English1",anchor=W,width=60)
my_tree.column("Hindi1",anchor=W,width=60)
my_tree.column("Social-science1",anchor=W,width=70)
my_tree.column("Science1",anchor=W,width=60)

my_tree.column("Maths2",anchor=W,width=60)
my_tree.column("English2",anchor=W,width=60)
my_tree.column("Hindi2",anchor=W,width=60)
my_tree.column("Social-science2",anchor=W,width=70)
my_tree.column("Science2",anchor=W,width=60)

my_tree.column("s1_total",anchor=W,width=60)
my_tree.column("s2_total",anchor=W,width=60)
my_tree.column("s1_per(%)",anchor=W,width=60)
my_tree.column("s2_per(%)",anchor=W,width=60)
my_tree.column("Grade",anchor=W,width=60)


my_tree.heading("#0",text="Label",anchor=W)
my_tree.heading("Name",text="Name",anchor=W)
my_tree.heading("Rollno.",text="Rollno.",anchor=W)
my_tree.heading("Standard",text="Standard",anchor=W)

my_tree.heading("Maths1",text="Maths1",anchor=W)
my_tree.heading("English1",text="English1",anchor=W)
my_tree.heading("Hindi1",text="Hindi1",anchor=W)
my_tree.heading("Social-science1",text="Social-science1",anchor=W)
my_tree.heading("Science1",text="Science1",anchor=W)

my_tree.heading("Maths2",text="Maths2",anchor=W)
my_tree.heading("English2",text="English2",anchor=W)
my_tree.heading("Hindi2",text="Hindi2",anchor=W)
my_tree.heading("Social-science2",text="Social-science2",anchor=W)
my_tree.heading("Science2",text="Science2",anchor=W)

my_tree.heading("s1_total",text="Sem1-total",anchor=W)
my_tree.heading("s2_total",text="Sem2-total",anchor=W)
my_tree.heading("s1_per(%)",text="Sem1-per(%)",anchor=W)
my_tree.heading("s2_per(%)",text="Sem2-per(%)",anchor=W)
my_tree.heading("Grade",text="Grade",anchor=W)


data = (("utsav",18,"Pandya"),
("utsav",18,"Pandya"),("utsav",18,"Pandya"),("utsav",18,"Pandya"),("utsav",18,"Pandya"),("ut",18,"Pandya"))
count = 0
for record in dataa:
    my_tree.insert(parent='',index=END,iid=count,text="1.",values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15],record[16],record[17]))
    count += 1

my_tree.place(x=0,y=130,height=300,width=1540)





student_info.mainloop()