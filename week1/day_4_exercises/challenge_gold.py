#Instructions
#Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
#Display a little cake as seen below:                                                                          
 #      ___iiiii___
#      |:H:a:p:p:y:|
 #   __|___________|__
  # |^^^^^^^^^^^^^^^^^|
   #|:B:i:r:t:h:d:a:y:|
  # |                |
   #~~~~~~~~~~~~~~~~~~~

#The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.

#Bonus : If they were born on a leap year, display two cake
from datetime import datetime,date
user_birthday = input ('type in your birth date (DD/MM/YYYY): ')
birth_day = datetime.strptime(user_birthday, "%d/%m/%Y").date()
today = date.today()
current_year = today.year
user_age =int(current_year - birth_day.year- ((today.month, today.day) <= (birth_day.month, birth_day.day)))
candles = 'i' * (user_age % 10)
num_candles= f'__{candles}__'
print(num_candles.center(20))
print('    |:H:A:P:P:Y:|   '.center(13))
print('|~~~~~~~~~~~~~~~~~~|'.center(13))
print('| :B:I:R:T:H:D:A:Y:|'.center(13))
print('|~~~~~~~~~~~~~~~~~~|'.center(13))  

