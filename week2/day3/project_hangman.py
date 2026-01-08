#Instructions
#The computer choose a random word and mark stars for each letter of each word.
#Then the player will guess a letter.
#If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
#If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
#The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
#The player can’t guess the same letter twice.

import random
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)
display_word = ["*"] * len(word)
attempt = 6
guessed_word =[]
Hag_gallow = [""" game over""",
                 """   o
                     / | \\
                      | |""" ,
           """  o
              / | \\
               | """,
             """  o
                 /|\\""",
              """  o
                 / |""",
            """  o 
                 |""",
            """  o """] 

print("Welcom to Hagman Word Challenge")
print(" ".join(display_word))

while "*" in display_word and attempt > 0 :
    guess = input("Enter a word: ").lower()
    if guess in guessed_word:
        print(f"youve already guessed {word} !")
        continue
    guessed_word.append(guess)
    if guess in word :
        print("your guess is right!")
    else:
        attempt -= 1
        print(f"you have {attempt} attempt remainig") 
        print(Hag_gallow[attempt]) 
else:print(f"the word is {word}")

    


