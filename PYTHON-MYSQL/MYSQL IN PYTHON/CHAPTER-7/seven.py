# DELETE RECORD FROM THE TABLE
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "practicedb"
)

my_cursor = mydb.cursor()
my_query = "DELETE FROM USERS WHERE ADDRESS='KARACHI'"
my_cursor.execute(my_query)
mydb.commit()


# DELETE ALL RECORD FROM THE TABLE
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "practicedb"
)

my_cursor = mydb.cursor()
my_query = "DELETE FROM USERS"
my_cursor.execute(my_query)
mydb.commit()


# PREVENT SQL INJECTION
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "practicedb"
)

my_cursor = mydb.cursor()
my_query = "DELETE FROM USERS WHERE ADDRESS='%s'"
my_value = ("karachi",)
my_cursor.execute(my_query,my_value)
mydb.commit()
