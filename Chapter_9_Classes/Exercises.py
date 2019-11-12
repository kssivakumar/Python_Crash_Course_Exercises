# 9.1 Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes:
# A restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.




# 9.2 Three Restaurants: Start with your class from exercise 9.1. Create these different instances from the class, and
# call describe_restaurant() for each instance.





# 9.3 Users: Make a class called User. Create two attributes called first_name and last_name, and then create several
# other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a
# summary of the user's information. Make another method called great_user() that prints a personalized greeting to the
# user. Create several instances representing different users, and call both methods for each user.




# 9.4 Number Served: Start with your program from exercise 9.1. Add an atribute called number_served with a default
# value of 0. Create an instance called restaurant from this class. print the number of customers the restaurant has
# served, and then change this value and then print it again. Add a method called set_number_served() that lets you
# increment the number of customers who've been served. Call this method with any number you like that could represent
# how many customers were served in, say, a day of business.





# 9.5 Login Attempts: Add an attribute called login_attempts to your User class from exercise 9.3. Write a method
# called increment_login_attempts() that increments the value of login_attempts by 1. Write another method called
# reset_login_attempts() that resets the value of login_attempts to 0. Make an instance of the User class and call
# increment_login_attempts() several times. Print the value of login attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.





# 9.6 Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IcreCreamStand that
# inherits from the Restaurant class you wrote in exercise 9.1 or exercise 9.4. Either version of the class will work;
# Just pick the one you like better. Add an attribute called flavors that store a list of ice cream flavors. Write
# a method that displays these flavors. Create an instance of IceCreamStand, and call this method.




# 9.7 Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class
# you wrote in exercise 9.3 or exercise 9.5. Add an attribute, privileges, that stores a list of strings like
# 'can add post', 'can delete post', 'can ban user', and so on. Write a method called show_privileges() that lists
# the administrator's set of privileges. Create an instance of admin, and call your method.





# 9.8 Privileges: Write a seperate Privileges class. The class should have one attribute, privileges, that stores a
# list of strings as described in exercise 9.7. Move the show_privileges() method to this class. Make a privileges
# instance as an attribute in the Admin class. Create a new instance of admin and use your method to show its
# privileges.





# 9.9 Battery Upgrade: Use the final version of electric_car.py from this section. Add a method to the battery class
# called upgrade_battery(). This method should check the battery size and set the capacity to 85if it isn't already.
# Make an electric car with a default battery size, call get_range() once, and then call get_range() a second time
# after upgrading the battery. You should see an increase in the car's range.





# 9.10 Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a seperate file that imports
# Restaurant. Make a Restaurant instance, and call one of Restaurant's methods to show that the import statement is
# working properly.





# 9.11 Imported Admin: Start with your work from exercise 9.8. Store the class User, Privileges, and Admin in one
# module. Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working.






# 9.12 Multiplying Modules: Store the User class in one module, and store the Privileges and Admin classes in a
# separate file, create an Admin instance and call show_privileges() to show that everything is working correctly.




# 9.13 OrderedDict Rewrite: Start with exercise 6.4 Where you used a standard dictionary to represent a glossary.
# Rewrite the program using the OrderedDict class and make sure the order of the output matches the order in which
# key-value pairs were added to the dictionary.






# 9.14 Dice: The module random contains functions that generate random numbers in a variety of ways. The function
# randint() returns an integer in the range you provide. The following code returns a number between 1 and 6:
from random import randint
x = randint(1,6)
# Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die()
# that prints a random number between 1 and the number of sides a die has. Make a 6 sided die and roll it 10 times.
# Make a 10 sided die and a 20 sided die. Roll each die 10 times.
