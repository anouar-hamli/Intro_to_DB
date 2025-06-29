import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password=''
    )
    if connection.is_connected():
        print("Connected to MySQL server successfully!")
except Error as e:
    print(f"Error: {e}")
finally:
    if connection.is_connected():
        connection.close()
        print("Connection closed.")
