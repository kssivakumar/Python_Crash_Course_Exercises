# 6.1 Person: use a dictionary to store information about a person you know. Store their first name, last name, age,
# and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of
# information stored in your dictionary.

names = {'first_name' : 'Dylan', 'last_name' : 'Zenmaster', 'age' : 23, 'city' : 'San Francisco'}

print({v for k,v in names.items()})


# 6.2 Favorite Number: Use a dictionary to store people's favorite numbers. Think of five names, and use them as keys in your
# dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person's
# name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

numbers = {'dylan' : 23, 'austyn' : 13, 'jake' : 35, 'brice' : 62, 'devon' : 48}

for k,v in numbers.items():
    print(k,v)

# 6.3 Glossary: A python dicitonary can be used to model an actual dictionary. However, to avoid confusion, let's call it
# a glossary.
# - Think of five programming words you've learned about in the previous chapters. Use these words as the keys in your
# glossary, and then store their meanings as values.
# - Print each word and it's meaning as neatly formatted output. You might print the word followed by a colon and then its
# meaning , or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n)
# to insert a blank line between each word-meaning pair in your output.

glossary = {'.items()' : 'returns all key-value pairs in teh dictionary', '.keys()' : 'returns all the keys in the dictionary', 
            'print()' : 'prints what you specify to the console', '.format' : 'used to format the output of a program', 'return' : 
            'Must be used in a function in order for that function to return a value when called.'}

for k, v in glossary.items():
    print(k + ': ',v)

# 6.4 Glossary 2: Now that you know how to loop through a dictionary, clean up the code from exercise 6.3 by replacing 
# your series of print statements with a loop that runs through the dictionary's keys and values. When you're sure that
# your loop works, add five more python terms to your glossary. When you run your program again, these new words and meanings
# should automatically be included in the output.

glossary = {'.items()' : 'returns all key-value pairs in teh dictionary', '.keys()' : 'returns all the keys in the dictionary',
            'print()' : 'prints what you specify to the console', '.format' : 'used to format the output of a program', 
            'return' : 'Must be used in a function in order for that function to return a value when called.', 
            '.choice()' : 'function in the random module that prints a value with the probability of 0.5', 
            'while':'One of pythons different loop functions', 'for':'another one of pythons loop functions',
            'bool': 'value of either True or False', '>':'one of pythons many equality operators'}

for k, v in glossary.items():
    print(k + ': ',v)

# 6.5 Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair
# might be 'nile' : 'egypt'
# - Use a loop to print a sentence about each river, such as 'The Nile runs through Egypt'
# - Use a loop to print the name of each river included in the dictionary.
# - Use a loop to print the name of each country in the dictionary.

rivers = {'Nile':'Egypt', 'Amazon':'Brazil', 'Yangtze':'Asia'}

for k,v in rivers.items():
    print('The ' + k + ' river flows through ' + v)

# 6.6 Polling: Use the code in favorite_languages.py
# - Make a list of people who should take the favorite languages poll. Include some names that are already in the dicitonary
# and some that are not.
# - Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking 
# them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.

favorite_languages = {'Jen':'Python', 'Sarah':'C', 'Edward':'ruby', 'Phill':'Python', 'Jake':'', 'Brice':'', 'Dylan':''}

for k,v in favorite_languages.items():
    if v != '':
        print(k + ' Thank you for taking our poll!')
    else:
        print(k + ' Please consider taking our poll!')


# 6.7 People: Start with the program you wrote for exercise 6.1. Make two new dicitonaries representing different people,
# and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list,
# print everything you know about each person.

person1 = {'first_name' : 'Dylan', 'last_name' : 'Zenmaster', 'age' : 23, 'city' : 'San Francisco'}


person2 = {'first_name' : 'Jake', 'last_name' : 'Zen', 'age' : 24, 'city' : 'LA'}


person3 = {'first_name' : 'Brice', 'last_name' : 'Man', 'age' : 24, 'city' : 'San Francisco'}


people = [person1, person2, person3]

for item in people:
    if item == person1:
        print(person1['first_name'] + ' ' + person1['last_name'] + ' is ' + str(person1['age']) + 
              ' years old and lives in ' + person1['city'])
    elif item == person2:
        print(person2['first_name'] + ' ' + person2['last_name'] + ' is ' + str(person2['age']) + 
              ' years old and lives in ' + person2['city'])
    else:
        print(person3['first_name'] + ' ' + person3['last_name'] + ' is ' + str(person3['age']) + 
              ' years old and lives in ' + person3['city'])


# 6.8 Pets: Make several dicitonaries, where the name of each dictionary is the name of a pet. In each dictionary, include
# the kind of animal and the owner's name . Store these dictionaries in a list called pets. Next, loop through your list and 
# as you do print everything you know about each pet.

cinder = {'owner_name' : 'Dylan', 'animal' : 'cat'}

sparrow = {'owner_name' : 'Jake', 'animal' : 'cat'}

ghost = {'owner_name' : 'Brice', 'animal' : 'dog'}

pets = [cinder, sparrow, ghost]

for pet in pets:
    print(pet['owner_name'] + ' owns a ' + pet['animal'])
    
# This is a simpler way of doing exercise 6.7 as well. Just thoght I would add both ways in here.    


# 6.9 Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dicitonary, and
# store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name
# a few of their favorite places. Loop through the dictionary, and print each person's name and their favorite places.

favorite_places = {'Jake': 'Italy', 'Brice': 'Australia', 'Dylan': 'San Francisco'}

for k,v in favorite_places.items():
    print(k + "'s favorite place in the world is " + v)

# 6.10 Favorite Numbers: Modify your program from exercise 6.2 so each person can have more than one favorite number. Then
# print each person's name along with their favorite numbers.

numbers = {'dylan' : '23 and 22', 'austyn' : '13 and 45', 'jake' : '35 and 21', 'brice' : '62 and 49', 'devon' : '48 and 98'}

for k,v in numbers.items():
    print(k + "'s favorite numbers are " + v)

# 6.11 Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary 
# of information about each city and include the country that the city is in, its approximate population, and one fact 
# about that city. The keys for eack city's dictioanry should be something like country, population, and fact. Print the name 
# of each city and all information you have stored about it.

cities = {'San Francisco': {'Country': 'USA', 'Population': 884363, 'Fact': 'Known as the number 1 tech hub in the world'}, 
          'Stockholm': {'Country': 'Sweden', 'Population': 965232, 'Fact': 'Known as the number 2 tech hub in the world'}, 
          'Oakland': {'Country': 'USA', 'Population': 429082, 'Fact': 'Home to the Oakland Raiders and Oakland Athletics'}}

for k, v in cities.items():
    print(k + ', is located in ' + v['Country'] + ' and has a population of ' + str(v['Population']) + 
          '. Also, it is ' + v['Fact'])
