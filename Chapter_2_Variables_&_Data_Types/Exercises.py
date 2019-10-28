# 2.1 Simple Message: Store a message in a variable, and then print that message.

variable1 = 'Hello World!'

print(variable1)


# 2.2 Simple Messages: Store a message in a variable, and print that message. Then change the value of your variable to
# a new message, and print the new message.

variable2 = 'Hello python community!'

print(variable2)

variable2 = "Let's explore the world of coding together!"

print(variable2)


# 2.3 Personal Message: Store a person's name in a variable, and print a message to that person. Your message should be simple,
# such as, 'Hello Eric, would you like to learn some python today?'

name = 'Guido van Rossum'

print('Thank you for creating an amazing programming language ' + name + '!')


# 2.4 Name Cases: Store a person's name in a variable, and then print that person's name in lowercase, uppercase, and titlecase.

n = 'Guido van Rossum'

print(n.lower())

print(n.upper())

print(n.title())

# 2.5 Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should
# look something like the following, include the quotation marks:
# Albert Einstein once said, "A person who never made a mistake never tried anything new."

famous_name = 'Albert Einstein'

print(famous_name + ' once said, "A person who never made a mistake never tried anything new."')

# 2.6 Famous Quote 2: Repeat Exercise 2.5, but this time store the famous person's name in a variable called famous_person.
# Then compose your message and store it in a new variable called message. Print your message.

famous_person = 'Albert Einstein'

message = '"A person who never made a mistake never tried anything new."'

print(famous_person + ' once said, ' + message)

# 2.7 Stripping Names: Store a person's name, and include some whitespace characters at the beginning and end of the name.
# Make sure you use each character combination, "\t" and "\n", at least once. Print the name once, so the whitespace around
# the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().


name_of_person = '\tGuido van Rossum\n'

print(name_of_person)

print(name_of_person.lstrip())
print(name_of_person.rstrip())
print(name_of_person.strip())


# 2.8 Number Eight: Write addition, subtraction, multiplication, and division operations
# that each result in the number 8. Be sure to enclose your operations in print statements
# to see the results. You should create four lines taht look like this:
# print(5 + 3)
# your output should simply be four lines with the number 8 appearing once on each line.

addition = (4 + 4)
subtraction = (10 - 2)
multiplication = (4 * 2)
division = (16 // 2) # I used floor division here becuase it asked for the number 8 specifically, not 8.0

print(addition)
print(subtraction)
print(multiplication)
print(division)

# 2.9 Favorite Number: Store your favorite number in a variable. Then, using that variable, create a message that reveals your
# favorite number. Print that message.

favorite_number = 23

message = 'My favorite number is '

print(message + str(favorite_number)) # We have to convert our favorite number to a string becuase we cannot concatenate strings and integers.
