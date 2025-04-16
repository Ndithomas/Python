numberList = [3, 7, 10, 14, 17, 20, 22, 25, 28, 31]

def checkOddNumbers(numberList):
    print("Odd numbers in the list:")
    for number in numberList:
        if number % 2 != 0:  
            print(number)

checkOddNumbers(numberList)