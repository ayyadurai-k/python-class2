mark1 = int(input("Enter your mark 1 : "))
mark2 = int(input("Enter your mark 2 : "))
mark3 = int(input("Enter your mark 3 : "))

avg = (mark1 + mark2 + mark3) / 3

# 80 <=  ------ A 
# 60 <=  ------ B
# 40 <=  ------ C
# 40 >  ------ D

if avg >= 80  :
    print("Grade A")
elif  avg >= 60:
    print("Grade B")
elif avg >= 40 :
    print("Grade C")
else:
    print("Grade D")



