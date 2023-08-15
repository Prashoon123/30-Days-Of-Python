# booleans

print(True)
print(False)

# operators

x = 5

x += 3  # x = x + 3 - addition
x -= 3  # x = x - 3 - subtraction
x *= 3  # x = x * 3 - multiplication
x /= 3  # x = x / 3 - division
x %= 3  # x = x % 3 - modulus
x //= 3  # x = x // 3 - floor division
x **= 3  # x = x ** 3 - exponentiation
# x &= 3  # x = x & 3
# x |= 3  # x = x | 3
# x ^= 3  # x = x ^ 3
# x >>= 3  # x = x >> 3
# x <<= 3  # x = x << 3

# Arithmetic operations in Python
# Integers

print("Addition: ", 1 + 2)
print("Subtraction: ", 51 - 7)
print("Multiplication: ", 71 * 99)
print("Division: ", 5 / 2)  # gives floating number 2.5
print("Division without remainder: ", 5 // 2)
print("Modulus: ", 6 % 7)  # gives the remainder
print("Exponentiation: ", 2**2)  # gives the square of 2

# floating numbers
print("Gravity: ", 9.81)
print("PI: ", 3.142)

# complex number
print("complex number: ", 1 + 1j)
print("multiplying complex num: ", (1+3j) * (5+7j))

# Calculating area of a circle
radius = 10                                 # radius of a circle
# two * sign means exponent or power
area_of_circle = 3.14 * radius ** 2
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         # Adding unit to the weight

# Calculate the density of a liquid
mass = 75  # in Kg
volume = 0.075  # in cubic meter
density = mass / volume  # 1000 Kg/m^3

# comparison operators
print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2

print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False


# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

# is: Returns true if both variables are the same object(x is y)
# is not: Returns true if both variables are not the same object(x is not y)
# in: Returns True if the queried list contains a certain item(x in y)
# not in: Returns True if the queried list doesn't have a certain item(x in y)

# True - because the data values are the same
print('1 is 1', 1 is 1)
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh')  # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh')  # False - there is no uppercase B
# True - because coding for all has the word coding
print('coding' in 'coding for all')
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

# logical operators
print(3 > 2 and 4 > 3)  # True - because both statements are true
print(3 > 2 and 4 < 3)  # False - because the second statement is false
print(3 < 2 and 4 < 3)  # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False)  # False
