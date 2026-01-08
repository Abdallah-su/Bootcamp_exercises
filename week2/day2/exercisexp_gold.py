#  Exercise 1 : When will I retire ?
#Instructions
#The point of the exercise is to check if a person can retire depending on their age and their gender.
#Note : Let’s say retirement age is 67 for men, and 62 for women (born after April, 1947).
#Create a function get_age(year, month, day)
#Hard-code the current year and month in your code (there are better ways of doing this, but for now it will be enough.)
#After calculating the age of a person, the function should return the age (the age is an integer).
#Create a function can_retire(gender, date_of_birth).
#It should call the get_age function (with what arguments?) in order to receive an age.
#Now it has all the information it needs in order to determine if the person with the given gender and date of birth is able to retire or not.
#Calculate. You may need to do a little more hard-coding here.
#Return True if the person can retire, and False if he/she can’t.
#Some Hints
#Ask for the user’s gender as “m” or “f”.
#Ask for the user’s date of birth in the form of “yyyy/mm/dd”, eg. “1993/09/21”.
#Call can_retire to get a definite value for whether the person can or can’t retire.
#Display a message informing the user whether they can retire or not.
#As always, test your code to ensure it works.
   
def get_age(year,month,day):
     current_year=2025
     current_month= 12
     current_day=23
     age = current_year - year
     if (current_month ,current_day)<(month, day):
           age -=1
     return  age

def can_retire(gender,birth_date):
     birth_date_format=birth_date.split("/")
     year, month, day =map (int, birth_date_format)  
     age = get_age(year, month, day)
     if gender == 'f' and age >= 62:
          return True
     elif gender == 'm' and age >= 67:
          return True
     else:
         return False

user_gender=input("Enter your gender(m/f): ")
user_age =(input("your date of brith(yyyy/mm/dd): "))
if (can_retire(user_gender, user_age)):
     print("congratulations! you can retire")
else:
     print("sorry it's not time to retire")


#Exercise 2 : Sum
#Instructions
#Write a function that accepts one parameter (an int: X) and returns the value of X+XX+XXX+XXXX.
#Example:
#If X=3, the output when calling our function should be 3702 (3 + 33 + 333 + 3333)
#Hint: treating our number as a int or a str at different points in our code may be helpful


def dont_add(i):
     return i + (i*11) + (i*111) + (i*1111)
print(dont_add(3))


#Exercise 3 : Double Dice

import random

def throw_dice():
     #a dice (6 faces)
     dice= random.randint(1,6)
     return dice

    
def throw_until_doubles():
    throw = 0
    while True:
        throw += 1
        face_1 = throw_dice()
        face_2 = throw_dice()
        if face_1 == face_2:
         return throw
     
def main_game():
    double =[]
    for _ in range(100):
        attempts = throw_until_doubles()
        double.append(attempts)
    total_throw = sum(double)
    average_throw =total_throw / 100
    print(f"it took you {total_throw} to reach 100 doubles")
    print(f"your average throw to reach a double is {average_throw}")

main_game()   