#PRINT PARTICULAR RECORD BASED ON CONDITION
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "practicedb"
)

my_cursor = mydb.cursor()
my_query = "SELECT address from users where name = 'moiz'"
my_cursor.execute(my_query)
my_result = my_cursor.fetchall()
for x in my_result:
    print(x)

# WILDCARD CHARCHTER
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "practicedb"
)

my_cursor = mydb.cursor()
my_query = "SELECT * from users where address like '%chi%'"
my_cursor.execute(my_query)
my_result = my_cursor.fetchall()
for x in my_result:
    print(x)


# PREVENT SQL INJECTION 
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "practicedb"
)

my_cursor = mydb.cursor()
my_query = "SELECT * from users where address = %s"
my_value = ("islamabad",)
my_cursor.execute(my_query,my_value)
my_result = my_cursor.fetchall()
for x in my_result:
    print(x)
