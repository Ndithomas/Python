class Calculator:
    def __init__(self):
        print("Welcome to P Calculator")
        self.run_calculator()
    
    def run_calculator(self):
        while True:
            try:
                firstNumber = int(input("Enter first number: "))
                operator = input("Select an operator (+, -, /, *, %): ")
                secondNumber = int(input("Enter second number: "))
                
                result = None
                
                if operator == '+':
                    result = self.add(firstNumber, secondNumber)
                elif operator == '-':
                    result = self.subtract(firstNumber, secondNumber)
                elif operator == '*':
                    result = self.multiply(firstNumber, secondNumber)
                elif operator == '/':
                    result = self.divide(firstNumber, secondNumber)
                elif operator == '%':
                    result = self.modulo(firstNumber, secondNumber)
                else:
                    print("Invalid operator! Please try again.")
                    continue
                
                print(f"Result: {result}\n")
                
                another = input("Perform another calculation? (y/n): ").lower()
                if another != 'y':
                    print("Goodbye!")
                    break
                    
            except ValueError:
                print("Invalid input! Please enter numbers only.")
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed!")
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError
        return a / b
    
    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError
        return a % b

calc = Calculator()