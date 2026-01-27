from func import sum_up
sum_up(67, 80 )

#exercise 3
import string
import random
all_letters = string.ascii_letters
the_string =' '
#print(all_letters)
#print(ran_char)
for _ in range(5):
    ran_char = random.choice(all_letters)
    the_string += ran_char
print(the_string)

#exercise 4
from datetime import date
current_date = date.today()
print(current_date)

#exerciose 5
from datetime import datetime
#current_date1 = datetime.today().date()
#current_time =datetime.today().time()
#print(current_date1)
#print(current_time)
current_datetime = datetime.now()
first_jan = datetime(2026, 1, 1,0,0,0,0,)
remaining_time = first_jan - current_datetime
time_left =remaining_time
print(first_jan)
print(current_datetime)
print(remaining_time)

#exercise 6
def minutes_lived(birth_date):
    bd = datetime.strptime(birth_date, "%Y-%m-%d")
    todays_date = datetime.now()
    years_lived = todays_date - bd
    minutes_lived = years_lived.total_seconds() / 60
    print (f"you've lived {int(minutes_lived)} minutes in your life ")

minutes_lived("1993-05-26")

#exercise7
from faker import Faker
fake = Faker()

user_list = [ ]
def user_dict(user_number):
  for _ in range(user_number):
     users_dict = {"user_name":fake.name(), "user_address":fake.address(), "user_language_code":fake.language_code()}
  user_list.append(users_dict)
  
  

user_dict(5)
print(user_list)

