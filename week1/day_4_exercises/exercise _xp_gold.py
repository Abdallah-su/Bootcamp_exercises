#Exercise 1: Concatenate lists
#Instructions
#Write code that concatenates two lists together without using the + sign.


#Exercise 2: Range of numbers
#Instructions
#Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.

for number in range(1500, 2501):
    if number % 5 == 0 and number % 7 == 0:
        print(number)


#Exercise 3: Check the index
#Instructions
#using this variable

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
#Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.
user_name =input("what's your name: ")
for i in names:
    if user_name == i:
        print(names.index(user_name))


#Exercise 4: Greatest Number
#Instructions
#Ask the user for 3 numbers and print the greatest number.

input_1 =int(input("give a number: "))
input_2 = int(input("give another one: "))
input_3 = int(input("give the last one: "))
gratest = max(input_1, input_2, input_3)
print(f'the greatest number is {gratest}')

#Exercise 5: The Alphabet
#Instructions
#Create a string of all the letters in the alphabet
#Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
vowel= 'AEIOU'
for letter in alphabet:
    if letter in vowel:
        print(f"{letter} is a vowel")
    else: print(f"{letter} is a consonant")
   

##xercise 6: Words and letters
#Instructions
#Ask a user for 7 words, store them in a list named words.
#Ask the user for a single character, store it in a variable called letter.
#Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
#If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.
words = [ ]
user_list = input("list 7 words: ")
list = user_list.split()
for word in list:
    words.append(word)
letter = input("mention a character: ")  
for word in words:
    if letter in word:
        print(word.index(letter)) 
    else:print(f"sorry! the letter is not found in {word}")

 
#Exercise 7: Min, Max, Sum
#Instructions
#Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million. Use the sum() function to see how quickly Python can add a million numbers.

list_of_numbers = range(1, 1000001)
print(min(list_of_numbers))
print(max(list_of_numbers))
print(sum(list_of_numbers))

#xercise 8 : List and Tuple
#Instructions
#Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.
#Suppose the following input is supplied to the program: 34,67,55,33,12,V
my_list= [ ]
nums = "34,67,55,33,12,98"
list_input = nums.split(",")
for num in list_input:
    my_list.append(num)
print(my_list)    
my_tuple = tuple(my_list)
print(my_tuple)                    


#Exercise 9 : Random number
#Instructions
#Ask the user to input a number from 1 to 9 (including).
#Get a random number between 1 and 9. Hint: random module.
#If the user guesses the correct number print a message that says Winner.
#If the user guesses the wrong number print a message that says better luck next time.
#Bonus: use a loop that allows the user to keep guessing until they want to quit.
#Bonus 2: on exiting the loop tally up and display total games won and lost.

import random

#user_guess = int(input("type in a number(1-9):  "))
#random_number = random.randint(1,9)
#if user_guess == random_number:
 #   print("you've won")
    
#else: print(f"sorry! better luck next time and rhe number is {random_number}")

win = 0
loss = 0
while True:
    user_guess = int(input("type in a number(1-9) or type 0 to exit:  "))
    random_number = random.randint(1,9)
    if user_guess == random_number: 
        win += 1
        print("you've won")
        continue
    elif user_guess == 0:
        break
    else:
        loss += 1
        print(f"sorry! better luck next time and rhe number is {random_number}")
        continue
print(f"you have total of {win} wins and {loss} loss" )