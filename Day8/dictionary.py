# creating an empty dictionary
my_dict = {}

# dictionary with values
fruits = {"fruit1": "orange", "fruit2": "apple", "fruit3": "mango"}

person = {
    "first_name": "Prashoon",
    "last_name": "Bhattacharjee",
    "age": 14,
    "country": "India",
    "is_married": False,
    "skills": ["Programming", "Investing", "Fitness"],
    "address": {
        "street": "10 Downing Street",
        "zipcode": "12345"
    }
}

# finding the length of a dictionary
print(len(fruits))  # 3

# accessing dictionary items
first_name = person["first_name"]
print(first_name)  # Prashoon

# adding items to a dictionary
person["social_security_number"] = "ABC123"
print(person)

# modifying items in a dictionary
person["age"] = 14 + 1
print(person)

# checking if a key is present in a dictionary
print("first_name" in person)  # True
print("bank_account" in person)  # False

# removing key and value pairs in a dictionary
person.pop("social_security_number")
person.popitem()  # removes the last inserted item
del person["is_married"]

print(person)

# converting a dictionary to a list
print(person.items())  # returns a list of tuples

# deleting a dictionary
del person

# copying a dictionary
american_politicians = {"President": "Joe Biden", "Vice President": "Kamala Harris",
                        "Majority Leader": "Chuck Schumer", "Minority Leader": "Mitch McConnell"}
american_leadership = american_politicians.copy()

# getting dictionary keys
keys = american_politicians.keys()
print(keys)

# getting dictionary values as a list
values = american_politicians.values()
print(values)
