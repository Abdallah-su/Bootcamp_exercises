# Instructions:

# Use the provided Cat class to create three cat objects. Then, create a function to find the oldest cat and print its details.



# Step 1: Create Cat Objects

# Use the Cat class to create three cat objects with different names and ages.


# Step 2: Create a Function to Find the Oldest Cat

# Create a function that takes the three cat objects as input.
# Inside the function, compare the ages of the cats to find the oldest one.
# Return the oldest cat object.


# Step 3: Print the Oldest Cat’s Details

# Call the function to get the oldest cat.
# Print a formatted string: “The oldest cat is <cat_name>, and is <cat_age> years old.”
# Replace <cat_name> and <cat_age> with the oldest cat’s name and age.

class cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
    
cat1 =cat('huraira', 2)
cat2=cat('Bikr', 3)
cat3 =cat('yoo', 4)

def older(*group):
    older = group[0]
    for cat in group:
      if older.age < cat.age:
        return cat
oldest_cat = older(cat1,cat2,cat3)
print(f'the oldest cat is {oldest_cat.name} with an age of {oldest_cat.age}')


#  Exercise 2 : Dogs
# Goal: Create a Dog class, instantiate objects, call methods, and compare dog sizes.
# Instructions:

# Create a Dog class with methods for barking and jumping. 
# Instantiate dog objects, call their methods, and compare their sizes.


# Step 1: Create the Dog Class
# Create a class called Dog.
class Dog:
   def __init__(self, name, height):
      self.name =name
      self.height =height
   def bark(self):
      print(f'{self.name} goes woof') 
   def jump(self):
      print(f'{self.name} can jump {self.height*2}cm high')

# Step 2: Create Dog Objects
davids_dog = Dog("power", 40)
sarahs_dog = Dog("lovely", 30)
print(f"""
david's dog is called {davids_dog.name} and is {davids_dog.height} years old
Sarah's dog is called {sarahs_dog.name} and is {sarahs_dog.height} years old""")
davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()


# Step 4: Compare Dog Sizes
def compare(object_1, object_2):
  if object_1.height > object_2.height:
      print(f'{object_1.name} is bigger than {object_2.name}')
  elif object_1.height == object_2.height:
   print(f'{object_1.name} has the same size as {object_2.name}')
  else: print(f'{object_2.name} is bigger than{object_1.name}')

compare(davids_dog, sarahs_dog)

# 🌟 Exercise 3 : Who’s the song producer?
# Goal: Create a Song class to represent song lyrics and print them.
# Instructions:
# Create a Song class with a method to print song lyrics line by line.
# Step 1: Create the Song Class
# Create a class called Song.
# In the __init__ method, take lyrics (a list) as a 
# parameter and create a corresponding attribute.
class Song:
   def __init__(self, lyrics):
      self.lyrics =lyrics
   def sing_me_a_song(self):
      for line in self.lyrics:
         print(f'\n {line}')

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()


# 🌟 Exercise 4 : Afternoon at the Zoo
# Goal:
# Create a Zoo class to manage animals. The class should allow adding animals, displaying them, selling them, and organizing them into alphabetical groups.

# Instructions
# Step 1: Define the Zoo Class
# 1. Create a class called Zoo.

# 2. Implement the __init__() method:

# It takes a string parameter zoo_name, representing the name of the zoo.
# Initialize an empty list called animals to keep track of animal names.
# 3. Add a method add_animal(new_animal):
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name =zoo_name
        self.animals =[ ]

    def add_animal(self, *new_animals):
        for animal in new_animals:
           if animal not in self.animals:
               self.animals.append(animal)
        
    def get_animals(self):
        print(f'the animals in the {self.zoo_name} are:')
        for animal in self.animals:
           print(animal)
        print()

    def sell_animal(self, animal_sold):
        for animal in self.animals:
           if animal ==animal_sold:
              self.animals.remove(animal)

    def sort_animals(self):
        animals =sorted(self.animals)
        group = { }
        for animal in animals:
            first_letter =animal[0]
            if first_letter not in group:
              group[first_letter]=[animal]
            else: group[first_letter].append(animal)
        return group
              


    def get_groups(self):
        print(f'The animals in the {self.zoo_name} in alphabetical order')
        for key ,value in self.sort_animals().items():
          print(f'{key}:{value}')

place = Zoo('Kumasi zoo')
(place.add_animal('Baboon', 'Bear','Cat', 'Cougar','Lion''Zebra'))
place.get_animals()
place.sell_animal('Cat')
place.sort_animals()
place.get_groups()

