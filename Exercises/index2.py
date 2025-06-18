

userData = {}

class UserAuthentication:
    def __init__(self, username="", email="", password=""):
        self.username = username
        self.email = email
        self.password = password

    def setUsername(self, username):
        if len(username) < 5:
            print("Invalid Username")
            return False
        else:
            self.username = username
            return True
            
    def getUsername(self):
        return self.username

    def setEmail(self, email):
        self.email = email 
    
    def getEmail(self):
        return self.email
    
    def setPasscode(self, password):
        if len(password) < 5:
            print("Invalid Password")
            return False
        else:
            self.password = password
            return True
    
    def getPassword(self):
        return self.password

    def userLogin(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == userData.get('username') and password == userData.get('password'):
            print("User Login Successful")
        else:
            print("Incorrect Login Details")
    
    def userRegistration(self):
        while True:
            username = input("Enter username (min 5 chars): ")
            if self.setUsername(username):  # Validates and sets self.username
                break  # Exit loop if valid
        
        while True:
            password = input("Enter password (min 5 chars): ")
            if self.setPasscode(password):  # Validates and sets self.password
                break  # Exit loop if valid
        
        # Store validated credentials in userData
        userData['username'] = self.username
        userData['password'] = self.password
        print("Account created successfully!")
    
customer1 = UserAuthentication()
customer1.userRegistration()
customer1.userLogin()