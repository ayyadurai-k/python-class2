numbers = []
try :
    n = int(input("How many numbers : "))
    for i in range(n):
        num = int(input("Enter number : "))
        numbers.append(num)

    print("Numbers : ",numbers)

    index = int(input("Enter The Index To Find The Value  : "))

    value = numbers[index]
    print("Value :  ",value)

except IndexError : 
    print(" No Value Found ")
except ValueError : 
    print(" Invalid Number ")