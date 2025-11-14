x = int(input("Enter number of students: "))
y = int(input("Enter number of subjects: "))
classsum = 0
count1 = 1
while count1 < x + 1:
    print("\nStudent no.", count1, ":")
    count2 = 1
    sum = 0
    while count2 < y + 1:
        grade = int(input("Enter a grade: "))
        sum += grade
        count2 += 1
    average = sum / y
    classsum += average
    count1 += 1
    print("The average of student number", count1, "is", average)
print("\nClass average: ", classsum / x, "\n")
