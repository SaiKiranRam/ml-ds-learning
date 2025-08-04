# Syntax of for loop
# for var in iterable:
#   <Statement_Block>
from Tools.scripts.make_ctype import values

# For loop with lists
list = ["Python", "Data Structures", "Machine Learning", "Data Science"]
print("The topics under the subject are:")
for concept in list:
    print(f"\t{concept}")

# For loop with Dictionary
print("Dictionary Iteration")
d = dict()
d["key1"] = "value1"
d["key2"] = "value2"
d["key3"] = "Value3"

for index in d:
    print(index, "\t", d[index])


# For loop with strings
word = "MachineLearningChampion"
for character in word:
    print(character, end='  ')# M  a  c  h  i  n  e  L  e  a  r  n  i  n  g  C  h  a  m  p  i  o  n

print()
# For loop with range
# Only for integers
for num in range(10):
    print(num, end=' ')#    0 1 2 3 4 5 6 7 8 9

print()
# Nested for loops
for num in range(2):
    for num2 in range(3):
        print(f"({num}, {num2})")
# (0, 0)
# (0, 1)
# (0, 2)
# (1, 0)
# (1, 1)
# (1, 2)

print()
# The enumerate function:
# The enumerate function is used to obtain both index and value during iteration
for index, value in enumerate(list): #  list assigned in Line# 7
    print(f"The value at {index} in the list is: {value}")

print()
# List comprehension provides a concise way to assign values into the list
squares = [x**2 for x in range(5)]
print(squares) #    [0, 1, 4, 9, 16]

for num in range(10):
    if num % 2 == 0:
        print(f"Even number printed: {num}")
        continue
    print(f"This line is printed if continue keyword isn't reached, index: {num}")

