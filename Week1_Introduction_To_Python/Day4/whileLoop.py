counter, limit = 5, 1
print("The count-down begins:")
while limit >= counter:
    print(limit, '...')
    limit += 1

# If condition is always true, then the Python execution steps into infinite loop

# Similar to java, the continue statement, helps skip the further execution of a code block
# in loop and proceed for next iteration
counter = 5
while counter >= limit:
    if(counter % 2 == 0):
        print(f"The value {counter} is even. Going to next iteration")
        counter -= 1
        continue
    print(f"The statement printed without continue with counter value: {counter}")
    counter -=1

# Break statement for loops
age = 18
while True:
    print("Simulation of some code execution......")
    if(age < 18):# Not an adult
        print("Only adults (age equal or greater than 18 years) are allowed to cast the vote")
        break
    print("You're eligible to cast the vote. Please select any one option to which you would like to cast your vote")
    print(".....<List of all parties which are ambitiously planning to rob public money>....")
    print("End of list. ")
    break
