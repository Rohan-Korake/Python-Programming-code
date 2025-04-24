import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Github123"
)
if conn.is_connected():
    print("Successfully connected to MYSQL")
else:
    print("Connection failure")

conn.close()