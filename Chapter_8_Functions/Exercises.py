# 8.1 Message: Write a function called display_message() that prints one sentence telling everyone what you are learning 
# about in this chapter. Call the function, and make sure the message displays correctly.

def display_message():
  return 'I am learning about functions in this chapter!'

print(display_message())

# 8.2 Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print
# a message, such as 'One of my favorite books is Alice in Wonderland.'. Call the function, making sure to
# include a book title  as an argument in the function call.

def favorite_book(book_title):
  return ("One of my favorite books is " + book_title + ".")
print(favorite_book('Alice in Wonderland'))

# 8.3 T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed
# on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

# With positional arguments
def make_shirt(size, text):

  return 'The size of the shirt is ' + size + ', and the message printed on the shirt reads, ' + text

print(make_shirt('Medium', 'I love Python!'))

# With Keyword arguments
def make_shirt(size, text):

  return 'The size of the shirt is ' + size + ', and the message printed on the shirt reads, ' + text

print(make_shirt(size='Large', text='I love Python!'))

# 8.4 Large Shirts: Modify the make_shirt() function so the shirts are large by default with a message that reads 
#'I love Python'
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

# Default Large shirt
def make_shirt(size='Large', text='I love Python'):

  return 'The size of the shirt is ' + size + ', and the message printed on the shirt reads, ' + text

print(make_shirt(size='Large', text='I love Python!'))

# Default Medium Shirt
def make_shirt(size='Large', text='I love Python'):

  return 'The size of the shirt is ' + size + ', and the message printed on the shirt reads, ' + text

print(make_shirt(size='Medium', text='I love Python!'))

# Shirt of any size with a different message
def make_shirt(size='Large', text='I love Python'):

  return 'The size of the shirt is ' + size + ', and the message printed on the shirt reads, ' + text

print(make_shirt(size='Small', text='I love coding in Python!'))

# 8.5 Cities: Write a function called describe_city(): that accepts the name of a city and its country. The function
# Should print a simple sentence, such as 'Reykjavik is in Iceland'. Give the parameter for the coutry a default value.
# Call your function for three different cities, at least one of which is not in the default country.

# Call 1
def describe_city(city, country='Iceland'):

  return city + ' is located in ' + country

print(describe_city('Reykjavik'))

# Call 2
def describe_city(city, country='Iceland'):

  return city + ' is located in ' + country

print(describe_city('San Francisco', country='USA'))

# Call 3
def describe_city(city, country='Iceland'):

  return city + ' is located in ' + country

print(describe_city('Stockholm', country='Sweden'))

# 8.6 City Names: Write a function called city_country() that takes in the name of a city and its country. The function
# Should return a string formatted like this: 'Santiago, Chile'
# Call your function with at least three city-country pairs, and print the value that's returned.

# Call 1
def city_country(city, country):
  return city + ', ' + country

print(city_country('Santiago', 'Chile'))

# Call 2
def city_country(city, country):
  return city + ', ' + country

print(city_country('Stockholm', 'Sweden'))

# Call 3
def city_country(city, country):
  return city + ', ' + country

print(city_country('Sydney', 'Australia'))


# 8.7 Album: Write a function called make_album() that builds a dictionary describing a music album. The function should
# take in an artist name and an album title, and it should return a dictionary containing these two pieces of information.
# Use the function to make three dictionaries representing different albums. Print each return value to show that the
# dictionaries are storing the album information correctly. Add an optional parameter to make_album() that allows you to
# store the number of tracks on an album. If the calling line includes a value for the number of tracks, add that value to
# the album's dictionary. Make at least one new function call that includes the number of tracks on an album.

# Call 1
def make_album(artist_name, album_title, number_of_tracks=''):
  if number_of_tracks == '':
    return {'Artist Name' : artist_name, 'Album Title' : album_title}
  else:
    return {'Artist Name' : artist_name, 'Album Title' : album_title, 'Number of Tracks': number_of_tracks}

print(make_album('NEFFEX', 'Careless'))

# Call 2
def make_album(artist_name, album_title, number_of_tracks=''):
  if number_of_tracks == '':
    return {'Artist Name' : artist_name, 'Album Title' : album_title}
  else:
    return {'Artist Name' : artist_name, 'Album Title' : album_title, 'Number of Tracks': number_of_tracks}

print(make_album('The Chainsmokers', 'World War Joy...Takeaway', '5'))


# Call 3
def make_album(artist_name, album_title, number_of_tracks=''):
  if number_of_tracks == '':
    return {'Artist Name' : artist_name, 'Album Title' : album_title}
  else:
    return {'Artist Name' : artist_name, 'Album Title' : album_title, 'Number of Tracks': number_of_tracks}

print(make_album('The Chainsmokers', 'Roses', '1'))

# 8.8 User Albums: Start with your program from exercise 8.7. Write a while loop that allows users to enter an album's artist
# and title. Once you have that information, call make_album() with the user's input and print the dicitonary that's created.
# Be sure to include a quit value in the while loop.

def make_album():

  user_input = input('Please Enter an Artist name and the Album title separated by a comma: ')
  artist_album_list = user_input.split(', ')

  while True:
    for item in artist_album_list:
      return {'Artist Name': artist_album_list[0], 'Album Title': artist_album_list[1]}
    quit()

print(make_album())


# 8.9 Magicians: Make a list of magician's names. Pass the list to a function called show_magicians(), which prints the name
# of each magician in the list.

def show_magicians(lst):
  for item in lst:
    print(item)

magician_names = ['Dark Magician','Dark Magician Girl','Silent Magician']

print(show_magicians(magician_names))

# 8.10 Great Magicians: Start with a copy of your program from exercise 8.9. Write a function called make_great() 
# that modifies the list of magicians by adding the phrase 'The Great' to each magician's name. Call show_magicians() 
# to see that the list has actually been modified.

def show_magicians(lst):
  for item in lst:
    print(item)

magician_names = ['Dark Magician','Dark Magician Girl','Silent Magician']

def make_great(names):
  names[:] = ['The Great ' + name for name in names]

print(make_great(names=magician_names))
print(show_magicians(magician_names))

# 8.11 Unchanged Magicians: Start with your work from exercise 8.10. Call the function make_great() with a copy of the 
# list of magician's names becuase the origional list will be unchanged, return the new list and store it in a seperate list. 
# Call show_magicians() with each list to show that you have one list of the orgional names and one list with 'The Great' 
# added to each magician's name.




# 8.12 Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have 
# one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich 
# that is being ordered. Call the function three times, using a different number of arguments each time.



# 8.13 User Profile: Start with a copy of user_profile.py from page 153. Build a profile of yourself by calling 
# build_profile(), using your first and last names and three other key value pairs that describe you.






# 8.14 Cars: Write a function that stores information about a car in a dictioanry. The function should always receive a 
# manufacturer and a model name it should then accept an arbitrary number of keyword arguments. Call the function with 
# the required information and two other name value pairs, such as a color or an optional feature. Your function should 
# work for a call like this one: 
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that's returned to make sure all the information was stored correctly.




# 8.15 Printing Models: Put the funcitons for the example printing_models.py in a seperate file called printing_functions.py. 
# Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.



# 8.16 Imports: Using a program you wrote that has one funciton in it, store that function in a seperate file. 
# Import the function into your main program file, and call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *




# 8.17 Styling Functions: Choose any three programs your wrote for this chapter, and make sure they follow the 
# styling guidelines described in this section.





































