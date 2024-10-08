
class Father: # PARENT CLASS OR BASE CLASS
    def call_father(self):
        print("From Father")

    def display_amount(self):
        print("2000 Rs")

class Daughter(Father): # CHILD CLASS OR SUB CLASS
    def call_daughter(self):
        print("From Daughter")
    
    def display_amount(self):
        print("1000 Rs")

# f = Father()
# f.call_daughter()

d = Daughter()
d.call_father()
d.display_amount()
d.call_daughter()