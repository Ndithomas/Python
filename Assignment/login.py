import register as reg

def user_input(desc):
    return input(desc)

def login_user():
    registered_users = reg.get_registered_users()
    attempts = 3

    print("\n USER LOGIN")
    while attempts > 0:
        username = user_input("Enter your username: ")
        password = user_input("Enter your password: ")

    
        for user in registered_users:
            if user["username"] == username and user["password"] == password:
                if user["blocked"]:
                    print("Your account is blocked. Please contact the administrator.")
                    return False
                    
                else:
                    print("Login successful! Welcome back,", username)
                    return True

        attempts -= 1
        if attempts > 0:
            print(f"Invalid credentials. You have {attempts} attempt(s) left.\n")
        else:
            
            for user in registered_users:
                if user["username"] == username:
                    user["blocked"] = True
                    print("You have exceeded the maximum number of attempts. Your account is blocked.")
                    print("Please contact the administrator for assistance.")
                    return False
                    