import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="haseeb725",
    database="db1"
)

my_cursor = mydb.cursor()

s = "DELETE FROM book WHERE title='python3'" 

my_cursor.execute(s)

mydb.commit()