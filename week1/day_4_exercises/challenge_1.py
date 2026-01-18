#challenge 1
user_number = int(input("type in a number: "))
user_length = int(input ("type in a length: "))
actual_length = user_length + 1
user_list = [j * user_number for j in range(1, actual_length)]
print(user_list)

#challenge 2
user_word = input ('type in a word that have atleast a letter repeated twice: ')
unique_word = None
results = ' '
for letter in user_word: 
    if letter != unique_word:
     results += letter
     unique_word = letter
print(results)    


