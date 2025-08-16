# Syntax of for loop
# for var in iterable:
#   <Statement_Block>

# For loop with lists
myList = ["Python", "Data Structures", "Machine Learning", "Data Science"]
print("The topics under the subject are:")
for concept in myList:
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
# For loop with range in reverse, with 10 as starting till -1 (exclusive), with an iteration update of -1
# Only for integers
for num in range(10, -1, -1):
    print(num, end=' ')#    10 9 8 7 6 5 4 3 2 1 0

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
print(myList) # ['Python', 'Data Structures', 'Machine Learning', 'Data Science']
for index, value in enumerate(myList):
    print(f"The value at {index} in the list is: {value}")
# The value at 0 in the list is: Python
# The value at 1 in the list is: Data Structures
# The value at 2 in the list is: Machine Learning
# The value at 3 in the list is: Data Science


print()
# List comprehension provides a concise way to assign values into the list
squares = [x**2 for x in range(5)]
print(squares) #    [0, 1, 4, 9, 16]

for num in range(10):
    if num % 2 == 0:
        print(f"Even number printed: {num}")
        continue
    print(f"This line is printed if continue keyword isn't reached, index: {num}")

