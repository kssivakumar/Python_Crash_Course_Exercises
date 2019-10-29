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










































































