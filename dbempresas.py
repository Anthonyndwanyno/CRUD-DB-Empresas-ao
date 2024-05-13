import mysql.connector

dataBase= mysql.connector.connect(
    host= 'localhost',
    user='root',
    password= 'soft'
)

cursorObject= dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE dbempresas")

print("feito")