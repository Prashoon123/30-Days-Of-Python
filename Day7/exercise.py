# Day 7 Exercises

it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Task 1
print(len(it_companies))

# Task 2
it_companies.add('Twitter')
print(it_companies)

# Task 3
it_companies.update({'Tesla', 'SpaceX'})
print(it_companies)

# Task 4
it_companies.pop()
print(it_companies)

# Task 5
# if company is not present then error will be thrown
it_companies.remove('IBM')
print(it_companies)

# if company is not present then no error will be thrown
it_companies.discard('Tesla')
print(it_companies)

# Task 6 - Level 2 starts here
A.union(B)

# Task 7
A.intersection(B)

# Task 8
A.issubset(B)

# Task 9
A.isdisjoint(B)

# Task 10
A.union(B) == B.union(A)

# Task 11
A.symmetric_difference(B)

# Task 12
del A
del B

# Task 13 - Level 3 starts here
set_ages = set(age)

if len(set_ages) == len(age):
    print("The lengths are equal")
else:
    print("The lengths are not equal")

# Task 14
sentence = "I am a teacher and I love to inspire and teach people"
individual_words = sentence.split()

print("Number of unique words: ", len(individual_words))
