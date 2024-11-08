a = 10 
b = 2

try :
    c = a/b
    print("Answer : ",c)
except ZeroDivisionError :
    print("Denominator cannot be 0")
finally :
    print("Code ended")
