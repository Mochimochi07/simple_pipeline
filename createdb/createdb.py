import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Loverfella9"
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE pokemon")
cursor.execute("USE pokemon")
cursor.execute("CREATE TABLE pokemon (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
