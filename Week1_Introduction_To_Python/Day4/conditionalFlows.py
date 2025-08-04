# Conditional statements are fundamental to programming as they allow the execution of specific code
# blocks based on certain conditions.
# In Python, the if-else statement is a powerful tool for incorporating decision-making logic into your programs.

# The if, elif and else Statement:
# Syntax below:
x = int(input("Please Enter any integer value: "))
if x > 0: # if followed by a condition and then with a ':'
# Indented statement just after condition forms its conditional statement codeblock
    print(x, 'is greater than 0. Hence its a positive integer')
    #   Nested if/elif/else should carry same indentation as other lines under conditional block
    if x % 2 == 0 and x > 10:
        print(x, "is an even number which is greater than 10")
    elif x % 2 != 0:
        print(x, "is an odd number")
    print("Further simulation of positive number code execution.......")
elif x < 0: # elif followed by a condition and then with a ':'
    print(x, 'is lesser than 0. Hence its a negative integer')
    print("Simulation of negative number code execution.......")
else:
    print(x, 'is zero. Hence its neither a negative nor positive number')
    print("Of all the numbers you could enter, you wanted to put zero??🧐")

# Short-hand if-else statement
# Single line both condtions and conditional statements can be executed
age = 19
isAdult = True if age >= 18 else False
print(f"Will a person with {age} be considered as an adult: {isAdult}")
print("The end")




