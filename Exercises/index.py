class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def printAge(self):
        print(f"My age is  {self.age}")

    def printName(self):
        print(f"My name is  {self.name}")

    def printGrade(self):
        print(f"My grade is  {self.grade}")       

st1 = Student("Paul", 90,"Grade 12")
st1.printAge()
st1.printName()
st1.printGrade()