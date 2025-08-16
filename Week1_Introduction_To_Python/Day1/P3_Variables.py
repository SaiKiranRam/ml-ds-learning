# Variables naming Convention
    # Variable names can only contain letters, digits and underscores (_).
    # A variable name cannot start with a digit.
    # Variable names are case-sensitive (myVar and myvar are different).
    # Avoid using Python keywords (e.g., if, else, for) as variable names.

# Type Casting functions:
#     int() - Converts compatible values to an integer.
#     float() - Transforms values into floating-point numbers.
#     str() - Converts any data type into a string.

num = 5
numFloat = float(num)
numWord = str(num)
print("num:", num)
print("numFloat:", numFloat)
print("numWord:", numWord)
print("Integer addition with var num:", num + num) # 10
print("Float addition with var numFloat:", numFloat + numFloat) # 10.0
print("Int and Float addition with var num and numFloat:", num + numFloat) # 10.0
print("String addition with var numWord:", numWord + numWord) # 55

# Know the type of variable using type() function
# Simple example:
print("Type of 100 is: ", end='')
print(type(100), end='\n\n')
#Example # 2
print("Type of:", f"num: %s" %type(num), f"numFloat: %s" %type(numFloat), f"numWord: %s" %type(numWord), sep='\n')


# Unlike Java, Object reference in python works by allocating the value's reference directly to variable,
# if a variable is used to assign another variable even in that case the latest variable has direct access
# to the value instead of the former variable. For example:
a = 5
b = a
print("Value of a:", a, "and b:", b, "BEFORE CHANGES in a")
a = 10
print("Value of a:", a, "and b:", b, "AFTER CHANGES in a")

# We can delete a variable using del function. Example below:
del a
# After deleting if we try to access the same variable, we get NameError: name 'a' is not defined
# Uncomment below print function to verify the same
# print(a)