# exercise 1
description ="strings are..."
#make it uppercase
print(description.upper())

#replace the word "are" to "is"
print (description.replace("are", "is"))

#print "word"
print("strings")


#exercise 2
#Create a variable called my_age, use python to know how old you will be in 123879 years
my_age =32
later_age =123879 +my_age
print (later_age)

#exercis 3
#Check what is the type of each value, then change it: if it is a string, make it an integer and vice-versa:
bank_balance = '33000'
phone_number = 532287514
print(type(bank_balance))
print(type(phone_number))
print(int(bank_balance))
print(str(phone_number))


#exercise 4
#Create a variable called first_name and a variable called last_name, and then print your full name using those two variables
first_name = "Abdallah"
last_name ="Suallah"
print (first_name +  last_name)


#exercise 5
x= 10
y = 5
z= 0
word1 ="hello"
word2 ="world"

#1. Check if x is less than y and y is greater than z.
print(x < y and y > z)

#2. Verify if word1 is not equal to word2.
print(word1 != word2)

#3. Use the bool() function to check the boolean value of z and word1.
print(bool(z))
print(bool(word1))


