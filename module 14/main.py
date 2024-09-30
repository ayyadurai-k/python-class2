

class Student:

    def __init__(self,n,roll_number,a,b,c) : # INITIALIZATION
        self.name = n
        self.roll_number = roll_number
        self.m1 = a
        self.m2 = b
        self.m3 = c
    
    def calculate_total(self):
        total_marks = self.m1 + self.m2 + self.m3 
        return total_marks
    
    def display_name(self):
        print("Name :  ",self.name)


student1 = Student("Jeevitha",10,29,25,28)
student2 = Student("Abinaya",11,25,29,30)


student1.display_name()
student2.display_name()


student1_mark = student1.calculate_total()
student2_mark = student2.calculate_total()

print("Total mark of student 1 : ",student1_mark)
print("Total mark of student 2 : ",student2_mark)




