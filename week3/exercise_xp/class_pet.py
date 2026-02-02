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
