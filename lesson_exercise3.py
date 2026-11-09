#exercise 3: Create a list of students with their names and marks.
students = [
    {"name": "Alice", "mark": 84},
    {"name": "Brian", "mark": 49},
    {"name": "Catherine", "mark": 73},
    {"name": "Daniel", "mark": 38},
    {"name": "Esther", "mark": 92},
    {"name": "Frank", "mark": 61}
]
#printing every student's name and marks using a loop
for student in students:
    name = student["name"]
    mark = student["mark"]
    print(name, "-", mark)
#determining pass and fail students using a loop and if statement when the pass mark is 50

for student in students:
    name = student["name"]
    mark = student["mark"]

    if mark >= 50:
        print(name, "has passed with a mark of", mark)
    else:
        print(name, "has failed with a mark of", mark)

#Calculating the len, aveg num of students, average mark, highest mark
# , and lowest mark using programming language and passed and failed and also pass percentage
number_of_students = len(students) #num of students

total_marks = sum(student["mark"] for student in students) #sum the total marks

average_mark = total_marks / number_of_students #calculate the average mark

highest_mark = max(student["mark"] for student in students) #find the highest mark

lowest_mark = min(student["mark"] for student in students) #find the lowest mark


# determining the number of students who passed and failed using a loop and if statement
passed_students = 0
failed_students = 0

def count_passed_failed(students, pass_mark=50):
    passed = 0
    failed = 0

    for student in students:
        if student["mark"] >= pass_mark:
            passed += 1
        else:
            failed += 1

    return passed, failed

passed_students, failed_students = count_passed_failed(students)
print("Number of students who passed:", passed_students)
print("Number of student who failed: ", failed_students)

 #Calculating the pass percentage and fail percentage
pass_percentage = (passed_students / number_of_students) * 100
fail_percentage = (failed_students / number_of_students) * 100
print("Pass percentage: ", pass_percentage, "%")
print("Fail percentage: ", fail_percentage, "%")
