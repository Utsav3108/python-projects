from mysql.connector import *

mydb = connect(host="localhost",user="root",passwd="123456789",database="utsavdb")
mycursor = mydb.cursor()
ved = "shreya"
sql = f"SELECT * FROM Login WHERE Firstname='{ved}' "

mycursor.execute(sql)

data = mycursor.fetchone()

print(data[4])
