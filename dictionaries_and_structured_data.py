# Working with Dictionaries and Data Structure in python 
# for real-world data-analysis programs

#🐍 Python Mini-Lesson 3: Dictionaries,
#  Functions & Working With Student Data


# A Python dictionary stores data as key-value pairs.
# For example:
student = {
    "name": "Flonicah Phiri",
    "age": 26,
    "mark": 98
}

# "name" → key
# "Flonicah Phiri" → value
# "age" → key
# 26 → value
# "mark" → key
# 98 → value

# To access the values in a dictionary, you can use the keys. 
# For example:

print(student["name"])
print(student["age"])
print(student["mark"])

#Adding and Changing Data You can add 
# another piece of information:
student["name"] = "Vericah Chipeta"
student["age"]= 49
student["mark"] =100
student["Course"] ="Computer Science"


#checking the results after adding and changing the data
print(student)


#A list  of dictionaries can be used to store data for multiple students.
students = [
    {
        
        "name": "Flonicah Phiri",
        "age": 26,
        "mark": 98
    },
    {
        "name": "Vericah Chipeta",
        "age": 49,
        "mark": 100
    },
    {
        "name": "Chikondi Mbewe",
        "age": 30,
        "mark": 85
    },
    {
        "name": "Gift Mbewe",
        "age": 30,
        "mark": 85
    }
]


#Accessing the data inside the dictionaries and lists
print(students[0]["name"])  # Flonicah Phiri
print(students[1]["age"])   # 49
print(students[2]["mark"])  # 85
print(students[3]["name"])  # Gift Mbewe
print(students[2]["mark"])   # 30

#loop through the students instead of accessing them one by one

for student in students:
    print(student["name"])

    #combining the for loop with an if statement to check for a specific condition
    for student in students:
        if student["mark"] >= 90:
            print(student["name"], "has passed with distinction.")
        else:
            print(student["name"], "has passed.")


