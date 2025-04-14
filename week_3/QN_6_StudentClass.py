''' A program with a class Student with the attributes such as id, name, address, admission year, level, 
 section. The program will instantiate the object of class to take input for all the attributes and display the output.'''

class Student:
    def __init__(self):
        #initializing the attributes of the object
        self.student_id= input("Enter student ID: ")
        self.student_name= input("Enter the name of student: ")
        self.student_address=input("Enter the address of student: ")
        self.student_admission_year=input("Enter the admission year of student: ")
        self.student_level=input("Enter the level of student: ")
        self.student_section=input("Enter the section of student: ")

    def display(self):
        # Displays the student details
        print("\n ---Student details--- \n")
        print(f" ID:, {self.student_id}")
        print(f" Name:, {self.student_name}")
        print(f" Address:, {self.student_address}")
        print(f" Admission Year: {self.student_admission_year}")
        print(f" Level: {self.student_level}")
        print(f" Section:, {self.student_section}")

student1= Student()# Creating an instance of student class

student1.display()