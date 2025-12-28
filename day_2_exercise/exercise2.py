#Exercise 1 : Hello World-I love Python
print(('Hello World\n'*4)+('I love python\n'*4))

#Exercise 2 : What is the Season ?
#Instructions
#Ask the user to input a month (1 to 12).
#Display the season of the month received :
#Spring runs from March (3) to May (5)
#Summer runs from June (6) to August (8)
#Autumn runs from September (9) to November (11)
#Winter runs from December (12) to February (2)

month =input("type in any month(1-12): ")
user_month =int( month)
if 2 < user_month < 6 :
    print("the season is spring")
elif 5 < user_month < 9 :
    print("the season is summer")
elif 8 <user_month <12:
    print("the season id autumn")
elif user_month<= 12:
    print("the season is winter")
else:print ("invalid input")

      
