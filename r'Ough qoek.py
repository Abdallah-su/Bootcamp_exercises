rick_dict = {
    'first_name':'Rick',
    'last_name':'Sanchez'
}

print("my name is",  rick_dict['first_name'],  rick_dict['last_name'])


Va_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
print(Va_dict.items())
for item, xtics in Va_dict.items() :
    print (item, '->' ,xtics)


    my_dog = {
  'name': 'Rufus',
  'age': 4,
  'best_friend': {
    'name': 'Felix',
    'age': 4.5
  },
  'favorite_foods': ['steaks', 'sausages', 'shawarma']
}
print() 
print
dog = my_dog.items()
print(my_dog ['best_friend'] ['name'])

rick_dict['last_name'] = 'frank'
print (rick_dict)
rick_dict['origin']= 'Ghana'
print(rick_dict)
del rick_dict['first_name']
rick_dict['first_name'] = 'frank'
print(rick_dict)
print(rick_dict.keys())
print(rick_dict.values())



my_books = {
  "title": "Harry Potter",
  "author": "JK Rowling",
}

for x, y in my_books.items():
    print(" the " +  x + " is " +  y)

print("the", x, "is", y )


for item in enumerate('abcd'):
    print(item)

b = "abdallah"
for c in enumerate(b) :
    print(c)

for (index_count, letter) in enumerate('abcd'):
    print('At index {} the letter is {}'.format(index_count, letter))
    print('At index {} the letter is{}' .format(letter, index_count))

for letter in 'Leonardo':t
    if letter == 'a':
       pass
    print(letter, end='') # end='' renders each letter next to the other

    i = 1
    while i = 0 :
    print('it ok')

print('Hello World!\n'*4)\


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}
    return full_name.title()
get_formatted_name('abdallah', 'suallah')



b= [" " for _ in range(4)]
print(b)









