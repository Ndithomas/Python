registered_users = []

def user_input(desc):
    return input(desc)

def register_user():
    print("\n USER  REGISTRATION ")
    username = user_input("Enter a username: ")
    password = user_input("Enter a password: ")

    user = {
        "username": username,
        "password": password,
        "blocked": False  
    }

    registered_users.append(user)
    print("Registration successful! Please log in to continue.\n")


def get_registered_users():
    return registered_users