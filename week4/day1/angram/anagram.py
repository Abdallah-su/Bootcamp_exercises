from week4.day1.angram.anagram_checker import AnagramChecker
user_character = AnagramChecker()
while True:
    user_input= input("""        Welcome to Anagram Game!
    Type in a word or x to exit the game: """)
    user_input = user_input.strip()
    if user_input == "x":
        break
    user_word = user_input.split()
    if len(user_word) > 1 or not user_input.isalpha():
            print("Error! only single word and aphabets are required")
            continue
    if user_character.is_valid_word(user_input):
         anagrams = user_character.get_anagrams(user_input)
    print(f" The anagrams for your {user_input} are: {anagrams}") 
word = AnagramChecker()
print(word.get_anagrams(user_input))
         
    
    
    
   
  
        
