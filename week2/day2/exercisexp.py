#Exercise 1: What Are You Learning?
#Goal: Create a function that displays a message about what you’re learning.
#Key Python Topics:
#Functions (defining and calling)
#print() function

def display_message(topic):
    return f"I am learning {topic}"
message ="Functions in python"
print(display_message(message))



# Exercise 2: What’s Your Favorite Book?
#Goal: Create a function that displays a message about a favorite book.
#Key Python Topics:
#Functions with parameters
#String concatenation or f-strings
#Calling functions with arguments

def fav_book(title):
    return f"my favorite book is {title}"
message_display = "bootcamps"
print(fav_book(message_display))

#Exercise 3: Some Geography
#Goal: Create a function that describes a city and its country.
#Key Python Topics:
#Functions with multiple parameters
#Default parameter values
#String formatting

def city_country(k, v):
    return f"{k} is in {v}" 
city = "Accra"
country = "Ghana"
print(city_country(city, country))

#Exercise 4: Random
#Goal: Create a function that generates random numbers and compares them.
#Key Python Topics:
#random module
#random.randint() function
#Conditional statements (if, else)

import random
def guess_num (n):
        jackpot= random.randint(1, 100)
        if n == jackpot:
            return "You've' guessed right"
        else: return f"sorry wrong! your input was {n} and the number is {jackpot}"
number= 78
print(guess_num(number))

#Exercise 5: Let’s Create Some Personalized Shirts!
#Goal: Create a function to describe a shirt’s size and message, with default values.
#Key Python Topics:
#Functions with parameters and default values
#Keyword arguments

def p_shirts(s):
     return f"my shirt size is {s} and I love it"
ss= "medium"
print(p_shirts(ss))

#goal: Modify a list of magician names and display them in different ways.
#Key Python Topics:
#Lists
#for loops
#Modifying lists
#Functions that modify data structures

magicians =['hassan', 'elisha', 'frank', 'noah']

#modifiers
magicians.remove("hassan")
print(magicians)
magicians.append('hassan')
print(magicians)
magicians.count('hassan')
print(magicians)

#loop
for magician in magicians:
     print(f'hello {magician}')
     print(f'your are {magician} ofcourse')

#functions
print(sorted(magicians))

#Exercise 7: Temperature Advice
#Goal: Generate a random temperature and provide advice based on the temperature range.
#Key Python Topics:
#Functions
#Conditionals (if / elif)
#Random numbers
#Floating-point numbers (Bonus)
#Handling seasons (Bonus)

import random
def temp_cond (t) :
     t =random.randint(10, 40)
     if t <=18 : return f'at {t} you got to wear something heavy.'
     else: return f'at {t} you can wear your summer stuffs'

temp_ =random.randint(10, 40)   
print(temp_cond(temp_)) 
 
     

