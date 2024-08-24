import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="haseeb725",
  database = "db1"
)

my_cursor = mydb.cursor()

my_table = "create table book ( book_id integer(4) , title varchar(20) , price float(5,3) )"

my_execute = my_cursor.execute(my_table)
