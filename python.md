python notes

PYTHON FILES EXTENSIOM
.py
eg index.py 
HOW TO RUN PYTHON CODE 
Python3 index.py 
Python is very key with indentation
DATE TYPE CATEGORY 
Primitive Data Type
Object Data Type
Number (int,float,complex) 
Float
Boolean
Double 

Arithmetic 
+ -  / % * // 
comparison Operator
== value 
!= 10 != 10
> <  >= <= 
Assignment Operator 
=
+= -= = /+ %= //= *=
Print()
Type() 
bytecode 

OOP 
FUNCTIONAL 
Variable Name
Must start with letters 
Inbuild keywords

Camel Case studentNamesOfGreat12
Pascal eazch workd start with a caps 
NameOfStudent 
Snake Case 
student_name_of_grade_12

Rules of creating a function with Python
def
function name 
()
:
Create Function
You need call it when you want to use it 
Arquments
The value you supply to a function call is arguments
Parameter
GLOBAL AND LOCAL VARIABLE 
The Return keyword
Pass Keyword

if() true 
else if() checking more than one condition
else default condition

switch()

Create a Python Programm that will do the following. 
FIRST: Prompt the user to give you 3 Numbers 
NEXT: The programm will check the bigest number and tell the user from the
three values collected from the user 

Create a Python Programm that will do the following. 
First: Ask the user to enter a number and the programm should report
if the number is an even number or an odd Number 

Create a Python Programm that will do the following. 
First: The program will ask the user for two numbers and when divided it should
return the remainder,
Create a Python Programm that will do the following. 
First: Prompt the user to enter three numbers and return the numbers or print 
the numbers base on their acending order 

We need to Python Programm that will ask the user to enter five names 
of student in their class 
when you are enterinh last student we want you the programm to print
all the 5 student in that class 
NEX: The programm should be able to check if the names if up to 5 or less
If the student names is less than 5 it should keep asking the user to continue
entering the student names 

*******
******
*****
***
**
*

Create a python Program that will have a list of 10 numbers and then print all the even numbers in the list 

Create a python Program that will have a list of 10 numbers and then print all the odd numbers in the list 

# gamingAge = int(input("Enter your Age"))

# Mutable
# Duplicate
# fetch data base on index postion
# Range

# range(10)

# for eachCount in range(10):
#     print(eachCount)

# formFiveStudent1 = ["Paul","Mary","Suzan"]
# for eachStudent in formFiveStudent1:
#     if eachStudent == "admin":
#         print(eachStudent)
#         continue


def userInput(desc):
    return input(desc)


initValue =1
while initValue < 4:
   userInput(f"Enter {initValue} Student Name? ") 
   initValue  += 1
print("Done")

Create a Python program that will prompt the user to perform the following actions:

User Registration
User Login
NB: We need three files: register.py, login.py, and main.py.
The main.py file will be used to call all the other functions.

The program should allow the user to register, and the data will be stored in a list.
Upon completing registration, the system should prompt the user to log in using the details they provided during account creation.

The user will have three attempts to log in.

If the first and second attempts fail, the system should warn the user.
On the third attempt, if they fail again, the system should block the user and display a message stating that their account is blocked.
The user will then be instructed to contact an administrator for assistance.
Managing the login logic, including how the blocked status is handled, is up to you.

Welcome Screen
Upon launching the program, the following options should be displayed:

WELCOME TO UBANK  
Press C to Open an Account  
Press L to Login  
Press CL to Terminate the Session  
When the user terminates the session, the system should display:

Thank you for visiting us. See you next time.
NB: We need to utilize all the Python concepts we have covered so far.


JWT
Token
Payload
Permission
Authorisation
Webservices
API 
Cookies 
Session 
web storage 

PYTHON ASSIGNMENT
Program Style: OOP
Program: Calculator

Write a Python program that allows the user to perform calculator functionalities.

Welcome to P Calculator
Steps:
When the user runs the program, they should be prompted to enter:
First Number
Select an Operator (+, -, /, *, %)
Second Number
The program should perform the calculation based on the selected operator and display the correct output.
Note:
Each operation (+, -, *, /, %) should be implemented in a separate method.
Good Luck! 🚀


# class Parent:
#     def __init__(self,name,age,grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
        
#     def printAge(self):
#         print(f"My Age is {self.age}")
    
#     def printName(self):
#         print(f"My Name is {self.name}")
    
#     def printGrade(self):
#         print(f"My Grade is {self.grade}")


# class Child(Parent):
#     def __init__(self, name, age, grade):
#         super().__init__(tname, tage, grade)
        

# ch1 = Child()
# ch1.printAge("JohnP")



# class Person:
#     def __init__(self,username="",salary=0):
#         self.username = username
#         self.salary=salary
        
#     def setUsername(self,username):
#         if len(username) < 5:
#             print("username is too short")
#         else:
#             self.username=username
    
#     def getUsername(self):
#         return self.username   
        
#     def setSalary(self,salary):
#         if salary < 500:
#             print("Invalid Amount")
#         else:
#             self.salary=salary
    
#     def getSalary(self):
#         return self.salary
    
        
#     def printSalry(self):
#         print(f"You Username is {self.getUsername()} and your salary is {self.getSalary()}")
        

# p1 = Person()
# p1.setSalary(600)
# p1.setUsername("John Paul")
# print(p1.printSalry())


userData = {
    
}

class UserAuthentication:
    def __init__(self,username="",email="",password=""):
        self.username = username
        self.email = email
        self.password = password

    def setUsername(self,username):
        if len(username) < 5:
            print("Invalid Username")
        else:
            self.username = username
            
    def getUsername(self):
        return self.username

    def setEmail(self,email):
        self.email = email 
    
    def getEmail(self):
        return self.email
    
    def setPasscode(self,password):
        if len(password) < 5:
            print("Invalid Password")
        else:
            self.password = password
    
    def getPassword(self):
        return self.password


    def userLogin(self):
        username = input("Enter username.. ")
        password = input("Enter password.. ")
        if(username == userData['username'] and password == userData['password']):
            print("User Login Ok")
        else:
            print("Incorrect Login Details")
    
    def userRegistration(self):
        userData['username'] = self.setUsername(input("Enter username.. "))
        userData['password'] = self.setPasscode(input("Enter Password.. "))
        print("Account created Ok")
    
    
customer1 = UserAuthentication()
customer1.userRegistration()
customer1.userLogin()



TEXT BASE USER INTERFACE

WELCOME USTOCK INVENTORY

PROCEED 


PRESS C S U D 
C " Create New Stock"
S " Search Stock"
U " Update Stock"
D " Delete Stock"


ID | productName | Qty | Madate | ExDate 

Search base on the title of stock
Udate base ID of the stock
Delete base on the ID

CRUD 

Backend: Python
Frontend: Textbase (Terminal Base)
Programming Style/Pattern: OOP


USER
    Properties:
    username | email | gender | phone | Address |
    Method:
    Create Product | Search Product | Delete Product | Update Product

PRODUCT
    Properties:
    Name | Manufurer | expdata | madata | size | color
    Method:

DATABASE DESIGN 

Step 1: Update Password if not sure

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Tomy@28728283701920'; 


Step 2: Installl connector

pip3 install mysql-connector-python

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Meriki@12345"
)

print(mydb)