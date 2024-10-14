class Parent:
    def __init__(self):
        self._name = "Jeevitha" # PROTECTED
        self.__age = 25 # PRIVATE
    
    def get_age(self):
        return self.__age


class Child(Parent):
   
    def display_name(self):
       print("Name : ",self._name) # Accessing protected attribute from child class
    
    def display_age(self):
       print("Age : ",self.get_age()) # Accessing private attribute from child class



obj = Child()

# print("Name : ",obj._name) # ITS POSSIBLE  , NOT RECOMMENDED

obj.display_name()
obj.display_age()