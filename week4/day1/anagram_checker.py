class AnagramChecker:
    def __init__(self):
        with open("sowpods.txt", "r" ) as f:
            self.words =[line.strip() for line in f] 

    def is_valid_word(self, word):
        if word.upper() in self.words:
            return word.upper()

    def is_anagram(self, word1, word2):
        word1=sorted(word1.upper())
        word2 = sorted(word2.upper())
        if word1 == word2:
            return True
        else: return False
        

    def get_anagrams(self, word):
        anagram_list = [ ]
        for characters in self.words:
            if self.is_anagram(word, characters):
                word.upper() != characters
                anagram_list.append(characters)
        return   anagram_list

    
   
checker = AnagramChecker()
print(checker.get_anagrams('stew'))

    

