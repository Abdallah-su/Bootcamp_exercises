user_words = input( 'type in a list of words atleast 3 separated by ",": ' )
words = user_words.split(',')
sorted_word = sorted(words)
print(','.join(sorted_word))