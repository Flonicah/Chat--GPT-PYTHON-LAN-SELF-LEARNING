#A Small Data Analysis Program in python programming

marks = [65, 72, 48, 81, 90, 55, 43, 76, 88, 39]

total = sum(marks)
number_of_students = len(marks)
average = total / number_of_students
highest = max(marks)
lowest = min(marks)

print("===== STUDENT RESULTS =====")

print("Number of students:", number_of_students)
print("Total marks:", total)
print("Average mark:", average)
print("Highest mark:", highest)
print("Lowest mark:", lowest)

print("\n===== PASS/FAIL =====")

for mark in marks:
    if mark >= 50 :
        print(mark, " Pass")
    
    else:
        print(mark, " Fail")