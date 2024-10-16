
numbers = []

n = int(input("How many numbers : ")) #5 

for i in range(n):
    num = int(input("Enter number : "))
    numbers.append(num)

print("Numbers : ",numbers)

index = int(input("Enter The Index To Find The Value  : "))


print(" Value :  ",numbers[index])
