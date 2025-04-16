import register as register_mod
import login as login_mod
import database as db_mod

class AuthManager:
    def __init__(self):
        self.register = register_mod.Register()
        self.login = login_mod.Login()
        self.db = db_mod.Database()
        self.current_user = None
        self.current_user_id = None
    
    def is_authenticated(self):
        return self.current_user is not None
    
    def handle_register(self):
        print("\nREGISTER NEW USER")
        username = input("Username: ")
        email = input("Email: ")
        password = input("Password: ")
        gender = input("Gender (Male/Female/Other): ")
        phone = input("Phone: ")
        address = input("Address: ")
        
        success, message = self.register.create_user(username, email, password, gender, phone, address)
        print(message)
    
    def handle_login(self):
        print("\nUSER LOGIN")
        username = input("Username: ")
        password = input("Password: ")
        
        if self.login.authenticate(username, password):
            result = self.db.execute_query(
                "SELECT user_id FROM users WHERE username = %s", 
                (username,),
                fetch=True
            )
            
            if result and len(result) > 0:
                self.current_user = username
                self.current_user_id = result[0][0] 
                print("Login successful!")
            else:
                print("Error fetching user data")
        else:
            print("Invalid credentials")
    
    def handle_logout(self):
        self.current_user = None
        self.current_user_id = None
        print("Logged out successfully")
