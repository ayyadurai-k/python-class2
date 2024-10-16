
numbers = []

try :
    n = int(input("How many numbers : "))
except ValueError :
    print("Invalid Number")

for i in range(n):
    num = int(input("Enter number : "))
    numbers.append(num)

print("Numbers : ",numbers)

index = int(input("Enter The Index To Find The Value  : "))

try : # 1
    value = numbers[index] #  2 
    print("Value :  ",value) # 3
except IndexError: # 4
    print("No Value Found") # 5

