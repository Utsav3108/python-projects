from tkinter import *                  #===========PROGRAM BEGINS
from tkinter import messagebox,ttk
import numpy
from mysql.connector import *
from tkinter import messagebox           #====IMPORTING REQUIRED FILES
class site:
    def __init__(self,home):
        self.home=home                   #=====INITIALISATION OF HOME SCREEN
        self.home.geometry("1550x800+0+0")
        self.home.title("Home")
        self.home.config(bg="white")

        
        
        schoolname = Label(self.home,text="Arpan English Medium School",font=("Century Gothic",60),bg="#00c489",fg="white").pack(fill=BOTH)
        qoutelabel = Label(self.home,text='"You Should do Hardwork for Success" \n-George bell',bg="white",fg="black",font=("Monotype Corsiva",50)).place(x=250,y=300)
        aboutusbtn = Button(self.home,text="About-us",command=self.aboutus,width=10,relief=RAISED,font=("calibri",30),bg="#00c489",fg="white").place(x=425,y=600)
        quitbtn = Button(self.home,text="Quit",command=quit,relief=RAISED,width=10,font=("calibri",30),bg="#00c489",fg="white").place(x=767,y=600)
        addstdbtn = Button(self.home,text="Add Student",command=self.dd,relief=RAISED,font=("calibri",30),bg="#00c489",fg="white").place(x=100,y=600)
        stdinfobtn = Button(self.home,text="Student Info",command=self.stdent_info,relief=RAISED,font=("calibri",30),bg="#00c489",fg="white").place(x=1150,y=600)
        
    def aboutus(self):                         #=====ABOUT-US WINDOW
        self.abtus = Tk()
        self.abtus.geometry("1550x900+0+0")
        self.abtus.title("About us")
        self.abtus.config(bg="white")
        schoolname = Label(self.abtus,text="About us",font=("Century Gothic",60),bg="#00c489",fg="white").pack(fill=BOTH)
        Note = "Arpan English Medium School is an English and Gujarati Medium School.\nHere, Every Teacher, who have 5year+ Experience in teaching field,\ngives there best to make students understand each and every concepts.  "
        notelabel = Label(self.abtus,text=Note,font=("Century Gothic",30),bg="white",fg="#00c489").pack()

        devlabel = Label(self.abtus,text="Developer's Detaills",font=("Verdana",25),width=75,anchor=CENTER,fg="white",bg="#00c489").place(x=0,y=300)
        devname = Label(self.abtus,text="Name:",font=("Century Gothic",30),bg="white",fg="#00c489").place(x=480,y=350)
        devname2 = Label(self.abtus,text="Qualification:",font=("Century Gothic",30),bg="white",fg="#00c489").place(x=480,y=420)
        devname3 = Label(self.abtus,text="Colloge:",font=("Century Gothic",30),bg="white",fg="#00c489").place(x=480,y=490)
        devname4 = Label(self.abtus,text="Mail ID:",font=("Century Gothic",30),bg="white",fg="#00c489").place(x=480,y=560)
        devname5 = Label(self.abtus,text="Phone No.:",font=("Century Gothic",30),bg="white",fg="#00c489").place(x=480,y=630)

        devname0 = Label(self.abtus,text="Pandya Utsav Hitendrabhai",font=("Century Gothic",30),bg="white",fg="#00c489").place(x=780,y=350)
        devname6 = Label(self.abtus,text="IT Eng. Sem-2",font=("Century Gothic",30),bg="white",fg="#00c489").place(x=780,y=420)
        devname7 = Label(self.abtus,text="Gec, Modasa",font=("Century Gothic",30),bg="white",fg="#00c489").place(x=780,y=490)
        devname8 = Label(self.abtus,text="utsavpandya@gmail.com",font=("Century Gothic",30),bg="white",fg="#00c489").place(x=780,y=560)
        devname9 = Label(self.abtus,text="9568884265",font=("Century Gothic",30),bg="white",fg="#00c489").place(x=780,y=630)
        

        self.abtus.mainloop()               #======ABOUT-US WINDOW ENDS

    def stdent_info(self):                   
        self.student_info = Tk()            #=====STUDENT-INFO WINDOW
        self.student_info.geometry("1540x900+0+0")
        self.student_info.title("Student Info")
        self.student_info.config(bg="white")

        mydb = connect(host="localhost",user="root",password="123456",database="utsavdb")
        mycursor = mydb.cursor()
        query = "SELECT * FROM dbms"        #======FETCHING ALL DATA FROM DATABASE
        mycursor.execute(query)
        data = mycursor.fetchall()

        print(data)                 #====PRINTING ALL DATA

        resultboard = Label(self.student_info,text="Student-Info",font=("Century Gothic",35),bg="#00c489",fg="white").pack(fill=BOTH)

        searchlabel = Label(self.student_info,text="Search by Rollno.",font=("Century Gothic",25),bg="#00c489",fg="white").place(x=260,y=70)
        self.searchEntry = Entry(self.student_info,font=("Century Gothic",25),bg="white",fg="#00c489")
        self.searchEntry.place(x=560,y=70,width=250)
        

        stdLabel = Label(self.student_info,text="Standard:",font=("verdana",25),fg="#00c489",bg="white").place(x=20,y=480)

        math1Label = Label(self.student_info,text="Math-1:",font=("verdana",25),fg="#00c489",bg="white").place(x=20,y=530)

        eng1Label = Label(self.student_info,text="English-1:",font=("verdana",25),fg="#00c489",bg="white").place(x=20,y=580)

        hindi1Label = Label(self.student_info,text="Hindi-1:",font=("verdana",25),fg="#00c489",bg="white").place(x=20,y=630)

        ss1Label = Label(self.student_info,text="Socialscience-1:",font=("verdana",25),fg="#00c489",bg="white").place(x=20,y=680)

        sci1Label = Label(self.student_info,text="Science-1:",font=("verdana",25),fg="#00c489",bg="white").place(x=20,y=730)

        math2Label = Label(self.student_info,text="Math-2:",font=("verdana",25),fg="#00c489",bg="white").place(x=520,y=530)

        eng2Label = Label(self.student_info,text="English-2:",font=("verdana",25),fg="#00c489",bg="white").place(x=520,y=580)

        hindi2Label = Label(self.student_info,text="Hindi-2:",font=("verdana",25),fg="#00c489",bg="white").place(x=520,y=630)

        ss2Label = Label(self.student_info,text="Socialscience-2:",font=("verdana",25),fg="#00c489",bg="white").place(x=520,y=680)

        sci2Label = Label(self.student_info,text="Science-2:",font=("verdana",25),fg="#00c489",bg="white").place(x=520,y=730)

        sem1TLabel = Label(self.student_info,text="Sem-1Totalmarks:",font=("verdana",25),fg="#00c489",bg="white").place(x=1020,y=530)

        sem1perLabel = Label(self.student_info,text="Sem-1Per(%):",font=("verdana",25),fg="#00c489",bg="white").place(x=1020,y=580)

        sem2TLabel = Label(self.student_info,text="Sem-2Totalmarks:",font=("verdana",25),fg="#00c489",bg="white").place(x=1020,y=630)

        sem2perLabel = Label(self.student_info,text="Sem-2Per(%):",font=("verdana",25),fg="#00c489",bg="white").place(x=1020,y=680)

        gradelabel = Label(self.student_info,text="Grade:",font=("verdana",25),fg="#00c489",bg="white").place(x=1020,y=730)
        
        def go():        #==========DEFINING GO FUNCTION
            print("GET ROLLNO.",self.searchEntry.get())
            query1 = f"SELECT * FROM dbms WHERE Roll_no = '{self.searchEntry.get()}'"
            mycursor.execute(query1)
            data2 = mycursor.fetchone()
            if data2 is None:              #=====VALIDATING      
                messagebox.showerror("Error","Student Not Found!",parent=self.student_info)
            else :
                namelabel = Label(self.student_info,text=f"{data2[0]}'s Report Card",font=("Verdana",25),width=75,anchor=CENTER,fg="white",bg="#00c489").place(x=0,y=430)
                print("===========================================")
                print(data2)
                print("===========================================")
                                              #================SHOWING ALL USER DATA ON WINDOW
                std3Label = Label(self.student_info,text=f"{data2[2]}",font=("century gothic",22),fg="white",bg="#00c489").place(x=300,y=480,width=150)

                math3Label = Label(self.student_info,text=f"{data2[3]}",font=("century gothic",22),fg="white",bg="#00c489").place(x=300,y=530,width=150)

                eng3Label = Label(self.student_info,text=f"{data2[4]}",font=("century gothic",22),fg="white",bg="#00c489").place(x=300,y=580,width=150)

                hindi3Label = Label(self.student_info,text=f"{data2[5]}",font=("century gothic",22),fg="white",bg="#00c489").place(x=300,y=630,width=150)

                ss3Label = Label(self.student_info,text=f"{data2[6]}",font=("century gothic",22),fg="white",bg="#00c489").place(x=300,y=680,width=150)

                sci3Label = Label(self.student_info,text=f"{data2[7]}",font=("century gothic",22),fg="white",bg="#00c489").place(x=300,y=730,width=150)

                math4Label = Label(self.student_info,text=f"{data2[8]}",font=("century gothic",22),fg="white",bg="#00c489").place(x=800,y=530,width=150)

                eng4Label = Label(self.student_info,text=f"{data2[9]}",font=("century gothic",22),fg="white",bg="#00c489").place(x=800,y=580,width=150)

                hindi4Label = Label(self.student_info,text=f"{data2[10]}",font=("century gothic",22),fg="white",bg="#00c489").place(x=800,y=630,width=150)

                ss4Label = Label(self.student_info,text=f"{data2[11]}",font=("century gothic",22),fg="white",bg="#00c489").place(x=800,y=680,width=150)

                sci4Label = Label(self.student_info,text=f"{data2[12]}",font=("century gothic",22),fg="white",bg="#00c489").place(x=800,y=730,width=150)

                s1T4Label = Label(self.student_info,text=f"{data2[13]}/350",font=("century gothic",22),fg="white",bg="#00c489").place(x=1340,y=530,width=150)

                s1per4Label = Label(self.student_info,text=f"{data2[15]}",font=("century gothic",22),fg="white",bg="#00c489").place(x=1340,y=580,width=150)

                s2T4Label = Label(self.student_info,text=f"{data2[14]}/350",font=("century gothic",22),fg="white",bg="#00c489").place(x=1340,y=630,width=150)

                s2per4Label = Label(self.student_info,text=f"{data2[16]}",font=("century gothic",22),fg="white",bg="#00c489").place(x=1340,y=680,width=150)

                grade4Label = Label(self.student_info,text=f"{data2[17]}",font=("century gothic",22),fg="white",bg="#00c489").place(x=1340,y=730,width=150)
                                               #=====GO BUTTON==============
        Gobtn = Button(self.student_info,text="Go",command=go,width=10,bg="#00c489",fg="white",font=("Century Gothic",17)).place(x=840,y=70)

       
        


                    #=========================TREEVIEW FOR TABLE OF DATA============================
        my_tree = ttk.Treeview(self.student_info)
        my_tree['column'] = ("Name","Rollno.","Standard","Maths1","English1","Hindi1","Social-science1","Science1","Maths2","English2","Hindi2","Social-science2","Science2","s1_total","s2_total","s1_per(%)","s2_per(%)","Grade")

        my_tree.column("#0",width=0,stretch=NO,)          #=======NAMING COLUMNS STARTS
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
        my_tree.column("Grade",anchor=W,width=60)               #=======NAMING COLUMNS ENDS


        my_tree.heading("#0",text="Label",anchor=W)             #=======HEADINGS OF COLUMNS BEGINS
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
        my_tree.heading("Grade",text="Grade",anchor=W)               #=========HEADINGS OF COLUMNS ENDS

        count = 0
        for record in data:                           #===========INSERING ALL DATA INTO TABLE
            my_tree.insert(parent='',index=END,iid=count,text="1.",values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15],record[16],record[17]))
            count += 1
        my_tree.place(x=0,y=130,height=300,width=1540)

        self.student_info.mainloop()
        
    def dd(self):
        self.addstd = Tk()
        self.addstd.geometry("1500x900")
        self.addstd.title("Add Student")
        self.addstd.config(bg="white")
        addst = Label(self.addstd,text="Add Student",font=("Century Gothic",45),bg="#00c489",fg="white").pack(fill=BOTH)
        
        vcmd = (self.addstd.register(self.validate),  #=========VALIDATION FOR ONLY INTEGER AND FLOAT TO BE WRITTEN
                    '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        
        namelabel = Label(self.addstd,text="Name",font=("Verdana",25),fg="#00c489",bg="white").place(x=400,y=100)
        self.nameentry = Entry(self.addstd,font=("Verdana",12),fg="#00c489",bg="white")
        self.nameentry.place(x=510,y=110,height=26)
        self.nameentry.focus()
        
        stdlabel = Label(self.addstd,text="Std",font=("Verdana",25),fg="#00c489",bg="white").place(x=400,y=170)
        self.stdentry = Entry(self.addstd,font=("Verdana",12),fg="#00c489",bg="white",relief=SUNKEN)
        self.stdentry.place(x=510,y=180,height=26)
        

        rollnolabel = Label(self.addstd,text="Rollno.",font=("Verdana",25),fg="#00c489",bg="white").place(x=900,y=100)
        self.rollnoentry = Entry(self.addstd,font=("Verdana",12),fg="#00c489",bg="white",validate='key',validatecommand=vcmd)
        self.rollnoentry.place(x=1020,y=110,height=26)

        sem1label = Label(self.addstd,text="Sem1",font=("Century Gothic",30),width=22,bg="#00c489",fg="white")
        sem1label.place(x=20,y=250)

        mathlabel = Label(self.addstd,text="Maths",font=("Verdana",25),fg="#00c489",bg="white").place(x=20,y=320)
        englabel = Label(self.addstd,text="English",font=("Verdana",25),fg="#00c489",bg="white").place(x=20,y=400)
        scilabel = Label(self.addstd,text="Science",font=("Verdana",25),fg="#00c489",bg="white").place(x=20,y=480)
        sslabel = Label(self.addstd,text="Social-Science",font=("Verdana",25),fg="#00c489",bg="white").place(x=20,y=560)
        hindilabel = Label(self.addstd,text="Hindi",font=("Verdana",25),fg="#00c489",bg="white").place(x=20,y=640)

        self.mathentry = Entry(self.addstd,font=("Verdana",15),fg="#00c489",bg="white",validate='key',validatecommand=vcmd)
        self.mathentry.place(x=280,y=327)
        self.engentry = Entry(self.addstd,font=("Verdana",15),fg="#00c489",bg="white",validate='key',validatecommand=vcmd)
        self.engentry.place(x=280,y=407)
        self.scientry = Entry(self.addstd,font=("Verdana",15),fg="#00c489",bg="white",validate='key',validatecommand=vcmd)
        self.scientry.place(x=280,y=487)
        self.ssentry = Entry(self.addstd,font=("Verdana",15),fg="#00c489",bg="white",validate='key',validatecommand=vcmd)
        self.ssentry.place(x=280,y=567)
        self.hindientry = Entry(self.addstd,font=("Verdana",15),fg="#00c489",bg="white",validate='key',validatecommand=vcmd)
        self.hindientry.place(x=280,y=647)

        sem1label1 = Label(self.addstd,text="Sem2",font=("Century Gothic",30),width=22,bg="#00c489",fg="white")
        sem1label1.place(x=960,y=250)

        mathlabel1 = Label(self.addstd,text="Maths",font=("Verdana",25),fg="#00c489",bg="white").place(x=960,y=320)
        englabel1= Label(self.addstd,text="English",font=("Verdana",25),fg="#00c489",bg="white").place(x=960,y=400)
        scilabel1 = Label(self.addstd,text="Science",font=("Verdana",25),fg="#00c489",bg="white").place(x=960,y=480)
        sslabel1 = Label(self.addstd,text="Social-Science",font=("Verdana",25),fg="#00c489",bg="white").place(x=960,y=560)
        hindilabel1 = Label(self.addstd,text="Hindi",font=("Verdana",25),fg="#00c489",bg="white").place(x=960,y=640)

        self.mathentry1 = Entry(self.addstd,font=("Verdana",15),fg="#00c489",bg="white",validate='key',validatecommand=vcmd)
        self.mathentry1.place(x=1220,y=327)
        self.engentry1 = Entry(self.addstd,font=("Verdana",15),fg="#00c489",bg="white",validate='key',validatecommand=vcmd)
        self.engentry1.place(x=1220,y=407)
        self.scientry1 = Entry(self.addstd,font=("Verdana",15),fg="#00c489",bg="white",validate='key',validatecommand=vcmd)
        self.scientry1.place(x=1220,y=487)
        self.ssentry1 = Entry(self.addstd,font=("Verdana",15),fg="#00c489",bg="white",validate='key',validatecommand=vcmd)
        self.ssentry1.place(x=1220,y=567)
        self.hindientry1 = Entry(self.addstd,font=("Verdana",15),fg="#00c489",bg="white",validate='key',validatecommand=vcmd)
        self.hindientry1.place(x=1220,y=647)

        total = Label(self.addstd,text="S1 Total",font=("Century Gothic",25),width=8,fg="white",bg="#00c489").place(x=580,y=320)
        pertagelabel = Label(self.addstd,text="S1 Per(%)",font=("Century Gothic",25),width=8,fg="white",bg="#00c489").place(x=580,y=370)

        total1 = Label(self.addstd,text="S2 Total",font=("Century Gothic",25),width=8,fg="white",bg="#00c489").place(x=580,y=420)
        pertagelabel1 = Label(self.addstd,text="S2 Per(%)",font=("Century Gothic",25),width=8,fg="white",bg="#00c489").place(x=580,y=470)

        gradelabel1 = Label(self.addstd,text="Grade",font=("Century Gothic",25),width=8,fg="white",bg="#00c489").place(x=580,y=520)
        
        def calculate(): #======FUNCTION FOR CALCULATING ALL THE MARKS AND TO GIVE GRADES UPON PERCENTAGE
            if self.nameentry.get()=="" or self.rollnoentry.get()=="" or self.stdentry.get()=="" or self.mathentry.get()=="" or self.engentry.get()=="" or self.scientry.get()=="" or self.ssentry.get()=="" or self.hindientry.get()=="" or self.mathentry1.get()=="" or self.hindientry1.get()=="" or self.ssentry1.get()=="" or self.engentry1.get()=="" or self.scientry1.get()=="": 
                messagebox.showerror("Error","All Fields are Required!",parent=self.addstd)
            
            else:
                mydb = connect(host="localhost",user="root",password="123456",database="utsavdb")
                mycursor = mydb.cursor()
                query1 = f"SELECT * FROM dbms WHERE Roll_no = '{self.rollnoentry.get()}'"
                mycursor.execute(query1)
                data2 = mycursor.fetchone()
                print(data2)
                if data2 is not None:    #======VALIDATION
                    messagebox.showerror("Error","Student Exist\nUse Another Rollno.!",parent=self.addstd) 
                else:
                    a=float(self.mathentry.get())       #======GETTING ALL THE VALUES
                    b=float(self.engentry.get())
                    c=float(self.scientry.get())
                    d=float(self.ssentry.get())
                    e=float(self.hindientry.get())

                    a1=float(self.mathentry1.get())
                    b1=float(self.engentry1.get())
                    c1=float(self.scientry1.get())
                    d1=float(self.ssentry1.get())
                    e1=float(self.hindientry1.get())

                    print("markget",a,b,c,d,e)
                    
                    markget = [a,b,c,d,e]
                    markget1 = [a1,b1,c1,d1,e1]

                    totalmarks1 = numpy.array(markget)
                    sum_totalmarks1 = totalmarks1.sum()   #===========SUMATION OF ALL MARKS OF SEM-1
                    print("sum of marks",sum_totalmarks1)

                    per1 = (sum_totalmarks1/350.0)*100
                    for_per1 = "{:.1f}".format(per1)      #===========PERCENTAGE OF SEM-1

                    totalmarks2 = numpy.array(markget1)  
                    sum_totalmarks2 = totalmarks2.sum()     #===========SUMATION OF ALL MARKS OF SEM-2
                    print("sum of marks2:",sum_totalmarks2)

                    per2 = (sum_totalmarks2/350)*100
                    for_per2 = "{:.1f}".format(per2)         #===========PERCENTAGE OF SEM-2
                    
                    tot = Label(self.addstd,text=f"{sum_totalmarks1}/350",font=("Verdana",25),fg="#00c489",bg="white").place(x=780,y=320,width=170)
                    perL = Label(self.addstd,text=f"{for_per1}%",font=("Verdana",25),fg="#00c489",bg="white").place(x=780,y=370,width=130)

                    tot1 = Label(self.addstd,text=f"{sum_totalmarks2}/350",font=("Verdana",25),fg="#00c489",bg="white").place(x=780,y=420,width=170)
                    perL1 = Label(self.addstd,text=f"{for_per2}%",font=("Verdana",25),fg="#00c489",bg="white").place(x=780,y=470,width=130)            


                    a2 = int(float(for_per2))
                    print("a2:",a2)              
                    if a2==100:                        #======ASSIGNING GRADE OF STUDENT
                        a3 = "A++"
                        aab = Label(self.addstd,text="A++",font=("Verdana",25),fg="#00c489",bg="white")
                        aab.place(x=800,y=520,width=75)
                    elif a2 in range(90,100):
                        a3 = "A+"
                        aab = Label(self.addstd,text="A+",font=("Verdana",25),fg="#00c489",bg="white")
                        aab.place(x=800,y=520,width=75)
                    elif a2 in range(80,90):
                        a3 = "A"
                        aab = Label(self.addstd,text="A",font=("Verdana",25),fg="#00c489",bg="white")
                        aab.place(x=800,y=520,width=75)
                    elif a2 in range(70,80):
                        a3 = "B++"
                        aab = Label(self.addstd,text="B++",font=("Verdana",25),fg="#00c489",bg="white")
                        aab.place(x=800,y=520,width=75)    
                    elif a2 in range(60,70):
                        a3 = "B+"
                        aab = Label(self.addstd,text="B+",font=("Verdana",25),fg="#00c489",bg="white")
                        aab.place(x=800,y=520,width=75)
                    elif a2 in range(50,60):
                        a3 = "B"
                        aab = Label(self.addstd,text="B",font=("Verdana",25),fg="#00c489",bg="white")
                        aab.place(x=800,y=520,width=75)
                    elif a2 in range(40,50):
                        a3 = "C+"
                        aab = Label(self.addstd,text="C+",font=("Verdana",25),fg="#00c489",bg="white")
                        aab.place(x=800,y=520,width=75)
                    elif a2 in range(33,40):
                        a3 = "C"
                        aab = Label(self.addstd,text="C",font=("Verdana",25),fg="#00c489",bg="white")
                        aab.place(x=800,y=520,width=75)
                    else :
                        a3 = "Fail"
                        aab = Label(self.addstd,text="Fail",font=("Verdana",25),fg="#00c489",bg="white")
                        aab.place(x=800,y=520,width=75)
                    print("status",a3)
        def save():                  #=======SAVING WHOLE DATA TO DATABASE

            mydb = connect(host="localhost",user="root",password="123456",database="utsavdb")
            mycursor = mydb.cursor()
            query1 = f"SELECT * FROM dbms WHERE Roll_no = '{self.rollnoentry.get()}'"
            mycursor.execute(query1)
            data2 = mycursor.fetchone()
            print(data2)
            

            if self.nameentry.get()=="" or self.rollnoentry.get()=="" or self.stdentry.get()=="" or self.mathentry.get()=="" or self.engentry.get()=="" or self.scientry.get()=="" or self.ssentry.get()=="" or self.hindientry.get()=="" or self.mathentry1.get()=="" or self.hindientry1.get()=="" or self.ssentry1.get()=="" or self.engentry1.get()=="" or self.scientry1.get()=="": 
                messagebox.showerror("Error","All Fields are Required!",parent=self.addstd)
            elif data2 is not None:      #=============RESTRICTING USER FROM SAVING SAME STUDENT INTO DATABASE
                messagebox.showerror("Error","Student Exist\nUse Another Rollno.!",parent=self.addstd)
            else:
                rollno = self.rollnoentry.get()
                name = self.nameentry.get()
                std = self.stdentry.get()
                
                print("======================================================================")
                print("roll:",rollno)
                print("name",name)
                print("std",std)
                mydb = connect(host="localhost",user="root",passwd="123456",database="utsavdb")
                mycursor = mydb.cursor()
                a=float(self.mathentry.get())
                b=float(self.engentry.get())
                c=float(self.scientry.get())
                d=float(self.ssentry.get())
                e=float(self.hindientry.get())

                a1=float(self.mathentry1.get())
                b1=float(self.engentry1.get())
                c1=float(self.scientry1.get())
                d1=float(self.ssentry1.get())
                e1=float(self.hindientry1.get())

                print("Maths1:",a)
                print("English1:",b)
                print("Science1:",c)
                print("Social1:",d)
                print("Hindi1:",e)

                print("Maths2:",a1)
                print("English2:",b1)
                print("Science2:",c1)
                print("Social2:",d1)
                print("Hindi2:",e1)
                
                markget = [a,b,c,d,e]
                markget1 = [a1,b1,c1,d1,e1]

                totalmarks1 = numpy.array(markget)
                sum_totalmarks1 = totalmarks1.sum()
                print("Sem1-Marks:",sum_totalmarks1)

                per1 = (sum_totalmarks1/350.0)*100
                for_per1 = "{:.1f}".format(per1)

                totalmarks2 = numpy.array(markget1)
                sum_totalmarks2 = totalmarks2.sum()
                print("Sem2-Marks:",sum_totalmarks2)

                per2 = (sum_totalmarks2/350)*100
                for_per2 = "{:.1f}".format(per2)
                print(f"Percentage{for_per1}%")
                print(f"Percentage{for_per2}%")
                a2 = int(float(for_per2))
                print("a2:",a2)
                if a2==100:
                    a3 = "A++"
                elif 90<a2<=99:
                    a3 = "A+"
                elif 80<a2<=90:
                    a3 = "A"
                elif 70<a2<=80:
                    a3 = "B++"
                elif 60<a2<=70:
                    a3 = "B+"
                elif 50<a2<=60:
                    a3 = "B"
                elif 40<a2<=50:
                    a3 = "C+"
                elif 33<a2<40:
                    a3 = "C"
                else :
                    a3 = "Fail"
                    
                print("status",a3)

                query = "INSERT into dbms(name,Roll_no,Standard,maths_sem1,english_sem1,hindi_sem1,ss_sem1,science_sem1,maths_sem2,english_sem2,hindi_sem2,ss_sem2,science_sem2,s1_total,s2_total,s1_per,s2_per,grade) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = [(name,rollno,std,a,b,e,d,c,a1,b1,e1,d1,c1,sum_totalmarks1,sum_totalmarks2,f"{for_per1}%",f"{for_per2}%",a3)]
                mycursor.executemany(query,val)
                mydb.commit()
                mydb.close()

                messagebox.showinfo("Success","Data Saved Successfully!",parent=self.addstd)
                print("======================================================================")
        
        calcbtn = Button(self.addstd,text="Calculate",command=calculate,width=10,bg="#00c489",fg="white",font=("Century Gothic",20)).place(x=550,y=700)
        savebtn = Button(self.addstd,text="Save",command=save,width=10,bg="#00c489",fg="white",font=("Century Gothic",20)).place(x=750,y=700)
        self.addstd.mainloop()
    def validate(self, action, index, value_if_allowed,
                        prior_value, text, validation_type, trigger_type, widget_name):
            if value_if_allowed:
                try:                          #=======VALIDATE FUNCTION FOR STRING RESTRICTION
                    float(value_if_allowed)
                    return True
                except ValueError:
                    return False
            elif value_if_allowed is "":
                return True
            else:
                return False

home=Tk()
obj = site(home)
home.mainloop()           #========PROGRAM ENDS
