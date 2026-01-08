#exercise 1
# #1. ask the user to enter his/her name
#2. use the len() function to check the lenght of the name. 
# if it is less than 5 letter print('You have a short name :)')

user_name =input("type in your name:")
len(user_name)
if len(user_name)<5 : print("you have a short name")


#exercise 2
#Ask the user for a number between 1 and 100
#If the number is a divisible by three, print Fizz
#If the number is a divisible by five, print Buzz.
#If the number is a divisible by both three and five, print FizzBuzz instead.
user_number_s = input("type in a number between 1 and 100: ")
user_number = int(user_number_s)
if user_number % 3 == 0: print("fizz")
if user_number % 5 == 0 : print("Buzz") 
if user_number % 3 ==  0 and user_number % 5 == 0 : print("FizzBuzz")












