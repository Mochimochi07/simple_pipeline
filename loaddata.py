import mysql.connector
import pandas as pd


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Loverfella9",
    database="pokemon"
)


cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS pokemon (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")


df = pd.read_csv("pokemon.csv")


for index, row in df.iterrows():
    name = row["results"].split("'")[3]
    sql = "INSERT INTO pokemon (name) VALUES (%s)"
    val = (name,)
    cursor.execute(sql, val)
    db.commit()

print("Data inserted into MySQL")
