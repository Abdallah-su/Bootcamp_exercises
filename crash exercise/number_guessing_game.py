import random
def number_guessing_game()

#random number define and the number of attempts
random_number=random.randint(1, 100)
attempts = 7
#the rules of the game
print("choose a random number between 1 and 100")
print("you have 7 attempts to guess the number")
print(f"you have {attempts} attempts to guess it.")
#how many attempts remainiing
#for loop tocontrol the number of attempts
#range(7)gengrates numbers from 0 to 6 for 7 attempts(MAX_ATTEMPTS)
attempts_remainder = MAX_ATTEMPTS-(attempt + 1)
while attempt > 0:
#user input to guess the number
user_guess = int(input(f"/nAttempt #{attempt_number +1} : Enter your guess: )
#check if the guess is correct
if user_guess==random_number: print(f"/n congratulations! you guessed the number correctly.{random_number} in {atempt_number +1} attempts ")
    if user_guess < random_number:
        print("your guess is too low try again")
    elif user_guess > random_number:
        print("your guess is too high try again")
      else print("congratulations! you guessed the number correctly.")
        break
    attempt -= 1
    if attempt > 0:
    print(f"you have {attempt} attempts left.")
    else:
        print(f"sorry, you've used all your attempts. The correct number was {random_number}.")

