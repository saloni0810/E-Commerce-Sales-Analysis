import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Siddhartha@01",auth_plugin='mysql_native_password')

myCursor = mydb.cursor()

myCursor.execute("show databases")

for i in myCursor:
    print(i)

