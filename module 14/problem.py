student1 = {
    "name" : "Jeevitha1",
    "roll_number" : 10,
    "mark1" : 25,
    "mark2" : 26,
    "mark3" : 22
}
student2 = {
    "name" : "Jeevitha2",
    "roll_no" : 11,
    "m1" : 26
}


students = [student1,student2]

total = students[0]["mark1"] + students[0]["mark2"] + students[0]["mark3"]

print("Total : ",total)