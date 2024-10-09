
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self,name,age,roll_no , m1 , m2):
        self.roll_no = roll_no
        self.m1 = m1 
        self.m2 = m2
        super().__init__(name,age)

    
    def display(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Roll No : ",self.roll_no)
        print("Mark 1 : ",self.m1)
        print("Mark 2 : ",self.m2)


s = Student("Jeevitha",25,101,97,98)

s.display()