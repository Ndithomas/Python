
userCollectedValue1 = int(input("Enter the first number: "))
userCollectedValue2 = int(input("Enter the second number: "))
userCollectedValue3 = int(input("Enter the third number: "))


if userCollectedValue1 >= userCollectedValue2  and userCollectedValue1 >= userCollectedValue3:
    largest = userCollectedValue1
elif userCollectedValue2 >= userCollectedValue1 and userCollectedValue2 >= userCollectedValue3:
    largest = userCollectedValue2
else:
    largest = userCollectedValue3


print(f"The largest number among {userCollectedValue1}, {userCollectedValue2}, and {userCollectedValue33} is: {largest}")