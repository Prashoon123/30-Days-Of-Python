# Day 6 Exercises

# Task 1
empty_tuple = tuple() # constructor method

# Task 2
brothers = ("Mike", "Bobby", "Floyd")
sisters = ("Lara", "Wendy", "Sally")

# Task 3
siblings = brothers + sisters

# Task 4
num_of_siblings = len(siblings)

# Task 5
family_members = list(siblings)
family_members.append("Dad")
family_members.append("Mom")

print(family_members)

# Task 6 - Level 2 starts here
siblings, parents = family_members[:6], family_members[6:]
print("Siblings >>>", siblings)
print("Parents >>>", parents)

# Task 7
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
vegetables = ("potato", "onion", "carrot", "lettuce", "cucumber")
animal_products = ("meat", "eggs", "milk", "cheese", "yoghurt")

food_stuff_tp = fruits + vegetables + animal_products

# Task 8
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Task 9
middle_items = food_stuff_tp[5:10]
print(middle_items)

# Task 10
first_items = food_stuff_lt[:3]
print(first_items)

last_items = food_stuff_lt[-3:]
print(last_items)

# Task 11
del food_stuff_tp

# Task 12
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)