# Taking an input and printing it
name = input("Hello There! This is an AI ML course python prompt. What's your name by the way?")
# Note that below print function doesn't explicitly have spaces between the usual string and variables since
# they're comma separated, the python will automatically take care of the spaces
print("Welcome,", name, "! Let's jump into the course and create new apps 😄💪")


name = input("Please enter the name of your headache: ")
# For String/text, typecasting isn't required as Python will automatically consider the input as String/text
# Typecasting input with int() converts the data into int type
age = int(input("Please enter headache's age: "))
city = input("Enter headache's city: ")
print("Details you've entered are :")
print(name, age, city) # Note that the variables are only comma separated. Bellow will be formatted for brevity
print("Name:", name)
print("Age:", age)
print("City:", city)
# ______________________________________________________________________________________________________________________

# Taking multiple space-separated inputs from console and printing it
x, y = input("Enter number of boys and girls in your class respectively:").split()
# NOTE: the .split90 is defined for string type only, hence typecasting int() or any other data type on input
#     and then splitting to assign multiple variables will not work
print() # By default, prints new line
boysNumber = "Number of boys:", x
girlsNumber = "Number of girls:", y

# Python has a provision to print multiple strings with a common separator which is appended between these strings
# Similarly, we can also define an end text which is executed after executing all the given Strings
# By default value of separator - sep is a single whitespace and of end is a new line \n
print(boysNumber, girlsNumber, sep='\n', end='\n_________________________________________\n')

# EXAMPLE 2
# date, month, year = input("Enter the date, month and year separated by a space:").s
# print(date, month, year, sep='-', end='\n\n')


# ______________________________________________________________________________________________________________________

# Type casting input or given values
# We can convert a single string input into int or any proper data type by casting it over input function OR
# by casting it over assigned variable
z = int(input("Enter total number of students, according to you:"))
totalNumber = int(x) + int(y)
print("Entered number of students:", z, "\nWhile the actual total is:", totalNumber)

# Typecasting the input/int/string to float using float() function
boysRatio = float(int(x) / totalNumber)
print("Ratio of boys to to total students in decimals:", boysRatio) # For example Prints 0.3333333333333333 ( many trailing numbers)
print("Formatting above decimal result into nearest 2 decimals: ${:.2f}".format(boysRatio))


# Using f-string
# We can use f-string by placing f"...{var1}....{var2}..." within print function argument where var1 and var2 are
# already assigned variables which needs to be logged
#Based on the above count of x (boys) and girls (y) using the same variables as example
print(f"With f-String we know that in the class there are {x} boys and {y} girls")

# Using % operator
# %d - integer
# %f - float
# %s - string
# %x - hexadecimal
# %o - octal

print("Total number of students are: %d" %totalNumber, "in the class")
