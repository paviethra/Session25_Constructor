class Student:
    #creating constructor
    def __init__(self):
        self.student_name = input("\nEnter Name of the Student: ")
        self.student_age = input("Enter the age of the Student: ")
        self.student_gender = input("Enter the gender of the Student: ")

    def display(self):
        print("\n Enter the Student Name: ",self.student_name)
        print("Enter the Student age",self.student_age)
        print("Enter the student gender: ",self.student_gender)


class Marks:
    def __init__(self):
        self.grade = input("Enter the student's Grade: ")
        print("----------Evaluate marks per Subject----------")
        self.english = float(input("Marks in english Subject: "))
        self.maths = float(input("Marks in  math Subject: "))
        self.physics = float(input("Marks in physics Subject: "))
        self.computer = float(input("Marks in computer Science Subject: "))
        self.chemistry = float(input("Marks in chemistry Subject: "))

    def display(self):
        self.total = self.english + self.maths + self.physics + self.computer + self.chemistry
        print("Total marks:",self.total)

class Data(Student,Marks):
    def __init__(self):
        Student.__init__(self)
        Marks.__init__(self)

    def result(self):
        Marks.display(self)

        
S1 = Data()
S1.result()
S2 = Data()
S2.result()


print("You can create more objects to add more student data")

        
    
