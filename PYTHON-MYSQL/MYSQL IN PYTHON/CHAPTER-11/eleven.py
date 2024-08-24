import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="haseeb725",
    database="practicedb"
)

my_cursor = mydb.cursor()

my_query = """
    SELECT users.name AS user, customers.name AS fav 
    FROM users 
    INNER JOIN customers ON users.fav = customers.id
    LIMIT 5;
"""

my_cursor.execute(my_query)
my_result = my_cursor.fetchall()

for a in my_result:
    print(a)

my_cursor.close()
mydb.close()
