import mysql.connector
from mysql.connector import Error
from appmoduls import mysqlcr
import bot

def init_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name 
            )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = init_connection("127.0.0.1", "root", "37113711", "sm_app")

def execute_query(connection, query):
     cursor = connection.cursor()
     try:
         cursor.execute(query)
         connection.commit()
         print("Query executed successfully")
     except Error as e:
         print(f"The error '{e}' occurred")


create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT,
  name TEXT NOT NULL,
  PRIMARY KEY (id)
)
"""
execute_query(connection, create_users_table)

create_users = """
INSERT INTO
  `users` (`name`)
VALUES
  (?);
"""
reviewers_records = [
       ("tom")
      ]
with connection.cursor() as cursor:
        cursor.executemany(create_users, reviewers_records)

def execute():
      execute_query(connection, create_users)
