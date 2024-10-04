class Person:

    def get_person_input(self):
        self.name=input("Enter Name : ")
        self.age=int(input("Enter Age : "))
        self.gender=input("Enter Gender : ")


class Student(Person):

    def get_student_input(self):
        self.roll_no=input("Enter Roll No : ")
        self.m1 = int(input("Enter Mark 1 : "))
        self.m2 = int(input("Enter Mark 2 : "))
    
    def display_output(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Gender : ",self.gender)
        print("Roll No : ",self.roll_no)
        print("Mark 1 : ",self.m1)
        print("Mark 2 : ",self.m2)

s = Student()

s.get_person_input()
s.get_student_input()
s.display_output()




