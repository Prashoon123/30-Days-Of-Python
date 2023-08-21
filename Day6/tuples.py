# creating an empty tuple
empty_tuple = ()
empty_tuple = tuple() # another way of creating an empty tuple, uses the constructor method

# tuple with initial values
new_tuple = ("one", "two", "three")
cars = ("BMW", "Audi", "Mercedes", "Toyota", "Honda")

# finding the length of a tuple
print(len(cars))

# accessing elements in a tuple
mercedes = cars[2]
print(mercedes)

toyota = cars[-2]

# slicing a tuple
names = ("John", "Mary", "Peter", "Jane", "Mark", "Maria")
all_names = names[0:len(names)]

john_to_mark = names[0:5]

# changing tuples to lists as tuples can't be changed we convert them into a list for having edit access
names_list = list(names)
print(names_list)

# checking whether an item is present in the tuple
schools_tuple = ("ABC", "DEF", "GHI", "JKL", "MNO")

bca_present = "BCA" in schools_tuple # False - it is not present in the schools tuple
print(bca_present)

# schools_tuple[0] = "BCA" error - tuples are immutable

# joining tuples
green_house_members = ("Mary", "Frank", "Joe")
red_house_members = ("Rick", "Morty", "Summer")

all_members = green_house_members + red_house_members
print(all_members)

# deleting a tuple
test_tpl = ("one", "two", "three")
del test_tpl # deletes the tuple