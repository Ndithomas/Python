import database as db_module

class Login:
    def __init__(self):
        self.db = db_module.Database()
    
    def authenticate(self, username, password):
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        result = self.db.execute_query(query, (username, password), fetch=True)
        
        if result and len(result) > 0:
            return True
        return False
