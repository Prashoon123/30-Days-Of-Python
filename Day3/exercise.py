import math

# Day 3 Exercise

age = 14
height = 167.5
complex_val = 1+5j

# triangle area
base = input("Please enter the length of the base of the triangle: ")
height = input("Kindly enter the height of the triangle: ")
area_of_triangle = (int(base) / 2) * int(height)

print("The area of the triangle is: ", area_of_triangle)

# perimeter of triangle
side_a, side_b, side_c = input("Please enter the length of Side A: "), input(
    "Please enter the length of Side B: "), input("Please enter the length of Side C: ")
perimeter_of_triangle = side_a + side_b + side_c

# area of rectangle
rect_length = input("Kindly enter the length of the rectangle: ")
rect_width = input("Kindly enter the width of the rectangle: ")

area_of_rect = int(rect_length) * int(rect_width)
perimeter_of_rect = 2 * (int(rect_length) + int(rect_width))


# area of circle
circle_radius = input("Kindly enter the radius of the circle: ")
area_of_circle = 3.142 * int(circle_radius)**2
circumference_of_circle = 2 * 3.142 * int(circle_radius)

# linear equations
# equation - y = 2x - 2
slope = 2
intercept_y = -2

# coordinates of the point
x1, y1 = 2, 2
x2, y2 = 6, 10

slope_2 = (y2 - y1) / (x2 - x1)
distance = math.sqrt((y2 - y1)**2 + (x2 - x1)**2)

print("Euclidean distance: ", distance, " units")

# comparing both slopes
print("Task 8 slope == Task 9 slope", slope == slope_2)

# comparing lengths

str_1 = "python"
str_2 = "dragon"

print("Length of str_1 != Length of str_2", len(str_1) == len(str_2))

found = "on" in str_1 and "on" in str_2
print('"On" exists in both the strings: ', found)

sentence = "I hope this course is not full of jargon."
jargon_exists = "jargon" in sentence
print("Does 'jargon' exist in the sentence? ", jargon_exists)

if "on" in str_1 and "on" in str_2:
    print("'on' is present in both the strings")
else:
    print("'on' is not present in both the strings")

str_1_to_float = float(len(str_1))
print(str(str_1_to_float))

# checking if the number is even
num = float(input("Check if the number is even: "))

if num % 2 == 0:
    print("This number is even")
else:
    print("This number isn't even")

print("Is the floor division value of 7 / 3 is equal to the int converted value of 2.7: ", int(7//3) == 2.7)

print(type(10) == type("10"))

print(int(9.8) == 10)

# wage of the person
hours = input("Enter the number of hours that you work for: ")
hours_num = int(hours)

hourly_rate = input("Enter your hourly rate: ")
hourly_rate_num = int(hourly_rate)

weekly_earning = hours_num * hourly_rate_num
print("Your weekly earning: $", weekly_earning)

# number of years to seconds
years_lived = input("Enter the number of years that you have lived for: ")
years_lived_num = int(years_lived)

seconds_lived = years_lived_num * 3.156e+7
print("You have lived for: ", seconds_lived, " seconds")

# preparing the table

def print_table(rows):
    for i in range(1, rows + 1):
        print(i, 1, i, i**2, i**3)


print_table(5)
