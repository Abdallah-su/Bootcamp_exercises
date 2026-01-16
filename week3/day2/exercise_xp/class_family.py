

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

       