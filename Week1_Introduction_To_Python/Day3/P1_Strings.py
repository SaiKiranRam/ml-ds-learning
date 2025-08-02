# A String is a data structure in Python that represents a sequence of characters. It is an immutable data type,
# meaning that once you have created a string, you cannot change it. Strings are used widely in many different applications,
# such as storing and manipulating text data, representing names, addresses, and other types of data that can be represented as text.
print("String Replication can be done by adding a * followed by a number,",
      "\nto replicate a string with the provided number of times.\nSyntax \"<string>\"*<repetition number>")
print("#"*50)
print("\tString Concatenation")
print("#"*50)
print("\nString concatenation involves combining multiple strings\n"
      "into a single string using the + operator.")
str1 = "Python"
str2 = "Data Science"
print("str1:",str1, "\tstr2:",str2)
print("Concatenated result from str1 + str2:", str1 + str2)
print("\n" + "#"*50)
print("\tString Length")
print("#"*50)
print("The len() function returns the length (number of characters) of a string.")
print("Length of str1:", len(str1))
print("\n" + "#"*50)
print("\tString Slicing")
print("#"*50)
print("In Python, the String Slicing method is used to access a range of characters in the String.",
      "\nSlicing in a String is done by using a Slicing operator, i.e., a colon (:).")
print("Similar to Java, the string returned after slicing",
      "\nincludes the character at the start index but not the character at the last index.")
sample = "MachineLearningChamp"
print("variable sample has value: " + sample)
print("Slicing characters from 5 (inclusive index) to 15(exclusive index):", sample[5:15])
print("Slicing characters from 5 till end of string:", sample[5:])
print("Slicing characters from 0 (start) till  to 15(exclusive index):", sample[:15])
print("Slicing characters from 1 (start) till  to -1(exclusive index):", sample[1:-1])
print("\n" + "#"*50)
print("\tString Case Conversion")
print("#"*50)
print("variable sample has value: " + sample)
print("Python upper() function when used on variable sample, converts all its characters to uppercase:", sample.upper() )
print("Python lower() function when used on variable sample, converts all its characters to lowercase:", sample.lower() )
print("Python capitalize() function converts \"abc def ghi\" -> \"Abc def ghi\":", "abc def ghi".capitalize() )
print("Python title() function converts \"abc def ghi\" ->  \"Abc Def Ghi\":", "abc def ghi".title())

print("\n" + "#"*50)
print("\tString Stripping")
print("#"*50)
print("Stripping functions remove any leading or trailing whitespaces in a string",
      "There are 3 functions:\n\t1)strip() -> removes whitespaces on both trailing and leading sides",
      "\n\t2) lstrip() -> removes leading whitespaces of the string",
      "\n\t3) rstrip() -> removes trailing whitespaces of the string")
whiteSpacedString = "      random text data      "
print("Sample test string, whiteSpacedString: '" + whiteSpacedString + "'")
print("whiteSpacedString.strip(): '" + whiteSpacedString.strip() + "'")
print("whiteSpacedString.lstrip(): " + whiteSpacedString.lstrip() + "'")
print("whiteSpacedString.rstrip(): '" + whiteSpacedString.rstrip() + "'")

print("\n" + "#"*50)
print("\tString Replacing")
print("#"*50)
print("Python replace() method replaces one substring with another")
level = "I'm beginner in Python"
updated_level = level.replace('beginner', 'expert')
print("Initial value of level:", level, "\nupdated_level:", updated_level)

print("\n" + "#"*50)
print("\tString Count")
print("#"*50)
print("The count() function provides the count of occurrence of any specific sub-string within a given string")
testString = "This is a test string for learning python string functions"
print('Sample variable testString:', testString)
print("Let's count the occurrence of 'i' in the given testString:", testString.count("i"))
print("Let's count the occurrence of 'i' in the given testString:", testString.count("i"))
print("Let's count the occurrence of 'is' in the given testString:", testString.count("is"))

print("\n" + "#"*50)
print("\tString Find")
print("#"*50)
print("The find() function returns the index of first occurrence of the substring, if not found then returns -1")
print("testString:",testString)
print("Index of the word 'string' in the testString", testString.find('string'))
print("Index of the word 'STRING' in the testString", testString.find('STRING'))

print("\n" + "#"*50)
print("\tString Check")
print("#"*50)
print("Multiple functions to test the nature of a string",
      "There are many functions:\n\t1)isAlpha() -> checks if given string contains alphabets",
      "\n\t2) isdigit() -> checks if given string contains digit(s) only",
      "\n\t3) islower() -> checks if given string contains lower cased characters only"
      "\n\t4) isupper() -> checks if given string contains upper cased characters only, etc........")
print("Example of isalpha() with", "Only words -> \n\t'abcd'", "abcd".isalpha(),
      "\n\tSpecial characters -> 'ab_cd'", 'ab_cd'.isalpha(),
      "\n\t'Word and Numbers -> abcd123'", 'abcd123'.isalpha(),
      "\n\tFloating String -> '2.0'", "2.0".isalpha(),
      "\n\tInteger as string -> '2'", '2'.isalpha())
print("\nExample of isdigit() with", "Only words -> \n\t'abcd'", "abcd".isdigit(),
      "\n\tSpecial characters -> 'ab_cd'", 'ab_cd'.isdigit(),
      "\n\t'Word and Numbers -> abcd123'", 'abcd123'.isdigit(),
      "\n\tFloating String -> '2.0'", "2.0".isdigit(),
      "\n\tInteger as string -> '2'", '2'.isdigit())
print("\nExample of islower() with", "Only words -> \n\t'abcd'", "abcd".islower(),
      "\n\tSpecial characters -> 'ab_cd'", 'ab_cd'.islower(),
      "\n\t'Word and Numbers -> AB_CD'", 'AB_CD'.islower(),
      "\n\tFloating String -> 'ABCD'", "ABCD".islower())
print("\nExample of isupper() with", "Only words -> \n\t'abcd'", "abcd".isupper(),
      "\n\tSpecial characters -> 'ab_cd'", 'ab_cd'.isupper(),
      "\n\t'Word and Numbers -> AB_CD'", 'AB_CD'.isupper(),
      "\n\tFloating String -> 'ABCD'", "ABCD".isupper())

print("\n" + "#"*50)
print("\tString Check for Start and End")
print("#"*50)
print("For any substring we can check for start and end of a given string with functions startswith() and endswith() respectively")
print('Sample variable testString:', testString)
print("Does the string starts with 'This is a' substring:", testString.startswith('This is a'))
print("Does the string ends with 'This is a' substring:", testString.endswith('This is a'))
print("Does the string starts with 'python string functions' substring:", testString.startswith('python string functions'))
print("Does the string ends with 'python string functions' substring:", testString.endswith('python string functions'))

print("\n" + "#"*50)
print("\tString Formatting")
print("#"*50)
# Strings in Python can be formatted with the use of format() method which is a very versatile and powerful tool
# for formatting Strings. Format method in String contains curly braces {} as placeholders which can hold arguments
# according to position or keyword to specify the order.
FormatedString1 = "{} {} {}".format("Beginner", "in", "Python")
print("Function format() prints in default order:", FormatedString1) # Beginner in Python
FormatedString2 = "{1} {0} {2}".format("Beginner", "in", "Python")
print("Function with numerical format() prints in provided order:", FormatedString2) # in Beginner Python
FormatedString3 = '{a} {b} {c}'.format(a = 'Abba', b = 'Dabba', c = 'Jabba')
print("String in order of Keywords:", FormatedString3)
