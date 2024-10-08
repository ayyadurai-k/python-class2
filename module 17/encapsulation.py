class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary 

    def set_salary(self,salary):
        self.__salary = salary

emp = Employee("Jeevitha",100000)

print("Salary Before : ",emp.get_salary())

emp.set_salary(200000)

print("Salary After : ",emp.get_salary())
