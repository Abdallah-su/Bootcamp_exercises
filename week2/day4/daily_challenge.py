#exercise 1
user_words = input('type in a list of words atleast 3 separated by ",": ')
words = user_words.split(',')
sorted_word = sorted(words)
print(','.join(sorted_word))

#exercise 2
def longest_word(sentence):
    words = sentence.split(' ')
    long_word = max(words, key =len)
    print(long_word)

sentence='type in a list of words atleast 3 separated by'
longest_word(sentence)

