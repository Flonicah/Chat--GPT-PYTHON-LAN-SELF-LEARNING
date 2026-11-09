#Creating functions in python programming language
#functions allows to package code into reusable blocks, 
# making it easier to organize and maintain your code.
#  Functions can take input parameters, 
# perform specific tasks, and return output values.

def greet():
    print("Hello, welcome to self learning of  Python programming language!")
    

    #functions with Parameters
    def greet_user(name):
        print("Hello, " + name + "! Welcome to self learning of Python programming language!")

        #in this case the "name" is  a parameter that can be passed to the function when it is called.
# functions that return values /results 

#marks list
marks = [65, 72, 48, 81, 90, 55, 43, 76, 88, 39]


def calculate_average(marks):

    total = sum(marks)
    number_of_students = len(marks)
    average = total / number_of_students
    return average
# displayiing the result of the average marks using the function
result = calculate_average(marks)
print("The average mark is:", result)