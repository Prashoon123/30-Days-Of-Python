# creating a string

first_string = "A"
print(first_string)

# length of string
print(len(first_string))

# creating a sentence
sentence = "This is a sentence created in Python"
print(sentence)

# creating multiline strings
multiline_string = '''This strings extends
to multiple lines, ain't it cool?!'''

print(multiline_string)

# string concatenation
first_name = "Prashoon"
last_name = "Bhattacharjee"
space = " "

full_name = first_name + space + last_name

print(full_name)

length_of_full_name = len(full_name)
print("This is the length of the name: ", length_of_full_name)

# escape sequences in strings
print("I hope everyone is enjoying the party? \n Are you?")

print("Days\tTopics\tExercises")  # adding a tab space or 4 spaces

print("Day1\t5\t5")
print("Day2\t6\t20")
print("Day3\t3\t6")
print("Day4\t4\t16")
print("This is a backslash symbol (\\)")

# string formatting
language = "Python"

formatted_string = print("I am %s %s. I am learning %s" %
                         (first_name, last_name, language))

# strings and numbers
radius = 5
pi = 3.142
area = pi * radius**2

formatted_string_1 = print("The area of the circle with a radius of %d is %.1f" % (
    radius, area))  # the one represents the number of decimals

python_libraries = ["Django", "Flask", "Numpy", "Matplotlib", "Pandas"]
formatted_string_2 = print(
    "The following are python libraries: %s" % (python_libraries))

# style string formatting str.format
first_name = first_name
last_name = last_name
language = language

formatted_string_3 = "I am {} {}. I am learning {}".format(
    first_name, last_name, language)
print(formatted_string_3)

a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))

# limits it to two digits after decimal
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formatted_string_4 = 'The area of a circle with a radius of {} is {:.2f}'.format(
    radius, area)  # 2 digits after decimal
print(formatted_string_4)

# string interpolation
a = a
b = b

print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

# python strings as sequences of characters
language = language

a, b, c, d, e, f = language
print(a)  # P
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n

# assigning characters in strings by index
third_letter = language[2]  # counting starts from 0
print("Third letter from the string 'Python': ", third_letter)

second_letter = language[-5]  # negative indexing works in the opposite manner
print(second_letter)

# sliced python strings
headphone = "BOAT"
# first three characters of the string 'headphones'
first_three_chars = headphone[0:3]
print(first_three_chars)

# reversing a string
headphone_reversed = headphone[::-1]
print(headphone_reversed)

# skipping characters while slicing
language = language
pto = language[0:6:2]
print(pto)

# capitalize
challenge = "thirty days of python"
print(challenge.capitalize())

# count
print(challenge.count("y"))  # y is there 3 times

# ends with
print(challenge.endswith("on"))  # True
print(challenge.endswith("abc"))  # False

# expands tab
challenge = challenge
expanded_challenge = challenge.expandtabs()

print(expanded_challenge)

# find
find_challenge = challenge.find("P")  # -1 which means it doesn't exist
print(find_challenge)
print(challenge.find("p"))  # exists in the 15th position

# rfind - finds the last occurrence of the substring
challenge = challenge
rfind_challenge = challenge.rfind("python")  # 15

# index - locate position of element efficiently
song_name = "Happier By Ed Sheeran"
ed_index = song_name.index("Ed")  # 11

print(ed_index)

# rindex - find last element's position efficiently
song_name = song_name
sheeran_index = song_name.rindex("Sheeran")

print(sheeran_index)  # 14

# isalnum - checks for alphanumeric characters
alpha_num = "ThirtyDaysPython"
print(alpha_num.isalnum())  # True

print(challenge.isalnum())  # False

# isalpha - checks if string elements are alphabet characters (a-z and A-Z)
challenge = challenge

challenge_chars = challenge.isalpha()  # True
print(challenge_chars)

# isdecimal - checks if string is a decimal
challenge = challenge
challenge_decimal = challenge.isdecimal()  # False

print(challenge_decimal)

# isdigit - checks if all characters in a string are numbers
sport_score = "Thirty"
print(sport_score.isdigit())  # False

sport_score = "50"
print(sport_score.isdigit())  # True

# isnumeric - checks if the elements of the string are numbers or related to numbers
numeric_val = "10"
print(numeric_val.isnumeric())  # True

numeric_val = "Thirty"
print(numeric_val.isnumeric())  # False

# isidentifier - checks if the string is a valid variable name
variable_name = "30Days"
print(variable_name.isidentifier())  # False as it starts with a number

variable_name = "days_thirty"
print(variable_name.isidentifier())  # True

# islower - checks if all the characters in string are of lower case
song_app = "spotify"
print(song_app.islower())  # True

song_app = "Apple Music"
print(song_app.islower())  # False

# isupper - checks if all the characters are uppercase
laptop = "DELL"
print(laptop.isupper())  # True

laptop = "Macbook"
print(laptop.isupper())  # False

# join
web_tech = ["HTML", "CSS", "JS", "REACTJS"]
concatenated_text = " ".join(web_tech)

print(concatenated_text)

# strip - removes all given characters starting from the beginning and end of the string
show_name = "House Of Cards"

print(show_name.strip("Ho"))  # use Of Cards

# replace
statement = "I am your teacher"

print(statement.replace("teacher", "coding buddy"))  # I am your coding buddy

# split - splits the string, using given string or space as a separator
rand_string = "Lorem Ipsum Dolor"
print(rand_string.split("Ipsum"))

# title - returns a title cased string
rand_string_2 = "lorem ipsum dolor"
print(rand_string_2.title())  # Lorem Ipsum Dolor

# swapcase - converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
bottle_type = "This bottle is made up of copper"

print(bottle_type.swapcase())  # tHIS BOTTLE IS MADE UP OF COPPER

# startswith - checks if the string starts with a specific string
bottle_type = "Bottle consists of gold and ruby"

print(bottle_type.startswith("Diamond"))  # False
print(bottle_type.startswith("Bottle"))  # True
