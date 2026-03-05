# Exercise 1 : Upcoming Holiday
# Instructions
# Write a function that displays today’s date.
# The function should also display the amount of time left from now
#  until the next upcoming holiday and print which holiday that is. 
# (Example: the next holiday is New Years’ Eve in 30 days).
# Hint: Use a module to find the datetime and name of the upcoming holiday.

from datetime import date, datetime
def holiday_date(h_year,h_month, h_day, name):
    holiday =date(h_year,h_month, h_day)
    today_date =date.today()
    print(f"Today's date is {today_date}")
    difference =holiday - today_date
    print(f'the next holiday is {name} in {difference.days} days')

holiday_date(2026,5,1, 'May Day')


# Exercise 2 : How Old Are You On Jupiter?
# Instructions
# Given an age in seconds, calculate how old someone would be on all those planets :

# Earth: orbital period 365.25 Earth days, or 31557600 seconds
# Example : if someone is 1,000,000,000 seconds old, 
# the function should output that they are 31.69 Earth-years old.
# Mercury: orbital period 0.2408467 Earth years
# Venus: orbital period 0.61519726 Earth years
# Mars: orbital period 1.8808158 Earth years
# Jupiter: orbital period 11.862615 Earth years
# Saturn: orbital period 29.447498 Earth years
# Uranus: orbital period 84.016846 Earth years
# Neptune: orbital period 164.79132 Earth years

def jupiter_years( year, month, day,):
    birthday= date(year,month, day)
    today =date.today()
    diff = today -birthday
    age_in_secs =diff.total_seconds()
    print(f' your age in seconds is {age_in_secs}s')
    #age_in_day =diff.days
    #year =age_in_day /365.25
    year = age_in_secs/31557600
    jupiter_age =year/11.862615
    print(f'your age in jupiter is {jupiter_age} earth years')

jupiter_years(1993,5,26)

# Exercise 3 : Regular Expression #1
# Instructions
# Hint: Use the RegEx (module)

# Use the regular expression module to extract numbers from a string

import re
return_numbers=re.findall(r'\d+',('k5k3q2g5z6x9bn'))
print(*return_numbers)


# Exercise 5: Python Password Generator
# Instructions
# Create a Python program that will generate a good password for you.

# Program flow:

# Ask the user to type in the number of characters that the password should have 
# (password length) – between 6 and 30 characters.
# Validate the input. Make sure the user is inputing a number between 6 to 30.
#  Create a loop which will continue to ask the user for an input until they enter a valid one.

# Generate a password with the required length.

# Print the password with a user-friendly message
# which reminds the user to keep the password in a safe place!

# Rules for the validity of the password

# Each password should contain:
# At least 1 digit (0-9)
# At least 1 lower-case character (a-z)
# At least 1 upper-case character (A-Z)
# At least 1 special character (eg. !, @, #, $, %, ^, _, …)
# Once there is at least 1 of each, the rest of the password should be composed of more characters from the options presented above.

# Create a test function first!

# Do the following steps 100 times, with different password lengths:
# Generate a password.
# Test the password to ensure that:
# it fulfills all the requirements above (eg. it has at least one digit, etc.)
# it has the specified length.
user_password = input('type in a new password, it be betwwen 6 and 30 characters: ')
while True:
    6<len(user_password)<30








