file = open('module13/sample.txt','r')

# READ
# str = file.read()
# print("Str : ",str)


# READLINE

# a = file.readline()
# b = file.readline()


# print("Line 1 : ",a)
# print("Line 2 : ",b)


# READLINEs

lines = file.readlines()

for line in lines:
    print("Line : ",line)
