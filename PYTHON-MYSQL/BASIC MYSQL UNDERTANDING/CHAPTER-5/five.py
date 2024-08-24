import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="haseeb725",
  database = "db1"
)

my_cursor = mydb.cursor()

s = "select * from book"

my_cursor.execute(s)

result = my_cursor.fetchall()

for rec in result:
    print(rec)

