import mysql.connector as mysql_connector
from mysql.connector import Error as MysqlError

class Database:
    def __init__(self):
        self.connection = self.connect()

    def connect(self):
        try:
            connection = mysql_connector.connect(
                host='localhost',
                user='root',
                password='Tomy@28728283701920',
                database='stock_inventory_db'
            )
            return connection
        except MysqlError as e:
            print(f"Error connecting to MySQL: {e}")
            return None

    def execute_query(self, query, params=None, fetch=False):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params or ())

            if fetch:
                result = cursor.fetchall()
                return result
            else:
                self.connection.commit()
                return True

        except MysqlError as e:
            print(f"Error executing query: {e}")
            return None
        finally:
            cursor.close()

    def close(self):
        if self.connection:
            self.connection.close()
