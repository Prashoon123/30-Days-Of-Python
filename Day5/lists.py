# creating a list using the built-in function
empty_lst = list()
print(empty_lst)

# creating a list using []
empty_lst = []
print(empty_lst)

# lists with initial values
languages = ["Java", "Python", "JavaScript"]

print(languages)  # prints the list
print(len(languages))  # prints the length of the list

# list with different data types
user_profile = ["Prashoon Bhattacharjee", 14, {
    "country": "India", "city": "Mumbai"}, False]

print(user_profile)
print(len(user_profile))

# accessing list items - indexing starts with 0
countries = ["India", "France", "USA", "Finland", "Portugal"]
usa = countries[2]

print(usa)  # USA

# accessing list names using negative indexing
finland = countries[-2]

print(finland)  # Portugal

# unpacking list items
names = ["Prashoon", "John", "Frank", "Mark"]
name_1, name_2, *other_names = names

print("Name 1: ", name_1)
print("Name 2: ", name_2)
print("Other names: ", other_names)

# slicing items from a list
fruits = ["Litchi", "Orange", "Watermelon", "Mango"]

all_fruits = fruits[0:]  # takes all the items from the list
litchi_and_orange = fruits[0:2]

print(litchi_and_orange)

watermelon_and_orange = fruits[-3:-1]
print(watermelon_and_orange)

# modifying lists
fruits[1] = "Cherry"

print(fruits)

# checking items in a list
cherry = "Cherry"

does_exist = cherry in fruits
print("The fruit cherry exists in the list, ", does_exist)

# adding items to a list
lst = list()
lst.append("New element")

print(lst)
print(len(lst))

# inserting items into the list - insert(index, item)
lst.insert(1, "New element 2")

print(lst)

# removing items
lst.remove("New element")
print(lst)

# pop method - removes the last item
fruits.pop()

print(fruits)

# removing items using del
lst = ["item1", "item2", "item3"]
del lst[1]  # deletes only a single item

print(lst)

del lst  # deletes the list entirely

# clear - empties the list []
lst = ["index1", "index2", "index3"]

lst.clear()
print(lst)

# copy
fruits_copy = fruits.copy()

print(fruits_copy)

# joining lists - plus operator
list_1 = ["index1", "index2"]
list_2 = ["index3"]

list_3 = list_1 + list_2

print(list_3)

# number line
negative_numbers = [-5, -4, -3, -2, -1]
zero = [0]
positive_numbers = [1, 2, 3, 3, 4, 5]

number_line = negative_numbers + zero + positive_numbers
print(number_line)

# extend method - another method of appending items to the list
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)

print("Integers: ", negative_numbers)

# count - number of times an item appears in the list
languages = ["Spanish", "English", "Italian", "French"]
# How many times does the string "Spanish" get repeated in the list
count = languages.count("Italian")

print(count)

# index - returns the index of the item in the list
french = languages.index("French")

print("Index of french in the 'languages' list: ", french)

# reversing a list
languages = ["Spanish", "English", "Italian", "French"]
languages.reverse()
# ['French', 'Italian', 'English', 'Spanish']
print("Reversed languages: ", languages)

# sort - sorts the list in ascending order
big_tech = ["Meta", "Apple", "Amazon",
            "Microsoft", "Google", "Oracle", "Cisco"]

big_tech.sort(reverse=False)  # sorts the list in ascending order
print(big_tech)

big_tech.sort(reverse=True)  # sorts the list in descending order
print(big_tech)

# sorted - sorts the list without modifying the original list
sorted_big_tech = sorted(big_tech)
print(sorted_big_tech)
