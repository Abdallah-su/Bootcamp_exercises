# Create a class called Text.
# The __init__ method should take a string as an argument and store it in an attribute (e.g: self.text).

class Text:
    def __init__(self, sentence):
        self.sentence = sentence

# Create a method called word_frequency(word).
# Split the text attribute into a list of words.
# Count the occurrences of the given word in the list.
# Return the count.
# If the word is not found, return None or a meaningful message.

    def  word_frequency(self, word):
        words_list =self.sentence.split()
        if word in words_list:
            return words_list.count(word)
        else: return None
# Create a method called most_common_word().
# Split the text into a list of words.
# Use a dictionary to store word frequencies.
# Find the word with the highest frequency.
# Return the most common word.
      
    def most_common_word(self):
        word_count_dict={}
        words = self.sentence.split()
        for word in words:
            word_count_dict[word]=words.get(word, 0) + 1
        return max(word_count_dict, key= word_count_dict.get)
    
# Create a method called unique_words().
# Split the text into a list of words.
# Use a set to store unique words.
# Return the unique words as a list.

    def unique_words(self):
        words = self.sentence.split()
        unique_words =set(words)
        word_list =list(unique_words)
        return word_list
# Step 5: Implement from_file Class Method

# Create a class method called from_file(file_path).
# Open the file at file_path in read mode.
# Read the file content.
# Create and return a Text instance with the file content as the text.
    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r') as file:
            content=file.read()
        return cls(content)


s='who are  are are you you'
s=Text(s)
print(s. word_frequency('you'))
print(s.most_common_word())
print(s.unique_words())