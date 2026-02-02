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