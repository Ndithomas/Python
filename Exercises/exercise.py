def userInput(desc):
    return input(desc)

def getStudentNames():
    studentNames = []
    while len(studentNames) < 5:
        name = userInput(f"Enter Student Name {len(studentNames) + 1}: ")
        if name.strip():  
            studentNames.append(name)
        else:
            print("Please enter a valid name.")
    return studentNames

def main():
    print("Please enter the names of 5 students in your class.")
    students = getStudentNames()
    print("\nThe 5 students in the class are:")
    for student in students:
        print(student)

main()