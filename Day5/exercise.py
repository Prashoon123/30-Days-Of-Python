# Day 5 - Exercises

# Task 1
lst = list()

# Task 2
lst = ["item1", "item2", "item3", "item4", "item5"]

# Task 3
len_lst = len(lst)
print(len_lst)

# Task 4
first_item = lst[0]
middle_item = lst[2]
last_item = lst[-1]

# Task 5
mixed_data_types = ["Prashoon Bhattacharjee", 14, "166cm",
                    False, {"country": "India", "city": "Mumbai"}]

# Task 6
it_companies = ["Facebook", "Google", "Microsoft",
                "Apple", "IBM", "Oracle", "Amazon"]

# Task 7
print(it_companies)

# Task 8
print(len(it_companies))  # No of companies in the list

# Task 9
first_company = it_companies[0]
middle_company = it_companies[3]
last_company = it_companies[-1]

# Task 10
it_companies[2] = "Cisco"
print(it_companies)

# Task 11
it_companies.append("Nvidia")  # Add to the end of the list

# Task 12
# Add to the middle of the list
it_companies.insert(int(len(it_companies)/2), "AMD")

# Task 13
it_companies[2] = it_companies[2].upper()  # Change the third item to uppercase
print(it_companies)

# Task 14
formatted_it_companies = "#; ".join(it_companies)
print(formatted_it_companies)

# Task 15
microsoft_exists = "Microsoft" in it_companies
print(microsoft_exists)

# Task 16
it_companies.sort()  # Sort the list in ascending order
print(it_companies)

# Task 17
it_companies.reverse()  # Change the entire order of the list
print(it_companies)

# Task 18
it_companies = it_companies[3:]  # Remove the first 3 companies from the list
print(it_companies)

# Task 19
it_companies = it_companies[:-3]  # Remove the last 3 companies from the list
print(it_companies)

# Task 20
# Remove all the companies in the middle of the list
it_companies = it_companies[1:-1]

# Task 21
it_companies = it_companies  # Remove the first company from the list
print(it_companies[1:])

# Task 22
it_companies.clear()  # Clear the list
print(it_companies)

# Task 23
del it_companies  # Delete/Destroy the list

# Task 24
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

full_stack = front_end + back_end  # Join the two lists

# Task 25
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")

print(full_stack)

# Task 26 - Level 2 Tasks Start Here
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()  # Sort the list and find the min and max age
min_age = ages[0]
max_age = ages[-1]

print("Min age: ", min_age)
print("Max age: ", max_age)

ages.append(min_age)  # Add the min age again to the list
ages.append(max_age)  # Add the max age again to the list

print(ages)

median_age = ages[int(len(ages)/2)]
print("Median age: ", median_age)

average_age = sum(ages)/len(ages)
print("Average age: ", average_age)

range_of_ages = max_age - min_age
print("Range of ages: ", range_of_ages)

# compare the value using abs method
print(abs(min_age - average_age) < abs(max_age - average_age))

# Task 27
countries = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Cape Verde',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombi',
    'Comoros',
    'Congo (Brazzaville)',
    'Congo',
    'Costa Rica',
    "Cote d'Ivoire",
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor (Timor Timur)',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia, The',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea, North',
    'Korea, South',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Macedonia',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia and Montenegro',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Swaziland',
    'Sweden',
    'Switzerland',
    'Syria',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe',
]

middle_country = countries[int(len(countries)/2)]
print("Middle country: ", middle_country)

# Task 28
first_half = countries[:int(len(countries)/2)+1] # First half of the countries
second_half = countries[int(len(countries)/2)+1:] # Second half of the countries

# Task 29
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

china, russia, usa, *scandic_countries = countries