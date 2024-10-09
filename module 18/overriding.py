


class Father:
    def display(self):
        print("This is father")
    

class Son(Father):
    def display(self):
        super().display()
        print("This is son")


s = Son()

s.display()