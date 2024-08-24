# ORDER TO PRINT IN ASCENDING ODRDER WHICH IS BY DEFAULT
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "practicedb"
)

my_cursor = mydb.cursor()
my_query = "SELECT * from users order by address"
my_cursor.execute(my_query)
my_result = my_cursor.fetchall()
for x in my_result:
    print(x)


# ORDER TO PRINT IN DESCENDING ODRDER
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "practicedb"
)

my_cursor = mydb.cursor()
my_query = "SELECT * from users order by address desc"
my_cursor.execute(my_query)
my_result = my_cursor.fetchall()
for x in my_result:
    print(x)
