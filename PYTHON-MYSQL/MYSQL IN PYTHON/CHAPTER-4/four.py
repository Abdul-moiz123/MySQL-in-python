#PRINT THE RECORD IN THE TABLE 
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "practicedb"
)

my_cursor = mydb.cursor()
my_query = "SELECT * FROM users"
my_cursor.execute(my_query)
my_result = my_cursor.fetchall()
for x in my_result:
    print(x)


#PRINT THE ONE PARTICULAR COLUMN FROM THE RECORD IN THE TABLE 
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "practicedb"
)

my_cursor = mydb.cursor()
my_query = "SELECT name from users"
my_cursor.execute(my_query)
my_result = my_cursor.fetchall()
for x in my_result:
    print(x)


# IF YOU WANT THE FIRST ROW OF THE TABLE ONLY
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "practicedb"
)

my_cursor = mydb.cursor()
my_query = "SELECT * from users"
my_cursor.execute(my_query)
my_result = my_cursor.fetchone()
print(my_result)
