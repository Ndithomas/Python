import mysql.connector

class Database:
    def __init__(self):
        self.connection = None
        
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Tomy@28728283701920",
                database="store_stock"
            )
            return self.connection
        except mysql.connector.Error as e:
            print(f"Database connection error: {e}")
            return None
            
    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
