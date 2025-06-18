num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))


if num1 > num2:
    num1, num2 = num2, num1 
if num1 > num3:
    num1, num3 = num3, num1  
if num2 > num3:
    num2, num3 = num3, num2  


print(f"The numbers in ascending order are: {num1}, {num2}, {num3}")