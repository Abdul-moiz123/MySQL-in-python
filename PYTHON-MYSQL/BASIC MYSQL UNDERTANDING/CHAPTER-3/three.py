import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="haseeb725",
  database = "db1"
)

my_cursor = mydb.cursor()

my_data  = "insert into book (book_id,title,price) values(%s,%s,%s)"
my_value = (1,"python3",5.3)

my_execute = my_cursor.execute(my_data,my_value)

mydb.commit()
