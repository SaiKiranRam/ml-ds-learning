# Dictionary is a collection of Key-Value pairs similar to Maps Data Structure in Java
# Data retrieval is constant time. However, the order of insertion is not maintained
# The collections in Python are equivalent to Java's Collection<Object>, since the data structure
# can hold any type of keys and/or values, as long as the Key literal with its type is unique. Example
# Key as integer 1 and string "1" are considered as unique Keys

# Syntax
# These collections are defined within {} braces, the key and its associated value is separated with a :
# dict_var = {key1:value1, key2:value2, key3:value3, key4:value4}
#                         OR
# dict_var = dict({key1:value1, key2:value2, key3:value3, key4:value4}) -> Note curly braces here
#                         OR
# dict_var = dict([key1:value1, key2:value2, key3:value3, key4:value4]) -> Note square braces here
#                         OR
# dict_var = {} -> For creating an empty dictionary
subjects = {1:"Python", 2:"Statistics", 3:"Machine Learning"}
print(subjects)

print("\n", "#"*100, "\n", sep='')

print("To access a specific value, mention the dictionary var name with its key in []")
print("Value of subjects[1]:", subjects[1])
print("If a Key doesn't exist, then to avoid throwing error,"
      "\nwe can use get function and provide a our key as 1st param and default value as 2nd parameter")
print("subjects.get(100000, \"Default_Value\"):", subjects.get(100000, "Default_Value"))

print("\n", "#"*100, "\n", sep='')

print("Before modifying subjects dictionary: ", subjects)
subjects[3] = "Data Analysis"
print("After modifying subjects dictionary: ", subjects)

# NOTE that multiple keys can be modified at same time
print("Also can be modified by .update function, as below"
      "\nsubjects.update({1:'Python Programming', 2:'Maths and Statistics'})", subjects.update({1:'Python Programming', 2:'Maths and Statistics'}))
print("After modifying subjects with .update function in dictionary: ", subjects)

print("New Key-value pair can also be added with the above .update function or by simply providing within []")
subjects.update({4: "Machine Learning"})
subjects[5] = "Data Science"
subjects.update({6: "Kacha Badam"})
print("subjects:", subjects)

print("\n", "#"*100, "\n", sep='')

print("Removing an element can be done by providing the key in del(<dictionary_name>[<key_name>]) function")
del(subjects[6])
print("Current collection after removing elements in subjects: ", subjects)


# Dictionary methods
#
# dict.copy() - Returns a copy of the dictionary
#
# dict.clear() - Remove all the elements from the dictionary
#
# dict.get(key, default = “None”) - Returns the value of specified key
#
# dict.items() - Returns a list containing a tuple for each key value pair
#
# dict.keys() - Returns a list containing dictionary’s keys
#
# dict.update(dict2) - Updates dictionary with specified key-value pairs
#
# dict.values() - Returns a list of all the values of dictionary
#
# pop() - Remove the element with specified key
#
# popItem() - Removes the last inserted key-value pair
#
# dict.setdefault(key,default= “None”) - set the key to the default value if the key is not specified in the dictionary
#
# dict.has_key(key) - returns true if the dictionary contains the specified key.    # -> Likely Removed
#
# dict.get(key, default = “None”) - used to get the value specified for the passed key.

print("\n", "#"*100, "\n", sep='')
print("Copy of one dict's values to create a fresh new dict can be done by .copy() function")
duplicate = subjects.copy()
# If you do not use .copy(), and modify duplicate, the change will reflect in subjects as well
# duplicate = subjects

print("Dictionaries can be cleared with .clear() function as below")
print("Prior clearing, collection duplicate: ", duplicate)
duplicate.clear()
print("After clearing, collection duplicate: ", duplicate)
print("After clearing, collection subjects: ", subjects)


print("\n", "#"*100, "\n", sep='')
print("Lets print just the keys and values as a separate collection using .keys() and .values()")
print("subjects.keys():", subjects.keys())
print("subjects.values():", subjects.values())

duplicate = subjects.copy()
duplicate[6] = "Baigan Baata"
print("Before popitem(), duplicate dict:", duplicate)
print("popItem():", duplicate.popitem())
print("After popitem(), duplicate dict:", duplicate)
duplicate[6] = "Baigan Baata"
print("Before POP(), duplicate dict:", duplicate)
print("\nAlthough key 6 is manually added, in real world code its always good to check if a key exists in dict",
      "which can be done by using .get(<key>, <default_Value>) function,"
      "return the key's respective value if its present ELSE returns the <default_value> provided earlier"
      "duplicate.get(6, 'Not_Applicable'):", duplicate.get(6, 'Not_Applicable'), sep='\n')
print("Another example of .get(), duplicate.get(1000, 'Not_Applicable'):", duplicate.get(1000, 'Not_Applicable'))
print("\nComing back to popping recently inserted item using: popItem():", duplicate.pop(6))
print("After POP(), duplicate dict:", duplicate)

print("\n", "#"*100, "\n", sep='')
print("The .setdefault(<key>, <default_value>) function is used to check in a dictionary whether a key exists,"
      "\nif Yes, then simply fetch its associated Value."
      "\nif Not, then set the Key with the <defaul_value> as its the value into the dictionary and then return the same value back")
print("duplicate.setdefault(1, 'Blahhhhhhh'):", duplicate.setdefault(1, 'Blahhhhhhh'))
print("duplicate.setdefault(100, 'Blahhhhhhh'):", duplicate.setdefault(100, 'Blahhhhhhh'))
print(duplicate)
duplicate.popitem()
print("\n\n", "#"*100, "\n", sep='')

print("We can also check if a key exists in a dict by using 'in'.\nExample1: 1 in duplicate = ", 1 in duplicate)
print("Example2: 3000 in duplicate = ", 3000 in duplicate)

print("\n", "#"*100, "\n", sep='')
print("Iterating through loop can be done in 3 ways, as follows:",
      "1) Using keys with .keys()",
      "2) Using values with .values()",
      "3) Using key-value pairs with .items()", sep='\n\t')
for key in duplicate.keys():
      print("Iterating on key:", key)

for value in duplicate.values():
      print("Iterating on value:", value)

for key, value in duplicate.items():
      print(f"Iterating over the key-value pair: {key}-{value}")
