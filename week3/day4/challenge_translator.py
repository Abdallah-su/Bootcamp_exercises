from googletrans import Translator
from deep_translator import GoogleTranslator
translator = Translator()
translations = { }
french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 

for word in french_words:
    translated =GoogleTranslator(source ='fr', target= 'en').translate(word)
    translations[word]= translated
print(translations)
