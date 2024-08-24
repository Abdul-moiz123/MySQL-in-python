import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="haseeb725",
    database="db1"
)

my_cursor = mydb.cursor()

s = "UPDATE book SET price=price+10 " # update all record
s = "UPDATE book SET price=price+10 WHERE price>50" # update particular record

my_cursor.execute(s)

mydb.commit()

