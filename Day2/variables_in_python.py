# variables in python

first_name = "Prashoon" # string
last_name = "Bhattacharjee"
country = "India"
city = "Mumbai"
age = 14 # integer
is_married = False # boolean
skills = ["Trading", "Coding", "Football"] # list

person_info = {
    "firstname": "Prashoon",
    "lastname": "Bhattacharjee",
    "country": "India",
    "city": "Mumbai",
}

# Printing the values stored in variables

print("First name: ", first_name)
print("First name length: ", len(first_name))
print("Last name: ", last_name)
print("Last name length: ", len(last_name))
print("Country: ", country)
print("City: ", city)
print("Age: ", age)
print("Married: ", is_married)
print("Skills: ", skills)
print("Personal info: ", person_info)

# declaring multiple variables in one line

first_name, last_name, country, age, is_married = "Prashoon", "Bhattacharjee", "India", 14, False

print(first_name, last_name, country, age, is_married)
print("First name: ", first_name)
print("Last name: ", last_name)
print("Country: ", country)
print("Age: ", age)
print("Married: ", is_married)

# Python developers use snake_case convention

# For e.g. variable name is macbook laptop

# so i'll have to wrote macbook_laptop

# this isn't allowed - macbook-laptop
# this too - macbook@laptop
# even this - macbook$laptop
# this too - 23macbookpatop