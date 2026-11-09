# #   🧠 Your Coding Challenge
# marks = [45, 67, 82, 39, 74, 91, 56, 48, 77, 63]


# Your program should calculate:
# 1. Number of students
# 2. Total marks
# 3. Average mark
# 4. Highest mark
# 5. Lowest mark
# 6. Number of students who passed
# 7. Number of students who failed
# 8. Pass percentage
# Use 50 as the pass mark.#

# writing the excerise code in python programming language
marks = [45, 67, 82, 39, 74, 91, 56, 48, 77, 63]


Number_of_students = len(marks)
Total_marks = sum(marks)
Average_mark = Total_marks / Number_of_students
Highest_mark = max(marks)
Lowest_mark = min(marks)


def count_passed_failed(marks, pass_mark=50):
    passed = 0
    failed = 0

    for mark in marks:
        if mark >= pass_mark:
            passed += 1
        else:
            failed += 1

    return passed, failed


# number student who passed and failed 

for mark in marks:
    if mark >= 50:
        print(mark, "Pass")
    else:
        print(mark, "Fail")

# getting the total for passed students and failed students
passed_students, failed_students = count_passed_failed(marks)
print("Passed students:", passed_students)
print("Failed students:", failed_students)

#getting the pass percentage
pass_percentage = (passed_students / Number_of_students) * 100
print("Pass percentage: ", pass_percentage, "%")

# Getting the fail percentage
fail_percentage = (failed_students / Number_of_students) * 100
print("Fail percentage: ", fail_percentage, "%")

# The chart gpt solution for the code challenge is complete and working as expected.

# marks = [45, 67, 82, 39, 74, 91, 56, 48, 77, 63]

# total = sum(marks)
# number_of_students = len(marks)
# average = total / number_of_students
# highest = max(marks)
# lowest = min(marks)

# passed = 0
# failed = 0

# for mark in marks:
#     if mark >= 50:
#         passed = passed + 1
#     else:
#         failed = failed + 1

# pass_percentage = (passed / number_of_students) * 100

# print("===== STUDENT PERFORMANCE =====")

# print("Number of students:", number_of_students)
# print("Total marks:", total)
# print("Average mark:", average)
# print("Highest mark:", highest)
# print("Lowest mark:", lowest)
# print("Passed:", passed)
# print("Failed:", failed)
# print("Pass percentage:", pass_percentage, "%")