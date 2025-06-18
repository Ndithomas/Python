import database as db_module
import re as regex

class Register:
    def __init__(self):
        self.db = db_module.Database()
    
    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return regex.match(pattern, email)
    
    def create_user(self, username, email, password, gender, phone, address):
        if not self.validate_email(email):
            return False, "Invalid email format"
        
        query = """
        INSERT INTO users (username, email, password, gender, phone, address)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        params = (username, email, password, gender, phone, address)
        
        result = self.db.execute_query(query, params)
        if result:
            return True, "User created successfully"
        return False, "Registration failed"
