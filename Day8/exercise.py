# Day 8 Exercises

# Task 1
dog = dict()

# Task 2
dog["color"] = "brown"
dog["name"] = "Swift"
dog["breed"] = "Golden Retriever"
dog["legs"] = 4
dog["age"] = 5

print(dog)

# Task 3
student = {
    "first_name": "Prashoon",
    "last_name": "Bhattacharjee",
    "gender": "Male",
    "age": 14,
    "marital_status": "Single",
    "skills": ["Programming", "Investing", "Fitness"],
    "country": "India",
    "city": "Mumbai",
    "address": {
        "street": "Altamount Road",
        "building_name": "Antilia"
    }
}

# Task 4
print(len(student))

# Task 5
print(student["skills"])

# Task 6
student["skills"].append("Communication")
print(student)

# Task 7
keys = student.keys()
print(keys)

# Task 8
values = student.values()
print(values)

# Task 9
del student["skills"]
print(student.items())

# Task 10
del dog["legs"]

# Task 11
del student

