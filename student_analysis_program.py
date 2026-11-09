#Building a student analysis program witthpython

students = [
    {"name": "Mary", "mark": 78},
    {"name": "John", "mark": 65},
    {"name": "Peter", "mark": 45},
    {"name": "Grace", "mark": 91},
    {"name": "David", "mark": 52}
]


def calculate_average(marks):
    return sum(marks) / len(marks)


marks = []

for student in students:
    marks.append(student["mark"])


average = calculate_average(marks)


print("===== STUDENT RESULTS =====")

for student in students:

    name = student["name"]
    mark = student["mark"]

    if mark >= 50:
        status = "Pass"
    else:
        status = "Fail"

    print(name, "-", mark, "-", status)


print("\n===== CLASS STATISTICS =====")

print("Number of students:", len(students))
print("Average mark:", average)
print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))