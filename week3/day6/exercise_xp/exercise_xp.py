def get_words_from_file():
    file= open("words.txt", "r")
    content=file.read()
    list_of_words = content.split()
    return list_of_words
    
def get_random_sentence(sentence_length):
    import random
    words = get_words_from_file()
    random_sentence = ' '.join(random.choices(words, k= sentence_length))
    return random_sentence

def main():
    print("Welcome to the Random Sentence Generator!")
    user_length = int(input("Enter the desired sentence length (number of words): "))
    if isinstance(user_length, int) and 2<= user_length<=20:
        sentence = get_random_sentence(user_length)
        print("Generated Sentence:")
        print(sentence)
    else:
        print(" Error! Please enter a valid number between 2 and 20.")
        exit()
if __name__ == "__main__":
    main()
