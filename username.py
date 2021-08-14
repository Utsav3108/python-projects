from mysql.connector import *

mydb = connect(host="localhost",user="root",passwd="123456789",database="utsavdb")
mycursor = mydb.cursor()
sql = f"SELECT * FROM Login WHERE Firstname='utsav' "   #{fn.get()}
mycursor.execute(sql)
data = mycursor.fetchone()
if data==None:
    print("New User!")
else :
    print("User Exist")
    
