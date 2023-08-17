# Day 4 Exercises

# Task 1
strings = ["Thirty", "Days", "Of", "Python"]
strings_concatenated = " ".join(strings)

print(strings_concatenated)

# Task 2
strings = ["Coding", "For", "All"]
strings_concatenated = " ".join(strings)

print(strings_concatenated)

# Task 3
company = "Coding For All"

# Task 4
print(company)

# Task 5
len_company = len(company)
print(len_company)

# Task 6
company_uppercase = company.upper()
print(company_uppercase)

# Task 7
company_lowercase = company.lower()
print(company_lowercase)

# Task 8
company_capitalize = company.capitalize()
company_title = company.title()
company_swapcase = company.swapcase()

print(company_capitalize)
print(company_title)
print(company_swapcase)

# Task 9
company_sliced = company.strip("Coding")
print(company_sliced)

# Task 10
print(company.index("Coding"))

# Task 11
company_replaced = company.replace("Coding", "Python")
print(company_replaced)

# Task 12
company_replaced_2 = company_replaced.replace("All", "Everyone")
print(company_replaced_2)

# Task 13
print(company.split())

# Task 14
big_tech = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(big_tech.split(","))

# Task 15
index_zero_company = print(company[0])

# Task 16
index_last_company = print(company[-1])

# Task 17
index_tenth_company = print(company[10])

# Task 18
acronym_company_replaced_2 = "".join(
    word[0] for word in company_replaced_2.split())
print(acronym_company_replaced_2)

# Task 19
acronym_company = "".join(firm[0] for firm in company.split())
print(acronym_company)

# Task 20
index_of_C = company.index("C")
print(index_of_C)

# Task 21
index_of_F = company.index("F")
print(index_of_F)

# Task 22
rindex_of_I = "Coding For All People".rindex("l")
print(rindex_of_I)

# Task 23
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.rindex("because"))

# Task 24
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.rindex("because"))

# Task 25
print(sentence.replace("because", ""))

# Task 26
print(sentence.index("because"))

# Task 27
print(sentence.replace("because", ""))

# Task 28
print(company.startswith("Coding"))

# Task 29
print(company.endswith("coding"))

# Task 30
sentence = "   Coding For All      "
print(company.strip(" "))

# Task 31
var_1 = "30DaysOfPython"
var_2 = "thirty_days_of_python"

print(var_1.isidentifier())  # False
print(var_2.isidentifier())  # True

# Task 32
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" # ".join(python_libraries))

# Task 33
extended_sentence = '''I am enjoying this challenge.
I just wonder what is next.'''

print(extended_sentence)

# Task 34
print("Name\t\tAge\t\tCountry\t\tCity")
print("Prashoon\t14\t\tIndia\t\tMumbai")

# Task 35
radius = 10
pi = 3.14
area = pi * radius ** 2
formatted_string = 'The area of a circle with a radius {} is {}.'.format(radius, int(area)) # 2 digits after decimal
print(formatted_string)

# Task 36
a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) 
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))