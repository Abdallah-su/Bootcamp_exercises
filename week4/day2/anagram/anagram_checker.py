class AnagramChecker:
    def __init__(self):
        with open("sowpods.txt", "r" ) as f:
            self.words =[line.strip() for line in f] 

    def is_valid_word(self, word):
        if word.upper() in self.words:
          return True
        
        
    def is_anagram(self, word1, word2):
        word1_sorted=sorted(word1.upper())
        word2_sorted= sorted(word2.upper())
        if word1_sorted == word2_sorted:
            return True
    
    

    def get_anagrams(self, word):
         anagram_list = [ ]
         for character in self.words:
            if self.is_anagram(word, character) and word.upper() != character:
                anagram_list.append(character)
         return anagram_list

    
   

    

