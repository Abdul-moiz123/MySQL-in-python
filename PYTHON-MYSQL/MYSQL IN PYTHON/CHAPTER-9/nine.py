# UPDATE THE RECORD IN THE TABLE
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "practicedb"
)

my_cursor = mydb.cursor()
my_query = ("update users set address = 'Quetta' where address='pindi'")
my_cursor.execute(my_query)
mydb.commit()


# UPDATE THE ALL RECORD IN THE TABLE
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "practicedb"
)

my_cursor = mydb.cursor()
my_query = ("update users set address = 'Quetta'")
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
my_query = ("update users set address = '%s' where address='%s'")
my_value = ("Karachi",)
my_cursor.execute(my_query,my_value)
mydb.commit()
