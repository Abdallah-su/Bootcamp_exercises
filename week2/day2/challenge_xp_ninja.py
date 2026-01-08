#Exercise 1 : What’s your name ?

def get_fullname(first_name,last_name, middle_name = " "):
    #middle_name is optional
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name

print(get_fullname(first_name="john", middle_name="hooker", last_name="lee"))
print(get_fullname(first_name="bruce", last_name="lee"))


#Exercise 2 : From English to Morse

def eng_morse_trans(statement):
    MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}
    translate = []
    for letter in statement.upper():
        if letter in MORSE_CODE_DICT:
            translate.append(MORSE_CODE_DICT[letter])
    return " ".join(translate)     

print(eng_morse_trans("i am at home"))

#Exercise 3 : Box of stars

def print_box(*words): 
     max_lenght = max(len(word)for word in words )
     width = 4 + max_lenght
     upper_stars ="*" * width
     print(upper_stars)
     for word in words:
      print(f"* {word.ljust(max_lenght)} *") 
     print(upper_stars)

print_box("Hello", "World", "in", "reallylongword", "a", "frame")