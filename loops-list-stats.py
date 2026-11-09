#pyhton lists programmming

marks =[54,67,80,90,99,88,66,55,44,77,78,79,67,68,69,65,64,63,62,61]


#access individual values using their position, called an index.
print(marks)
print(marks[0])
print(marks[2])
print(marks[4])

#checking the length /number of items in the list
print(len(marks))


#looping in python programming code
    #pronting the marks using the for loop

for mark in marks:
    print(mark)


#calculating statistics using programming language

print("The highest mark is:", max(marks))
print("The lowest mark is:", min(marks))
print("The total marks is : ", sum(marks))

average = sum(marks) / len(marks)

print("Average Marks is :", average)


marks = [65, 72, 48, 81, 90]

for mark in marks:
    if mark >= 50:
       print(mark, "Pass")
    else:
       print(mark, "Fail")

    #Another if statement in the for loop 
for mark in marks:
    if mark>=80:
        print(mark, "Distinction")
    else:
        print(marks, "Credit")

#A Small Data Analysis Program in the other python file
