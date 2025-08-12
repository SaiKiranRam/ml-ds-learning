# Python Lists are just like the arrays, declared in other languages which is an ordered collection of data. It is very flexible as the items in a list do not need to be of the same type. Here are the key characteristics of lists:
#
# Lists in Python maintain the order of elements as they are inserted. The order in which elements are added is the same order in which they are stored.
# Lists are mutable, meaning you can modify their elements after the list is created. You can change, add, or remove elements from a list.
# Lists can contain elements of different data types.
# Lists in Python are dynamic, meaning they can grow or shrink in size as needed.
# Lists support indexing, allowing you to access individual elements using their position (index) in the list.
# Lists are iterable, meaning you can loop through each element using a for loop.
from setuptools.namespaces import flatten

# Lists are created using '[]' brackets and mentioning elements separated by ','
sample_list = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 123, 456, True, False]
print("sample_list:", sample_list)


print('\n', '#'*100, sep='\n')
print('\t\tAccessing Elements')
print('#'*100, sep='\n')
print("Elements can be accessed with index, a positive number as index provides its respective element")
print("where as a negative index (from -1) can be used to provides elements from reverse in list")
words = ["This", "is", "a", "sample", "list", "collection", "in", "Python"]
print("Our sample collection var words:", words)
print(f"Accessing\n first element: {words[0]}\n last element: {words[-1]}")


print('\n', '#'*100, sep='\n')
print('\t\tSlicing List')
print('#'*100, sep='\n')
print("Printing sub list from a list using index as below")
print("As with any program, first index inclusive, second index exclusive - words[0,5]:", words[0:5])
print("Iterating over list by skipping an element:", words[::2])
print("Reversing a list by providing negative numbers as index - words[::-1]:", words[::-1])
print("Reversing a list by two steps (skip ome element in between) - words[::-2]:", words[::-2])


print('\n', '#'*100, sep='\n')
print('\t\tList Modifiers - Changing elements in List')
print('#'*100, sep='\n')
words[1] = "IS"
print("Modify the elements of a list by its index. For example: words[1] = 'is', we can modify its value",
      f"into ans upper case as words[1] = 'IS', words[1]: {words[1]}", sep='\n')


print('\n', '#'*100, sep='\n')
print('\t\tList Modifiers - Adding to List')
print('#'*100, sep='\n')
words.append('World')
print("Use .append() function to add an element at the end. words.append('World')", words)
print("The same can be performed for a multidimensional list.",
      "For example. For a 2D list, one list element can be appended to existing list data structure")


print('\n', '#'*100, sep='\n')
print('\t\tList Modifiers - Removing from List')
print('#'*100, sep='\n')
sample = ["this","is","just","is","sample"]
print("List before any element removal - sample:", sample)
sample.remove('is')
print("The .remove function removes the first of occurrence of the element if there are multiple repetitions of the same element")
print("List after an element removal - sample:", sample)


sample = ["this","is","just","a","sample"]
print('\n', '#'*100, sep='\n')
print('\t\tList Operations - Concatenating to the list')
print('#'*100, sep='\n')
print("Similar to string, list concatenating can be performed over list with '+' operator."
      f"\nExample, sample + sample = {sample + words}")


print('\n', '#'*100, sep='\n')
print('\t\tList Operations - Repetition to the list')
print("Similar to string, list repetition can be performed over list with '*' operator."
      f"\nExample, sample * 5 = {sample * 5}")


print('\n', '#'*100, sep='\n')
print('\t\tCommon List Operations - len() to calculate number of elements in the list')
print('#'*100, sep='\n')
print("Similar to string, list elements number can be calculated over list with len(<list>) function."
      f"\nExample, len(sample) = {len(sample)}")


print('\n', '#'*100, sep='\n')
print('\t\tList Operations - Counting repetition of an element in a list')
print('#'*100, sep='\n')
print("Using count(<value to search>) we can get the number of repetitions of an element if present in a list)"
      f"\nExample, Finding word 'is' from sample + sample = {(sample + sample).count('is')}",
      f"\nThe count if element is not present:  {(sample + sample).count('ABCD')}")


print('\n', '#'*100, sep='\n')
print('\t\tList Operations - Finding index of an element in a list')
print('#'*100, sep='\n')
print("Using index(<value to search>) we can get the index of an element if present in a list, if its not present throws ValueError)"
      f"\nExample, Finding word 'is' from sample = {sample.index('is')}")


print('\n', '#'*100, sep='\n')
print('\t\tList Operations - Extending a list')
another_sample = sample.copy()
print("another_sample:", another_sample)
another_sample.extend(words)
print("List can be extended by providing any number of elements or another list itself",
      "using .extend(<new_list>) or .extend([elm1,elm2,.....]) function",
      f"Example, another_sample.extent(words)",
      another_sample,
      sep='\n')


print('\n', '#'*100, sep='\n')
print('\t\tCommon List Operations - sort() to calculate number of elements in the list')
print('#'*100, sep='\n')
print("A list with its sorted elements can be generated over list with sorted(<list>) function."
      f"\nExample, sorted(sample) = {sorted(sample)}")
print("\nFor reverse sorted elements from a given list,",
      "add reverse flag True to the sorted function as - sorted(<list>) function.",
      f"Example, sorted(sample) = {sorted(sample, reverse=True)}", sep='\n')


print('\n', '#'*100, sep='\n')
print('\t\tMaxima and Minima in a list')
print('#'*100, sep='\n')
numerical_list = [3,4,5,6,7,1,2,9,8]
print("Calculates the maximum value with max() and minimum value with min() function respectively",
      "Cannot be used for heterogeneous elements containing multiple data type values")
print("max(numerical_list):", max(numerical_list))
print("min(numerical_list):", min(numerical_list))
print("max(sample):", max(sample))
print("min(sample):", min(sample))


print('\n', '#'*100, sep='\n')
print('\t\tIterating over a list - With For loop')
print('#'*100, sep='\n')
print("Iterating directly over list:")
for elements in words:
      print(elements, end=" ")
print("\n\nIterating over list with index:")
for num in range(len(words)):
      print(words[num], end=" ")
print("\n\nIterating over list with index in reverse:")
for reverseNum in range(len(words) -1, -1, -1):
      print(words[reverseNum], end=" ")


print('\n', '#'*100, sep='\n')
print('\t\tList Comprehensions')
print('#'*100, sep='\n')
print("List comprehensions provide a concise way to create lists.",
      "They offer a compact syntax for generating lists based on existing iterables, such as lists, strings, or ranges.", sep='\n')
print("\nList comprehension from range:\n")
num_list = [i for i in range(1,6)]
print("num_list:", num_list)
squared_list = [i**2 for i in num_list]
print("squared_list:",squared_list)
print("\nList comprehension with conditional statement:\n")
squared_even_list = [i**2 for i in num_list if i%2 == 0]
print("squared_even_list:",squared_even_list)

print("\nFlattening a multi-D list")
# Here's a breakdown:
#
# The first for row in nested_list iterates through each inner list (row) in lst, which are [1, 2, 3], [4, 5, 6], and [7, 8, 9].
#
# The second for num in row iterates through each element (num) in the current row.
#
# The result is a single list containing all elements from the inner lists, which is [1, 2, 3, 4, 5, 6, 7, 8, 9].
nested_list = [[1,2,3],[4,5,6],[7,8,9],[9,4,2]]
flatten_list = [num for row in nested_list for num in row]
print(flatten_list)