# WAY TO CREATE DATABASE  
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
)

my_cursor = mydb.cursor()
my_query = ("CREATE DATABASE practicedb")
my_cursor.execute(my_query)


# WAY TO CHECK LIST OF DATABASE IN MYSQL
import mysql.connector 

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
)

my_cursor = mydb.cursor()
my_query = ("SHOW DATABASES")
my_cursor.execute(my_query)

for x in my_cursor:
    print(x)


# WAY TO DELETE A DATABASE
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
)

my_cursor = mydb.cursor()
my_query = ("DROP DATABASE mydatabase,")
my_cursor.execute(my_query)


#  AFTER CREATING DATABASE ADD IT TO THE mydb PARAMETER
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "practicedb"
)

my_cursor = mydb.cursor()