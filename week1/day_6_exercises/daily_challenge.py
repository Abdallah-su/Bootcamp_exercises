# Challenge 1: Letter Index Dictionary
# Goal: Create a dictionary that stores the indices (number of the position) of each letter in a word provided by the user(input()).
word_dict = {}
user_word = input("Please enter a word: ")
for index, letter in enumerate(user_word):
    if letter in word_dict:
        word_dict[letter].append(index)
    else:
        word_dict[letter] = [index]
print(word_dict)    

    # Challenge 2: Affordable Items
    # Goal: Create a program that prints a list of items that can be purchased with a given amount of money.
items_purchase1 = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet1 = "$300"
items_purchase2= {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
wallet2 = "$100"
items_purchase3 = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
wallet3 = "$1"
def affordable_items(items_purchase, wallet):
   affordable_items = []
   wallet_amount = int(wallet.replace("$", "").replace(",", ""))
   for item, price in items_purchase.items():
      price_amount = int(price.replace("$", "").replace(",", ""))
      if price_amount <= wallet_amount:
        affordable_items.append(item)
   print("With", wallet, "you can afford:", affordable_items)

affordable_items(items_purchase1, wallet1)
affordable_items(items_purchase2, wallet2)  
affordable_items(items_purchase3, wallet3)