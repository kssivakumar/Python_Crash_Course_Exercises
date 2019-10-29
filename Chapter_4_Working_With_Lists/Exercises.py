# 4.1 Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop
# to print the name of each pizza.

pizzas = ['Pineapple', 'Hawaiian', 'Pepperoni']

for pizza in pizzas:
    print(pizza)
    
# - Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. For 
# each pizza you should have one line of output containing a simple statement like 'I like pepperoni pizza.'

pizzas = ['Pineapple', 'Hawaiian', 'Pepperoni']

for pizza in pizzas:
    message = ('I like ' + pizza + ' pizza.')
    print(message)
    
# - Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist 
# of three or more lines about the kinds of pizza you like and then an additional sentence, such as 'I really love pizza.'

pizzas = ['Pineapple', 'Hawaiian', 'Pepperoni']

for pizza in pizzas:
    message = ('I like ' + pizza + ' pizza.')
    print(message)
print('I really love pizza!') 


# 4.2 Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals
# in a list, and then use a for loop to print out the name of each animal.

animals = ['Shark', 'Dolphins', 'Fish']

for animal in animals:
    print(animal)
    
# - Modify your program to print a statement about each animal, such as 'A dog would make a great pet.'

animals = ['Shark', 'Dolphins', 'Fish']

for animal in animals:

    message1 = ('A ' + animal + ' would not make a great pet.')
    message2 = (animal + ' are known to be extremely intelligent.')
    message3 = ('A ' + animal + ' would make a great pet!')

    if animal == 'Shark':
        print(message1)
    elif animal == 'Dolphins':
        print(message2)
    else:
        print(message3)
        
# - Add a line at the end of your program stating what these animals have in common. You could print a sentence such 
# as 'Any of these animals would make a great pet!'

animals = ['Shark', 'Dolphins', 'Fish']

for animal in animals:

    message1 = ('A ' + animal + ' would not make a great pet.')
    message2 = (animal + ' are known to be extremely intelligent.')
    message3 = ('A ' + animal + ' would make a great pet!')

    if animal == 'Shark':
        print(message1)
    elif animal == 'Dolphins':
        print(message2)
    else:
        print(message3)
print('All of these animals live in water!')


# 4.3 Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

for num in range(1, 21):
    print(num)
    
# 4.4 One Million: Make a list of the numbers from one to one million, and then use a for loop
# to print the numbers.

nums = list(range(1, 1000001))

for num in nums:
    print(num)
    
# 4.5 Summing a Million: Make a list of the numbers from one to one million, and then use min() and max()
# to make sure your list actually starts at one and ends at one million. Also, use the sum() function to
# see how quickly Python can add a million numbers.

nums = list(range(1, 1000001))

print(min(nums))
print(max(nums))
print(sum(nums))

# 4.6 Odd numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20.
# Use a for loop to print each number.

nums = list(range(1, 20, 2))

for num in nums:
    print(num)
    
# 4.7 Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

nums = list(range(3, 31))
threes = []
for num in nums:
    if num % 3 == 0:
        threes.append(num)
        print(num)
        
        
# 4.8 Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python.
# Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.

nums = list(range(1, 11))

cubes = []

for num in nums:
    num **= 3
    cubes.append(num)

for num in cubes:
    print(num)
    
# 4.9 Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes

cubes = [num ** 3 for num in range(1, 11)]

print(cubes)


# 4.10 Slices: Using one of the programs you wrote in this chapter, add several lines to the 
# end of the program that do the following:
#
# - Print the message, 'The first three items in the list are:...' Then use a slice to print
# the first three items from that programs list.

cubes = [num ** 3 for num in range(1, 11)]

print('The first three items in the list are:...')

for item in cubes[:3]:
    print(item)
    
# - Print the message, 'Three items from the middle of the list are:...' Use a slice to print
# The items from the middle of the list.

cubes = [num ** 3 for num in range(1, 11)]

print('Three items from the middle of the list are:...')

for item in cubes[4:7]:
    print(item)
    
# - Print the message, 'The last three items in the list are:...' Use a slice to print the last
# three items in the list.

cubes = [num ** 3 for num in range(1, 11)]

print('The last three items in the list are:...')

for item in cubes[-3:]:
    print(item)
    
# 4.11 My Pizzas, Your Pizzas: Start with your program from exercise 4.1. Make a copy of the list
# of pizzas, and call it friend_pizzas. Then, do the following:

friend_pizzas = pizzas.copy()

# - Add a new pizza to the origional list.

pizzas.append('Cheese')

# - Add a different pizza to the list friend_pizza

friend_pizza.append('Italian')

# - Prove that you have two seperate lists. Print the message, 'My favorite pizzas are:...' and
# use a for loop to print the first list. Print the message, 'My friend's favorite pizzas are:...'
# and then use a for loop to print the second list. Make sure each new pizza is stored in the
# appropriate list.

print('My favorite pizzas are:...')

for pizza in pizzas:
    print(pizza)
    
print("My friend's favorite pizzas are:...")

for pizza in friends_pizza:
  print(pizza)
  
# I am skipping 4.12 because I have been writing for loops in my programs

# 4.13 Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple
# foods, and store them in a tuple.

foods = ('Steak', 'Macaroni', 'Rice', 'Chicken', 'Salad')

# - Use a for loop to print each food the restaurant offers.

for food in foods:
    print(food)
    
# - Try to modify one of the items, and make sure that Python rejects the change
# This is pretty simple to do in your IDE, Pyhton should automatically reject what you are trying to do

# - The restaurant changes its menu, replacing two of the items with different foods. Add a block 
# of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

# Tuples are immutable so we have to rewrite the tuple.

foods = ('chicken', 'salad', 'Rice', 'Buffalo', 'Turkey')




