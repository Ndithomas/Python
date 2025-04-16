import mysql.connector

# Connect to server
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Tomy@28728283701920"
    )

# Get a cursor
print(database)
