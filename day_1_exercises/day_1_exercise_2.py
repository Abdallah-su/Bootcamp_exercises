#exercise 1
#You have a friend named Alice, and you want to send her a message with the following details:
Name ="Alice"
Age= 30
City= "New York"
#asks:
#Use f-strings to print a message saying:
#"Hello, Alice! You are 30 years old and live in New York."
#Use str.format() to print the same message.
print(f"Hello, {Name}! you are {Age} years old and live in {City}")
print(str(f"Hello, {Name}! you are {Age} years old and live in {City}"))


#exercise 2
#Ask the user for their age using the input() function and store it in a variable age.
#Convert the inputted age into an integer and calculate the number of years until they turn 100.
#Display a message: "You will turn 100 in X years", where X is the number of years calculated.
age = input("user's age : ")
u_age =int(age)
l_age = 100
n_years = l_age - u_age
print(n_years)

print("you will turn 100 years in 70 years")


#exercise 
#Analyze the code below and predict what the outcome will be. Check the results in your python shell.

age = input("How old are you? ")
age =int(age)
print(f"You are {age} years old")









      

