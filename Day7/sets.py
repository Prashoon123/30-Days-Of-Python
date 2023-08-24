# creating an empty set
empty_set = set()

# creating a set with items
countries = {'India', 'USA', 'UK', 'Canada', 'Australia'}

# getting the length of the set
print(len(countries))

# accessing set items
print("Does India exist in the set? ", 'India' in countries)

# adding items to the set
countries.add('France')
print(countries)

# removing a country from the set
countries.remove("Australia")
print(countries)

removed_item = countries.pop() # removes a random item from the set and returns it
print(removed_item)

# clearing the set
fruits = {"Orange", "Guava", "Apple", "Dragon Fruit"}
fruits.clear()

print(fruits)

# deleting the set
del fruits

# converting list to set
items = ["item1", "item2", "item3", "item4"]
items_to_set = set(items)

print(items_to_set)

# joining sets
affordable_cars = {"Maruti", "Hyundai", "Tata", "Mahindra"}
luxury_cars = {"Mercedes", "BMW", "Audi", "Jaguar"}

cars = affordable_cars.union(luxury_cars)
print(cars)

# inserting sets
fruits_seasonal = {"Mango", "Banana", "Apple", "Grapes"} 
fruits_all = {"Orange", "Guava", "Apple", "Dragon Fruit"}

fruits_seasonal.update(fruits_all) # things will be added to the fruits_seasonal set
print(fruits_all)

# finding common items in sets
names_1 = {"John", "Kane", "Steve", "Rogers"}
names_2 = {"Steve", "Rogers", "Tony", "Stark"}

print(names_1.intersection(names_2)) # {"Steve", "Rogers"} will be printed

# checking subset and superset
sports = {"Football", "Cricket", "Ice Hockey", "Basketball", "Speed Skating"}
winter_sports = {"Ice Hockey", "Speed Skating"}

print(winter_sports.issubset(sports)) # True will be printed
print(sports.issuperset(winter_sports)) # True will be printed

print(winter_sports.issuperset(sports)) # False will be printed
print(sports.issubset(winter_sports)) # False will be printed

# checking the difference
print(sports.difference(winter_sports)) # {"Football", "Cricket", "Basketball"} will be printed
print(winter_sports.difference(sports)) # {} will be printed

# printing unique items from both the sets
tech_companies = {"Google", "Microsoft", "Apple", "Amazon"}
pharma_companies = {"Pfizer", "Johnson & Johnson", "AstraZeneca", "Amazon"}

all_companies = tech_companies.union(pharma_companies)

top_companies = {"Aramco", "Apple", "Amazon", "Microsoft", "Google", "Tesla", "Nvidia", "Facebook"}
print(all_companies.symmetric_difference(top_companies))

# checking if 2 sets have the common items or not
luxury_watches = {"Rolex", "Omega", "Cartier", "Patek Philippe"}
italian_watches = {"Panerai", "Omega", "Cartier", "Patek Philippe"}

print(luxury_watches.isdisjoint(italian_watches)) # False will be printed as some items are common hence this set isn't disjoint

luxury_watches = {"Rolex", "Omega", "Cartier", "Patek Philippe"}
indian_watches = {"Titan", "Fastrack", "Fossil", "Timex"}

print(luxury_watches.isdisjoint(indian_watches)) # True will be printed as no items are common hence this set is disjoint

