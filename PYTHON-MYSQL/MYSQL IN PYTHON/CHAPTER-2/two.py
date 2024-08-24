# CREATE TABLE
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "practicedb"
)

my_cursor = mydb.cursor()
my_query = ("CREATE TABLE CUSTOMERS (name varchar(255) , address varchar(255))")
my_cursor.execute(my_query)


# CHECK TABLE IN THE DATABASE --> PRACTICEDB
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "practicedb"
)

my_cursor = mydb.cursor()
my_query = ("SHOW TABLES ")
my_cursor.execute(my_query)

for x in my_cursor:
    print(x)


#CREATE TABLE WITH THE PRIMARY KEY
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "practicedb"
)

my_cursor = mydb.cursor()
my_query = ("CREATE TABLE USERS (id int auto_increment PRIMARY KEY , name varchar(255) , address varchar(255))")
my_cursor.execute(my_query)


#SHOW TABLE WITH THE PRIMARY KEY
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "practicedb"
)

my_cursor = mydb.cursor()
my_query = ("SHOW TABLES")
my_cursor.execute(my_query)
for a in my_cursor:
    print(a)

# CREATE PRIMARY KEY IN THE ALREADY CREATED TABLE
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "practicedb"
)

my_cursor = mydb.cursor()
my_query = ("ALTER TABLE CUSTOMERS AND COLUMN ID INT AUTO_INCREMENT PRIMARY KEY")
my_cursor.execute(my_query)
