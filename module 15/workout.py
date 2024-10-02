class Student:
    def __init__(self,count):
        self.count = count

    def get_input(self):
        self.name = input(f"Enter the student {self.count} name: ")
        self.department = input("Enter the department: ")
        self.mark_1 = int(input("Enter the mark_1: "))
        self.mark_2 = int(input("Enter the mark_2: "))
        self.mark_3 = int(input("Enter the mark_3: "))

    def calculate_total_average(self):
        self.total = self.mark_1 + self.mark_2 + self.mark_3
        self.average = self.total / 3

    def display_output(self):
        print(f"Student {self.count} : \n")
        print("Name:", self.name)
        print("Department:", self.department)
        print("Mark 1:", self.mark_1)
        print("Mark 2:", self.mark_2)
        print("Mark 3:", self.mark_3)
        print("Average:", self.average)
        print("Total:", self.total)
        print()

student1 = Student(1) # {}
student2 = Student(2) # {}


student1.get_input() # {name,department,mark_1,....mark_3}
student2.get_input() # {name,department,mark_1,....mark_3}


student1.calculate_total_average()  # {name,department,mark_1,....mark_3,total,average}
student2.calculate_total_average()  # {name,department,mark_1,....mark_3,total,average}

student1.display_output()
student2.display_output()