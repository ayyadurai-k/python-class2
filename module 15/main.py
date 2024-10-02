

class Employee:

    def __init__(self):
        self.name = ''
        self.salary = 0
        self.department = ''

    def get_input(self):
        self.name = input("Enter employee name : ") # {name:'XXXXXXX',salary:0,department:''}
        self.salary = int(input("Enter employee salary : ")) # {name:'XXXXXXX',salary:000000,department:''}
        self.department = input("Enter employee department : ")  # {name:'XXXXXXX',salary:000000,department:'YYYYYY'}

    def display_output(self):
        print("Name : ",self.name)
        print("Salary : ",self.salary)
        print("Department : ",self.department)
        print()

        


emp = Employee()
emp.get_input()
emp.display_output()








