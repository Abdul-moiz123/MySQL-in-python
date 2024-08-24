# HOW TO CREATE DATABASE 

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="haseeb725",
)

cur = mydb.cursor()
exe = cur.execute("CREATE DATABASE db1") 