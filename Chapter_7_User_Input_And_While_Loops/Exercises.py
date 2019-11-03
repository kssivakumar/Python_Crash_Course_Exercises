# 7.1 Rental Car: Write a program that asks the user what kind of rental car they would like. Print a message about that car,
# such as 'Let me see if I can find you a Subaru.'

user_input = input('Please enter the rental car which you would like: ')

print('Let me see if I can find you a ' + user_input + '.')

# 7.2 Restaurant Seating: Write a program that asks the user how many people are in their dinner group. If the answer if more
# than eight, print a message saying they'll have to wait for a table. Otherwise report that their table is ready.

user_input = int(input('Please enter the number of people in your dinner group: '))

if user_input > 8:
    print('I am sorry, you will have to wait for a table.')
else:
    print('Your table is ready')
    
# 7.3 Multiples Of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.

user_input = int(input('Please enter a number: '))

if user_input % 10 == 0:
    print('The number you entered is a multiple of ten.')
else:
    print('The number you entered is not a multiple of ten.')
    
# 7.4 Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
# As they enter each topping, print a message saying you'll add that topping to their pizza.

user_input = input('Please enter a pizza topping. When you would like no more toppings please enter "quit": ')
toppings = user_input.split()

while True:
    for item in toppings:
        if item == 'quit':
            quit()
        else:
            print('I will add ' + item + ' to your pizza.')
    break
    
# 7.5 Movie Tickets: A movie theater charges different ticket prices depending on a person's age. If a person is under the
# age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15
# Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

user_input = int(input('Please enter your age: '))

while True:
    if user_input < 3:
        print('The movie ticket is free.')
    elif user_input >= 3 and user_input <= 12:
        print('The movie ticket is $10.')
    else:
        print('The movie ticket is $15.')

    break
    
# 7.6 Three Exits: Write different versions of either Exercises 7.4 or Exercises 7.5 that do each of the following:
# - Use a conditional test in the while statement to stop the loop.
# - Use an active variable to control how long the loop runs.
# - Use a break statement to exit the loop when the user enters a 'quit' value.

# Using conditional test
user_input = int(input('Please enter your age: '))

while user_input != 0:
    if user_input < 3:
        print('The movie ticket is free.')
    elif user_input >= 3 and user_input <= 12:
        print('The movie ticket is $10.')
    else:
        print('The movie ticket is $15.')

    break
    
# Using accumulation    
count = 0
while count <= 3:
    user_input = int(input('Please enter your age: '))

    if user_input < 3:
        print('The movie ticket is free.')
    elif user_input >= 3 and user_input <= 12:
        print('The movie ticket is $10.')
    else:
        print('The movie ticket is $15.')

    count += 1
    
# Using break statement    
    user_input = int(input('Please enter your age: '))

while True:
    if user_input < 3:
        print('The movie ticket is free.')
    elif user_input >= 3 and user_input <= 12:
        print('The movie ticket is $10.')
    else:
        print('The movie ticket is $15.')

    break
# 7.7 Infinity: Write a loop that never ends, and run it.

while True:
    print('Hello World!')
    
# 7.8 Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called
# finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as 'I made your tuna
# sandwich.'. As each sandwich is made move it to the list of finished sandwiches. After all the sandwiches have been made,
# print a message listing each sandwich that was made.

sandwich_orders = ['pb&j', 'ham', 'tuna']

finished_sandwiches = []

while True:
    for item in sandwich_orders:
        print('I made your ' + item + ' sandwich.')
        finished_sandwiches.append(item)
    break

for item in finished_sandwiches:
    print(item + ' sandwich was made.')
    
# 7.9 No Pastrami: Using the list sandwich_orders from exercise 7.8, make sure the sandwich 'pastrami' appears in the list at
# least three times. Add code near the beginning of your program to print a message saying that the deli has run out of
# pastrami, and then use a while loop to remove all occurances of 'pastrami' from sandwich_orders. Make sure no pastrami
# sandwiches end up in finished_sandwiches.

sandwich_orders = ['pb&j', 'ham', 'tuna', 'pastrami', 'pastrami', 'pastrami']

finished_sandwiches = []

while True:
    for item in sandwich_orders:
        if item == 'pastrami':
            print('I am sorry, the deli has run out of pastrami')
            sandwich_orders.remove('pastrami')
        else:
            print('I made your ' + item + ' sandwich.')
            finished_sandwiches.append(item)
    break

for item in finished_sandwiches:
    print(item + ' sandwich was made.')
    
# 7.10 Dream Vacation: Write a program that polls users about their dream vactaion. Write a prompt similar to 'If you could
# visit one place in the world, where would you go?' Include a block of code that prints the results of the poll.
