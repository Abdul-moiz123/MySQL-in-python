# DROP OFF TABLE IN THE DATABASE --> PRACTICEDB
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "practicedb"
)

my_cursor = mydb.cursor()
my_query = ("DROP TABLE CUSTOMERS")
my_cursor.execute(my_query)



#DROP OFF TABLE IN THE DATABASEIF ITS EXIST --> PRACTICEDB
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "practicedb"
)

my_cursor = mydb.cursor()
my_query = ("DROP TABLE if exists CUSTOMERS")
my_cursor.execute(my_query)

