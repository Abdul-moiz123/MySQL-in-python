# LIMIT TO PRINT THE RECORD IN THE TABLE
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "practicedb"
)

my_cursor = mydb.cursor()
my_query = ("select * from users limit 1")
my_cursor.execute(my_query)
my_result = my_cursor.fetchall()

for a in my_result:
    print(a)


# LIMIT TO PRINT THE RECORD IN THE TABLE WITH THE PARTICULAR POSITION
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "practicedb"
)

my_cursor = mydb.cursor()
my_query = ("select * from users limit 2 offset 2")
my_cursor.execute(my_query)
my_result = my_cursor.fetchall()

for a in my_result:
    print(a)    