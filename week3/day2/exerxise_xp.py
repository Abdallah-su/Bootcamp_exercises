class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())
class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'
all_cats = [Bengal('Beauty',2), Chartreux('Queen', 3), siamese('Gift', 1)]
for cat in all_cats:
    print(f"The cat name is {cat.name} and it's {cat.age} years old")
        
sara_pet = Pets(all_cats)
sara_pet.walk()

 #Exercise 2: Dogs
#Goal: Create a Dog class with methods for barking, running speed, and fighting.
 
class dog(): 
    def __init__(self,name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        
    def bark(self):
        return f'{self.name} is barking'  

    def speed(self) :
        return self.weight/self.age * 10
        
    def fight(self, other_dog):
        self.other_dog = other_dog
        self_power= self.speed() *self.age
        other_power =other_dog.speed() * other_dog.age
        if self_power < other_power:
              return f'{other_dog.name} has won'
        else: return f'{self.name} has won'


dog_1 = dog('Johny',4, 30)
dog_2 =dog('Gerald', 5, 35)
dog_3 = dog('Pique', 2, 20)
print(dog_1.bark())
print(dog_2.speed())
print(dog_1.fight(dog_2))


 #Exercise 3: Dogs Domesticated
#Goal: Create a PetDog class that inherits from Dog and adds training and tricks.
import random
class petDog(dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False
   
    def train(self):
        print(self.bark())
        self.trained = True
    
    def play(self, *args) :
        for dog in args:
            print(f'{self.name}')

    def do_a_trick(self) :
        if self.trained == True:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            random_trick = random.choice(tricks)
        print(f"{self.name} {random_trick}")


my_dog = petDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()

friend_dog = petDog("havre", 3, 12)
friend_dog.train()
friend_dog.play("yoo", "fighter")
friend_dog.do_a_trick()


#Exercise 4: Family and Person Classes
#Goal:
#Practice working with classes and object interactions by modeling a family and its members.

class person():
    def __init__(self, first_name, age, last_name = ' '):
        self.first_name =first_name
        self.age = age
        self.last_name = " "

    def is_18(self):
        if self.age >= 18 :
            return True
        else: 
            return False
        
class family():
   def __init__(self, last_name):
        self.last_name =last_name
        self.members =[ ]
        

   def born(self, first_name, age):
       new_person = person(first_name, age)
       new_person.last_name = self.last_name
       self.members.append(new_person) 

   def check_majority(self,first_name):  
       for member in self.members: 
           if member.first_name == first_name:
               if member.is_18():
                print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                return True
               else:
                print("Sorry, you are not allowed to go out with your friends.")
                return False
           
   def family_presentation(self):
#It should print the family’s last name.
#Then, it should print each family member’s first name and age.
    print(f'Family name: {self.last_name}')
    for member in self.members:
        print(f'first_name: {member.first_name} Age: {member.age}')

my_family = family(last_name= "Suallah")
my_family.born("Abdallah", 32)
my_family.born("Zainab", 12)
my_family.born('Siaka', 20)
my_family.born('Aramata', 28)
my_family.check_majority("Zainab")
my_family.check_majority("Aramata")
my_family.family_presentation()

       
        


