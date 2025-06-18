import register as reg
import login as log

def user_input(desc):
    return input(desc)

def display_welcome_screen():
    print("WELCOME TO UBANK")
    print("Press C to Open an Account")
    print("Press L to Login")
    print("Press CL to Terminate the Session")

def main():
    while True:
        display_welcome_screen()
        choice = user_input("Enter your choice: ").upper()

        match choice:
            case "C":
                reg.register_user()
            case "L":
                log.login_user()
            case "CL":
                print("Thank you for visiting us. See you next time.")
                break
            case _:
                print("Invalid choice. Please try again.\n")


main()