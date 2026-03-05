# Instruction: Information from the user
# Harder Daily Challenge
# Notice : solve this exercise using a lambda function.

# Ask a user for the following inputs 5 times:
# Name (string)
# Age (int)
# Score (int)
# Build a list of tuples using these inputs, each tuple should contain a name, age and score.
# Sort the list by the following priority Name > Age > Score.

print('kindly input these details for 5 people: Name, Age, Score')
user_info =[ ]
for i in range(5):
    name = input(f'kindly input the Name{i+1}: ')
    age =int(input(f'kindly input the Age{i+1}: '))
    score=int(input(f'kindly input the Score{i+1}: '))
    user_info.append((name,age,score))
print(f' original : {user_info}')
user_info_sorted =sorted(user_info, key = lambda x :( x[0], x[1], x[2]))
print(f'sorted : {user_info_sorted}')


# If the following tuples are given as input to the script:

# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
# Note : The lambda function will not print but sort



