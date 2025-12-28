print('Hello World!\n'*4)


print(99**3 *8)


print(15 < 8) #False#print(5 < 3 ) # false
print(3 == 3) #True
print(3 == "3") #False 
#print("3" > 3) # False #cannot be compared
print("Hello" == "hello") #False


#Create a variable called computer_brand which value is the brand name of your computer.
#Using the computer_brand variable, print a sentence that states the following:
#"I have a <computer_brand> computer."

computer_brand = "Lenova"
brand=(f"I have a {computer_brand}  computer.")
print(brand)

#🌟 Exercise 5: Your information
#Instructions
#Create a variable called name, and set it’s value to your name.
#Create a variable called age, and set it’s value to your age.
#Create a variable called shoe_size, and set it’s value to your shoe size.
#Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2, and 3.
#Have your code print the info message.
#Run your code.

name = "Abdallah"
age = 32
shoe_size = 42
info = f"I'm {name}, {age}years old with a shoe size of {shoe_size}."
print(info)

#🌟 Exercise 6: A & B
#Instructions
#Create two variables, a and b.
#Each variable’s value should be a number.
#If a is bigger than b, have your code print "Hello World".
a = 47
b = 27
if a > b :
    print("Hello World.")

#Exercise 7: Odd or Even
#Instructions
#Write code that asks the user for a number and determines whether this number is odd or even.
number = input("type in a number : ")
Username = int(number)
if  Username %2 ==0 :
    print("the number is even")
else: print("the number is odd")

 #Exercise 8: What’s your name?
#Instructions
#Write code that asks the user for their name and determines whether or not you have the same name. Print out a funny message based on the outcome.

usern =input("what's your name :")
if usern == 'Abdallah' :
    print("you're the real gee")
else: print("you need to change your name")


#🌟 Exercise 9: Tall enough to ride a roller coaster
#Instructions
#Write code that will ask the user for their height in centimeters.
#If they are over 145 cm, print a message that states they are tall enough to ride.
#If they are not tall enough, print a message that says they need to grow some more to ride.

height = input("what's your height : cm")
user_height = int(height)
if user_height > 145 :
    print("you're tall enough to ride")
else :print("you need to grow more before you can ride")









