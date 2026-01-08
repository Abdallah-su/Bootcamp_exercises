#people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
#Using map and filter, try to say hello to everyone who's name is less than or equal to 4 letter

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

chosen =filter(lambda name : len(name)<= 4, people)
greetings =map(lambda name :f"hello {name}", chosen)g
print (list(greetings))