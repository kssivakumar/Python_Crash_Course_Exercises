# 3.1 Names: Store the names of a few of your friends in a list called names. Print each person's name by accessing each
# element in the list, one at a time. (Print each friend's name on a new line.)

friends = ['Brice', 'Jake', 'Ben', 'Eli', 'Mark']

for element in friends:
  print(element)


# 3.2 Greetings: Start with the list you used in exercise 3.1, but instead of just printing each person's name, print a message
# to them. The text of each message should be the same, but each message should be personalized with the person's name.

friends = ['Brice', 'Jake', 'Ben', 'Eli', 'Mark']


for element in friends:
    message = ('Hello ' + element + ', ' 'I hope you are doing well since graduation!')
    print(message)

# 3.3 Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores
# several examples. Use your list to print a series of statements about these items,
# such as "I would like to own a Honda motorcycle."

mode_of_transportation = ['Honda', 'Yamaha', 'Ducati']

for element in mode_of_transportation:
    message1 = ('I would like to own a ' + element + ' someday!')
    message2 = ('I am not a fan of the motorcylce brand ' + element + '.')

    if element != 'Ducati':
        print(message2)
    else:
        print(message1)
        
        
# 3.4 Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite?
# Make a list that includes at least three people you'd like to invite to dinner. Then use your list
# to print a message to each person, inviting them to dinner.

guest_list = ['Brice', 'Jake', 'Ben']

for name in guest_list:
    message = (name + ',' + ' I would like to invite you to a dinner, which is taking place at 1 Pacific Drive, California.')
    print(message)
    
    
# 3.5 Changing Guest List: You just heard that one of your guests can't make the dinner, so you need 
# to send out a set of new invitations. You'll have to think of someone else to invite.
#
# - Start with your program from exercise 3.4. Add a print statement at the end of your program
# stating the name of the guest who can't make it.
#
# - Modify your list, replacing the name of the guest who can't make it with the name of the new
# person you are inviting.
#
# - Print a second set of invitation messages, one for each person who is still in your list.

guest_list = ['Brice', 'Jake', 'Ben']

for name in guest_list:
    message = (name + ',' + ' I would like to invite you to a dinner, which is taking place at 1 Pacific Drive, California.')
    print(message)
print('\nBen is unable to make the dinner! You will have to choose someone else.\n')

guest_list[-1] = 'Eli'

for name in guest_list:
    message = (name + ',' + ' I would like to invite you to a dinner, which is taking place at 1 Pacific Drive, California.')
    print(message)


# 3.6 More Guests: You just found a bigger dinner table, so now more space is available. Think of three
# more guests to invite to dinner.
#
# - Start with your program from exercise 3.4 or exercise 3.5. Add a print statement to the end of your program
# informing people that you found a bigger dinner table.
#
# - Use insert() to add one new guest to the beginning of your list.
#
# - Use insert() to add one new guest to the middle of your list.
#
# - Use append() to add one new guest to the end of your list.
#
# - Print a new set of invitation messages, one for each person in your list.


guest_list = ['Brice', 'Jake', 'Ben']

for name in guest_list:
    message = (name + ',' + ' I would like to invite you to a dinner, which is taking place at 1 Pacific Drive, California.')
    print(message)
    message2 = (name + ', I have found a bigger dinner table and will be inviting three more people.\n')
    print(message2)
    
guest_list.insert(0, 'Mark')
guest_list.insert(2, 'Eli')
guest_list.append('Austyn')

for name in guest_list:
    message = (name + ',' + ' I would like to invite you to a dinner, which is taking place at 1 Pacific Drive, California.\n')
    print(message)
    
# 3.7 Shrinking Guest List: You just found out that your new dinner table won't arrive in time for the dinner,
# and you have space for only two guests.
#
# - Start with your program from exercise 3.6. Add a new line that prints a message saying that you can
# only invite two people for dinner.
#
# - Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time
# you pop a name from your list, print a message to that person letting them know you're sorry you can't invite
# them to dinner.
#
# - Print a message to each of the two people still in your list, letting them know they're still invited.
#
# - Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure
# you actually have an empty list at the end of your program.


guest_list = ['Brice', 'Jake', 'Ben']

for name in guest_list:
    message = (name + ',' + ' I would like to invite you to a dinner, which is taking place at 1 Pacific Drive, California.')
    print(message)
    message2 = (name + ', I have found a bigger dinner table and will be inviting three more people.\n')
    print(message2)

guest_list.insert(0, 'Mark')
guest_list.insert(2, 'Eli')
guest_list.append('Austyn')


for name in guest_list:
    message = (name + ',' + ' I would like to invite you to a dinner, which is taking place at 1 Pacific Drive, California.\n')
    print(message)


print('I can only invite two people to dinner!\n')


while len(guest_list) > 2:
    removed = guest_list.pop()
    print(removed + ', I am sorry but I can only invite two people to dinner!\n')


for name in guest_list:
    print(name + ', You are still invited to dinner!')


del guest_list[:]

print(guest_list)



# 3.8 Seeing The World: Think of at least five places in the world that youd like to visit.
#
# - Store the locations in a list. Make sure the list is not in alphabetical order.

places_to_visit = ['Fiji', 'Italy', 'China', 'Sweden', 'Australia']

# - Use sorted() to print your list in alphabetical order without modifying that actual list

print(sorted(places_to_visit))

# - Show that your list is still in its origional order by printing it

print(places_to_visit)

# - Use sorted() to print your list in reverse alphabetical order without changing the order of the
# origional list.

print(sorted(places_to_visit)[::-1])

# - Show that your list is still in its origional order by printing it again

print(places_to_visit)

# - Use reverse to change the order of your list. Print the list to show that its order has changed.

places_to_visit.reverse()
print(places_to_visit)

# - Use reverse() to change the order of your list again. Print the list to show it's back to it's origional order

places_to_visit.reverse()
print(places_to_visit)

# - Use sort() to change your list so it's stored in alphabetical order. Print the list to show that its order has been 
# changed.

places_to_visit.sort()
print(places_to_visit)

# - Use sort() to change your list so it's stored in reverse alphabetical order. Print the list to show that its order has 
# changed.

places_to_visit.sort(reverse=True)
print(places_to_visit)


# 3.9 Dinner Guests: Working with one of the programs from 3.4 through 3.7, use len() to print a message indicating the number
# of people you are inviting to dinner.

guest_list = ['Brice', 'Jake', 'Ben']

print('You are inviting ' + str(len(guest_list)) + ' people to dinner')


# 3.10 Every Function: Think of something you could store in a list. For example, you could make a list of mountains, rivers, 
# countries, cities, languages, or anything else you'd like. Write a program that creates a list containing these items
# and then use uses each function introduced in this chapter at least once.
#
# We have to use the functions: append(), insert(), del, pop(), remove(), sort(), sorted(), len(), reverse()

# append()

friends = 'Mark, Brice, Jake, Ben, Eli'

friends_list = friends.split(', ')

friends_list.append('Austyn')

# insert()

friends = 'Mark, Brice, Jake, Ben, Eli'

friends_list = friends.split(', ')

friends_list.insert(2, 'Austyn')

# del

friends = 'Mark, Brice, Jake, Ben, Eli'

friends_list = friends.split(', ')

del friends_list[2]

# pop()

friends = 'Mark, Brice, Jake, Ben, Eli'

friends_list = friends.split(', ')

friends_list.pop(0)

# remove()

friends = 'Mark, Brice, Jake, Ben, Eli'

friends_list = friends.split(', ')

friends_list.remove('Brice')

# sort()

friends = 'Mark, Brice, Jake, Ben, Eli'

friends_list = friends.split(', ')

friends_list.sort()

# sorted()

friends = 'Mark, Brice, Jake, Ben, Eli'

friends_list = friends.split(', ')

x = sorted(friends_list)

# len()

friends = 'Mark, Brice, Jake, Ben, Eli'

friends_list = friends.split(', ')

x = len(friends_list)

# reverse()

friends = 'Mark, Brice, Jake, Ben, Eli'

friends_list = friends.split(', ')

friends_list.reverse()

# Now put all of them into a single program. I used an accumulation pattern to save on a lot of coding.

friends = 'Mark, Brice, Jake, Ben, Eli'

friends_list = friends.split(', ')

count = 0

while count < 1:

    friends_list.append('Austyn')
    print(friends_list)

    friends_list.insert(2, 'Austyn')
    print(friends_list)

    del friends_list[2]
    print(friends_list)

    friends_list.pop(0)
    print(friends_list)

    friends_list.remove('Brice')
    print(friends_list)

    friends_list.sort()
    print(friends_list)

    print(sorted(friends_list))

    print(len(friends_list))

    friends_list.reverse()

    count += 1

print(friends_list)
