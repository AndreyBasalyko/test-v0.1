import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
            )
        print("Connection to MySQL successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("127.0.0.1", "root", "37113711")

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
def create():       
    create_database_query = "CREATE DATABASE IF NOT EXISTS sm_app"
    create_database(connection, create_database_query)
    