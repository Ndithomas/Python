import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Tomy@28728283701920",
  database="student"
)

manager = mydb.cursor()
query = "INSERT INTO Users (lastname,firstname,email) VALUES (%s,%s,%s)"
value = ("mailto:john","joe","mich@gmail.com")
manager.execute(query,value)
mydb.commit()
print("User account created OK")