# 5.1 Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your prediction for
# the results of each test. Your code should look something like this:

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# - Look closely at your results, and make sure you understand why each line evaluates to True or False
# - Create at least 10 tests. Have at least 5 tests evaulaute to True and another 5 tests evaluate to False.

car = 'audi'
newlst = ['audi', 'mazda', 'nissan']
print("Is car in newlst? I predict True")
print(car in newlst)

letter = 'd'
bike = 'Ducati'
bike.split()
print("Is letter in bike? I predict True")
print(letter in bike.lower())

emptylst = []
print("Is emptylst empty? I predict True")
print([] == emptylst)

add = (5 + 5)
print('Is the value of add equal to 10? I predict True')
print(add == 10)

Jake = 21
print('The legal drinking age is 21. Is Jake old enough to drink? I predict True.')
print(Jake == 21)

word = 'Python'
print('Is word equal to Java? I predict False.')
print(word == 'Java')

nums = [1, 3, 5, 7, 9]
print('Is 10 in nums? I predict False.')
print(10 in nums)

nums = [1, 2, 3, 4, 5]
nums.append(6)
for num in nums:
    if num == 5:
        num *= num
        print(num)
print('Is num equal to 5? I predict False.')
print(num == 5)

coding = 'fun'
print('Is there an ! in coding? I predict False.')
print('!' in coding)

city = '     San Francisco     '
city.lstrip()
print('Is city equal to San Francisco? I predict False.')
print(city == 'San Francisco')


# 5.2 More Conditional Tests: You don't have to limit the number of tests you create to 10. If you want to try more
# comparisons, write more tests. Have at least one True and one False result for each of the following:

# - Tests for equality and inequality with strings

word1 = 'Python'
word2 = 'python'
print(word1.lower() == word2)

word1 = 'Python'
word2 = 'python'
print(word1 == word2)

# - Tests using the lower() function

word1 = 'Python'
word2 = 'python'
print(word1.lower() == word2)

word1 = 'Python'
word2 = 'python'
print(word1.lower() == word2.title())

# - Numerical tests involving equality and inequality , greater than and less than, greater than or equal to, 
# and less than or equal to.

x = 25
y = 30
print(x > y)

x = 25
y = 30
print(x < y)

x = 31
y = 30
print(x >= y)

x = 31
y = 30
print(x <= y)
# - Tests using the and keyword and the or keyword

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst2 = [1, 3, 5, 7, 9]
print(9 in lst1 and 9 in lst2)

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst2 = [1, 3, 5, 7, 9]
print(100 in lst1 or 100 in lst2)

# - Tests whether an item is in a list

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(2 in lst1)

# - Tests whether an item is not in a list

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(10 in lst1)


# 5.3 Alien Colors 1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign
# it a value of 'green', 'yellow', or 'red'.

alien_color = ['green', 'yellow', 'red']

# - Write an if statement to test whether the alien's color is green. If it is, print a message that the player just
# earned 5 points.
# - Write one version of this program that passes the if test and another that fails. (The version that fails will have
# no output).

# I combined the two instructions into one program using the random module becuase I thought it would be fun to have some
# variety and becuase it was just good practice.

import random
alien_color = ['green', 'yellow', 'red']
if random.choice(alien_color) == 'green':
    print('You just earned 5 points!')
else:
    exit()
    
# 5.4 Alien Colors 2: Choose a color for an alien as you did in Exercise 5.3, and write an if - else chain.
# - If the alien's color is green, print a statement that the player just earned 5 points for shooting the alien.
# - If the alien's color is not green, print a statement that the player just earned 10 points.
# Write one version of this program that runs the if block and another that runs the else block.

# Again I am just combining these into one program....

import random
alien_color = ['green', 'yellow', 'red']
if random.choice(alien_color) == 'green':
    print('You just earned 5 points!')
elif random.choice(alien_color) != 'green':
    print('You just earned 10 points!')
    

# 5.5 Alien Colors 3: Turn your if-else chain from 5.4 into an if-elif-else chain.
# - If the alien's color is green, print a message that the player earned 5 points
# - If the alien's color is yello, print a message that the player earned 10 points
# - If the alien's color is red, print a message that the player earned 15 points
# I pretty much did that in the previous example but here is the updated program

import random
alien_color = ['green', 'yellow', 'red']
if random.choice(alien_color) == 'green':
    print('You just earned 5 points!')
elif random.choice(alien_color) == 'yellow':
    print('You just earned 10 points!')
else:
    print('You just earned 15 points!')


# 5.6 Stages Of Life: Write an if-elif-else chain that determines a person's stage of life. Set a value for the lariable age, 
#and then:
# - If the person is less than 2 years old, print a message that the person is a baby.
# - If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
# - If the person is at least 4 years old but less than 13 print a message that the person is a kid.
# - If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
# - If the person is at least 20 years old but less than 65, print a message that the person is an adult.
# - If the person is age 65 or older, print a message that the person is an elder.

# I used the random module here so that when we do not have to hard code the age of the person we are looking. Instead
# we can just run the program and get a random age between 0 and 100 and the program will automatically tell us what stage
# of life they are in.

import random
age = range(101)
if random.choice(age) < 2:
    print('This person is a baby.')
elif random.choice(age) >= 2 and random.choice(age) < 4:
    print('This person is a toddler.')
elif random.choice(age) >= 4 and random.choice(age) < 13:
    print('This person is a kid.')
elif random.choice(age) >= 13 and random.choice(age) < 20:
    print('This person is a teenager.')
elif random.choice(age) >= 20 and random.choice(age) < 65:
    print('This person is an adult.')
else:
    print('This person is an elder.')


# 5.7 Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check
# for certain 
# fruits in your list.
# - Make a list of your favorite fruits and call it favorite_fruits.
# - Write five if statements. Each should check whether a certain kind of fruit is in your list.
# if the fruit is in your list, the if block should print a statement, such as 'You really like bananas!'

# I thought the way this question wanted us to do the problem was ineffective and had a slower run time so I did a for loop.
favorite_fruits = ['Strawberries', 'Blueberries', 'Peaches', 'Apples', 'Raspberries']

for fruit in favorite_fruits:
    if fruit in favorite_fruits:
        print('You really like ' + fruit + '!')
        
        
# 5.8 Hello Admin: Make a list of five or more usernames, including tha name 'admin'. Imagine that you are writing code
# that will print a greeting to each user after they log into a website. Loop through the list, and print a greeting to 
# each user.
# - If the username is 'admin', print a special greeting, such as 'Hello admin, would you like to see a status report?'
# - Otherwise, print a generic greeting, such as 'Hello Eric, thank you for logging in again.'

usernames = ['admin', 'jake', 'brice', 'dylan', 'eli']

for name in usernames:
    if name == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print('Hello ' + name + ', thank you for logging in again.')
        
# 5.9 No Users: Add an if test to the previous exercise to make sure that the list is not empty.
# - If the list is empty, print the message 'We need to find some users!'
# - Remove all of the usernames from your list, and make sure the correct message is printed.

usernames = ['admin', 'jake', 'brice', 'dylan', 'eli']

if usernames == []:
    print('We need to find some users!')
elif len(usernames) > 0:
    for name in usernames:
        if name == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello ' + name + ', thank you for logging in again!')
            
# 5.10 Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone
# has a unique username.
# - Make a list of five or more usernames called current_users.
# - Make another list of five usernames called new_users. Make sure one or two of the usernames are also in
# the current_users list.
# Loop through the new_users list to see is each new username has already been used. If it has, print a message
# that the person will need to enter a new username. If a username has not been used, print a message
# saying that the username is available.
# Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted.

current_users = ['admin', 'dylan', 'Brice', 'JOHN', 'JaKe!']
new_users = ['DYlan', 'BricE', 'Ben', 'eli', 'marK']

current_users2 = []
new_users2 = []

for name in current_users:
    current_users2.append(name.lower())
for names in new_users:
    new_users2.append(names.lower())

for item in current_users2:
    if item in new_users2:
        print('That username is already taken. Please choose a different one.')
    else:
        print('That username is valid.')
        
# 5.11 Ordinal Numbers: Odinal numbers indicate their position in a list, such as 1st or 2nd.
# Most ordinal numbers end in th, except 1, 2, and 3.
# - Store the numbers 1 - 9 in a list
# - Loop through the list
# - Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number.
# Your output should read '1st 2nd 3rd 4th 5th 6th 7th 8th 9th', and each result should be on a seperate line.

ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in ordinal_numbers:
    if num == 1:
        print(str(num) + 'st')
    elif num == 2:
        print(str(num) + 'nd')
    elif num == 3:
        print(str(num) + 'rd')
    else:
        print(str(num) + 'th')
