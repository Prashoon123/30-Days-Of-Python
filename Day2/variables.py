# Day 2: 30 Days of python programming

first_name = "John"
last_name = "Doe"
full_name = "John Doe"
country = "France"
city = "Paris"
age = 55
year = 2023
is_married = True
is_true = False
is_light_on = True
light_color, light_type, cost = "blue", "led", 599

# type of all the variables
type(first_name)
type(last_name)
type(full_name)
type(country)
type(city)
type(age)
type(year)
type(is_married)
type(is_true)
type(is_light_on)
type(light_color)
type(light_type)
type(cost)

# length of the first_name variable
len(first_name)

# length of last_name variable
len(last_name)

# mathematical functions with num_one and num_two
num_one = 5
num_two = 5

# add
total = num_one + num_two

# subtract
diff = num_one - num_two

# multiplication
product = num_two * num_one

# division
division = num_one / num_two

# modulus
remainder = num_two % num_one

# power and indices
exp = num_one**num_two

# floor division
floor_division = num_one // num_two

# circle related question
area_of_circle = 3.142 * 30**2
circum_of_circle = 2 * 3.142 * 30

input_radius = input("Kindly enter the radius of the circle: ")
area_of_input = 3.142 * int(input_radius)**2

print(area_of_input)

# user object
user = {
    "first_name": first_name,
    "last_name": last_name,
    "country": country,
    "age": age
}

first_name = user["first_name"]
last_name = user["last_name"]
country = user["country"]
age = user["age"]