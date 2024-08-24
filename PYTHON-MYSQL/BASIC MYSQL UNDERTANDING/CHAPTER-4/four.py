import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="haseeb725",
  database = "db1"
)

my_cursor = mydb.cursor()

my_data  = "insert into book (book_id,title,price) values(%s,%s,%s)"
my_value = [(2,"php",54.3),(3,"java",23),(4,"HTML",99),(5,"Sql",33)]

my_execute = my_cursor.executemany(my_data,my_value)

mydb.commit()
