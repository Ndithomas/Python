num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def checkReminder():
    remainder = num1 % num2
    
    print(f"The remainder of {num1} divided by {num2} is: {remainder}")

checkReminder()