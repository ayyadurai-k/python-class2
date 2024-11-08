

class NegativeNumberError(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)


def multiple(a,b):
    try :
        if a < 0 : 
            raise NegativeNumberError("Negative numbers are not allowed(a)")
        if b < 0 :
            raise NegativeNumberError("Negative numbers are not allowed(b)")
        return a * b
    except NegativeNumberError as e :
        print(e.message)

print(multiple(-2,-2))