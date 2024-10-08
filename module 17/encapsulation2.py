

class User:

    def __init__(self,username,password):
        self.username = username
        self.__password = password
    
    def change_password(self, new_password):
        self.__password = new_password

    def get_password(self):
        return self.__password

user = User("Jeevitha", "password123")

print("Original password: " , user.get_password())

user.change_password("password321")

print("Changed password: " , user.get_password())