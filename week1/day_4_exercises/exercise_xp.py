#exercise1

#Create a set called my_fav_numbers and populate it with your favorite numbers.
#Add two new numbers to the set.
#Remove the last number you added to the set.
#Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
#Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
#Note: Sets are unordered collections, so ensure no duplicate numbers are added.

my_fav_numbers={3,4,5,6,7,8,9}
my_fav_numbers.add(2)
print(my_fav_numbers)
my_fav_numbers.add(1)
print(my_fav_numbers)
 
my_fav_numbers.remove(1)
print(my_fav_numbers)

friend_fav_numbers ={1,3,5,7,9,11}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)


#Instructions:
#Given a tuple of integers, try to add more integers to the tuple.
#Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.

#my_integers=(2,4,6,8,9)
#my_integers.append(10)


#Instructions:
#You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#Remove "Banana" from the list.
#Remove "Blueberries" from the list.
#Add "Kiwi" to the end of the list.
#Add "Apples" to the beginning of the list.
#Count how many times "Apples" appear in the list.
#Empty the list.
#Print the final state of the list.

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(basket)
basket.append("kiwi")
print(basket)
print(basket.count("Apples"))
basket.clear()
print(basket)


#Write a for loop to print all numbers from 1 to 20, inclusive.
#Write another for loop that prints every number from 1 to 20 where the index is even.

for number in range(1,21):
    print(number)
for even_number in range(0,22,2) :
    print(even_number)


#instructions:
#Use an input to ask the user to enter their name.
#Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
#hint: check for the method isdigit()
#if the input is incorrect, keep asking for the correct input until it is correct
#if the input is correct print “thank you” and break the loop

name = input("enter your name : ")
while True :
      if not name.isdigit() and len(name)>=3 :
        print("Thank you")
        break
      else: name = input("Enter the correct name")


#Instructions:
#Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
#Store these fruits in a list.
#Ask the user to input the name of any fruit.
#If the fruit is in their list of favorite fruits, print:
#"You chose one of your favorite fruits! Enjoy!"
#If not, print:
#"You chose a new fruit. I hope you enjoy it!"

user_fav_fruit1 =input ("List your favorite fruits : ")
user_fav_fruit=user_fav_fruit1.split()
fruit = input("enter any fruit :")
if fruit in user_fav_fruit :
    print("you've chosen your favorite fruit")
else:print("you've chosen a new fruit")
  
#Instructions:
#Write a loop that asks the user to enter pizza toppings one by one.
##Stop the loop when the user types 'quit'.
#For each topping entered, print:
#"Adding [topping] to your pizza."
#After exiting the loop, print all the toppings and the total cost of the pizza.
#The base price is $10, and each topping adds $2.50.

topping = []
base_price =10
each_topping =2.5
while True:
    user_topping =input ("enter pizza toppings one by one or quit to finish: ")
    if user_topping.lower == "quit":
        break
    topping.append(user_topping)
    print(f"Adding {user_topping} to your pizza")
    
total_cost = base_price + (len(user_topping )* each_topping)
print(topping)
print(total_cost)

#nstructions:
#Ask for the age of each person in a family who wants to buy a movie ticket.
#Calculate the total cost based on the following rules:
#Free for people under 3.
#$10 for people aged 3 to 12.
#$15 for anyone over 12.
#Print the total ticket cost.

age =None
price =None
while True:
    age =input("whta's your age : ")
    user_age =int(age)
    if user_age <= 3: price= 0
    elif 3<user_age>= 12: price=10
    else: price =15
    t_cost=len(user_age)*price
    print(t_cost)