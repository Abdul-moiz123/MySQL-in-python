# # ENTER SINGLE RECORD IN TO THE TABLE
# import mysql.connector

# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "haseeb725",
#     database = "practicedb"
# )

# my_cursor = mydb.cursor()

# my_query = "INSERT INTO USERS (name,address) values (%s,%s)"
# my_value = ("moiz","karachi")
# my_cursor.execute(my_query,my_value)

# mydb.commit()

# # ENTER MULTIPLE RECORD IN TO THE TABLE
# import mysql.connector

# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "haseeb725",
#     database = "practicedb"
# )

# my_cursor = mydb.cursor()

# my_query = "INSERT INTO USERS (name,address) values (%s,%s)"
# my_value = [("rafay","karachi"),("haseeb","lahore"),("anas","pindi")]
# my_cursor.executemany(my_query,my_value)
# mydb.commit()


# # GET ID OF THE RECORD IN TO THE TABLE
# import mysql.connector

# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "haseeb725",
#     database = "practicedb"
# )

# my_cursor = mydb.cursor()

# my_query = "INSERT INTO USERS (name,address) values (%s,%s)"
# my_value = ("moiz","karachi")
# my_cursor.execute(my_query,my_value)
# print(f"the ID of the record is {my_cursor.lastrowid}")
# print(f"the Total of the record is {my_cursor.rowcount}")
# mydb.commit()


