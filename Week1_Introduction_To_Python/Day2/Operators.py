# In Python programming, Operators in general are used to perform operations on values and variables. These are standard symbols used for logical and arithmetic operations. In this article, we will look into different types of Python operators.
#
# OPERATORS: These are the special symbols. Eg- + , * , /, etc.
# OPERAND: It is the value on which the operator is applied.

# Arithmetic Ops:
a = 10
b = 3
print("**************************************************")
print("****************    Arithmetic    ****************")
print("**************************************************")
print("a:", a, "& b:", b)
print("a + b:", a+b) # 13
print("a - b:", a-b) # 7
print("a * b:", a*b) # 30
print("a / b:", a/b) # 3.3333333333333335
print("Floor Division -> a // b:", a//b) # 3
print("a % b:", a%b) # 1
print("a^b or (Exponentiation) -> a ** b:", a**b) # 1000
print("Absolute value of any number can be given by abs() func. For Example:\nabs(-35) =", abs(-35)) # 35
# If we try for arithmetic operations on boolean True and False, they inherit 1 and 0 value respectively
# Hence True + True = 1 + 1 = 2
print("\nArithmetic values for True(1) and False(0):", "\nTrue + True:", True + True,
      "\nFalse + False:", False + False,"\nTrue * False:", True * False)
print("\n\nIMPORTANT NOTE: All other operators have  ## Left to Right ##  calculating process but,")
print("for exponentiation or ** operator alone the calculation happens from  ## Right to Left ##")
print("For example: 2**2**-1, is calculated as: ")
print("2**2**-1 = 2**(2** -1) = 2**(1/2) = 2**(0.5) = Square Root of 2 = 1.41...")
print("Proof of 2**2**-1 is square root", 2**2**-1)
# Comparison
print("\n\n**************************************************")
print("****************    Comparison    ****************")
print("**************************************************")
# a: 10 & b: 3
print("a:", a, "& b:", b)
print("a > b", a > b)
print("a < b", a < b)
print("a == b", a == b)
print("a != b", a != b)
print("a >= b", a >= b)
print("a <= b", a <= b)

# Logical
print("\n\n*************************************************")
print("*****************    Logical    *****************")
print("*************************************************")
a = True
b = False
print("a:", a, "& b:", b)
print("a and b", a and b)
print("a or b", a or b)
print("not a", not a)
print("not b", not  b)
print("\nIMPORTANT NOTE: Logical operators perform short-circuiting operation by default,")
print("similar to the || and && operators in Java.\n"
      "These operators are also used to perform operations on non-boolean values."
      "For Example: Take an empty string and assign it to another while using (or) along with a non-empty literal")
s1 = ""
s2 = s1 or "Some_Default_String"
print("s2:",s2) # Prints Some_Default_String as s1 is empty and by default sets the non-empty literal value
# In the same way, we can assign a numerical value to a variable based on validation with or
# As long as the number has any positive or negative value, the 'or' operator will not let 0 to be assigned
num1 = 0
num2 = num1 or 10
num3 = num1 or -10.0
num4 = num1 or 0.0
print("num2:", num2) # 10
print("num3:", num3) # -10.0
print("num4:", num4) # 0.0


# Bitwise
print("\n\n*************************************************")
print("*****************    Bitwise    *****************")
print("*************************************************")
a = 10
b = 4
c = 11

print("\nIMPORTANT NOTE: To convert integers into bits or vice-versa, Python provides in-built functions\n"
      "Example: bin(<integer>). This prints with prefix 0b to signify that the literal is a binary value")
bin_a = bin(a)
print("bin_a = bin(a)", bin_a) # 0b1010
print("Binary bin_a converting to decimal/integer", int(bin_a,2)) # 10
print("a:", a, "& b:", b) # 10 & 4
print("a & b", a & b) # 0
print("a | b", a | b) # 14
print("~a", ~a) # -11
print("bin(a)", bin(a), "\tIts type: ", type(bin(a))) #
print("bin(~a)", bin(~a)) # -0b1100
print("~b", ~b) # -5
print("~c", ~c) # -12
print("bin(c)", bin(c)) # 0b1011
print("bin(~c)", bin(~c)) # -0b1100
# The exclusive-or/xor/^ operator is used to deduce a <intersection> b value from its respective binaries
# The xor works in this way: if both the bits are SAME then 0, else 1
# For example 0 ^ 0 = 0, 1 ^ 1 = 0, 0 ^ 1 = 1 & 1 ^ 0 = 1
print("a ^ b", a ^ b) # 14

# Right shift Operator is used to shift existing bits by the mentioned number to the right. For example
# binary of 5 is 0101, 5 >> 1 = 2, since right shifting bits by ONE spot gives -> 0010
# Similarly, binary of 7 is 0111, 7 >> 1 = 3, since the binary equivalent of result would be 0011 which is 3 in decimal
# Similarly, binary of 10 is 01010, 10 >> 2 = 2, right shifting bits by TWO spot gives 0010 which is 2 in decimal
# Similarly, binary of 10 is 01010, 10 >> 3 = 1, right shifting bits by THREE spot gives 00010 which is 1 in decimal
print("5 >> 1", 5 >> 1) # 2
print("7 >> 1", 7 >> 1) # 3
print("a >> 2", a >> 2) # 2
print("a >> 3", a >> 3) # 1
# Left shift Operator is used to shift existing bits by the mentioned number to the left. For example
# binary of 5 is 0101, 5 << 1 = 10, since right shifting bits by ONE spot gives -> 01010
# Similarly, binary of 7 is 0111, 7 << 1 = 14, since the binary equivalent of result would be 01110 which is 14 in decimal
# Similarly, binary of 10 is 01010, 10 << 2 = 2, left shifting bits by TWO spot gives 0101000 which is 40 in decimal
# Similarly, binary of 10 is 01010, 10 << 3 = 1, left shifting bits by THREE spot gives 01010000 which is 80 in decimal
print("5 << 1", 5 << 1) # 10
print("7 << 1", 7 << 1) # 14
print("a << 2", a << 2) # 40
print("a << 3", a << 3) # 80
print("\nIMPORTANT NOTE: If we notice the the left shift << operator generally doubles the current value\n"
      "And the right shift >> generally gives a floor division by 2")

# Assignment
print("\n\n****************************************************")
print("*****************    Assignment    *****************")
print("****************************************************")
b = a
print("a:", a, "& b:", b) # a: 10 & b: 10
b += a
print("b", b)
b -= a
print("b -= a", b)
b *= a
print("b *= a", b)
b /= a
print("b /= a", b) # b /= a 10.0 -> Gives floating value as result by default
# b <<= a
# print("b <<= a", b)
# print("b", b)


# Identity
print("\n\n*************************************************")
print("****************    Identity    *****************")
print("*************************************************")
# In Python, ## is ## and ## is not ## are identity operators which ae used to check if the variables/literal values are
# on the same part of memory. This works for literals and None value but not for containers/collections
a = 10
b=10
c=a
print("a is b",a is b) # True
print("a is c",a is c) # True
print("a is not c",a is not c) # False
print("b is c",b is c) # True
l1 = [1,2,3]
l2 = [1,2,3]
l3 = None
l4 = None
print("l1 is l2",l1 is l2) # False -> Even if the data structure(here list) has same values
print("l3 is l4",l3 is l4) # True
print("The same way we can try for Boolean as below:\nTrue is False:",True is False) # False
print("True is not False:",True is not False) # True