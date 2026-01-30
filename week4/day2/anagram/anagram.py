from anagram_checker import AnagramChecker
user_character = AnagramChecker()
while True:
    user_input= input("""        Welcome to Anagram Game!
    Type in a word or x to exit the game: """)
    user_input = user_input.strip().upper()
    if user_input == "x":
        break
    
    user_word = user_input.split()
    if len(user_word) != 1 or not user_word[0].isalpha():
        print("Error! only single word and aphabets are required")
        continue

    if user_character.is_valid_word(user_word[0]):
        anagrams = user_character.get_anagrams(user_word[0])
        if anagrams:
            print(f"Anagrams for {user_word[0]} are: {', '.join(anagrams)}")
        else:
            print(f"No anagrams found for {user_word[0]}.")
    else:
        print(f"{user_word[0]} is not a valid word. Please try again.")
        

    
    
    
    
   
  
        
