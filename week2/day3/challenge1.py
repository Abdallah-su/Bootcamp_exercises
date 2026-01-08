##Exercise 1
#Instructions
#Write a script that inserts an item at a defined index in a list.

#list the items in square bracket[] and assign it to a variabe
verbs =['go', 'come', 'recite', 'read' ]
#use the index to insert an item to the list
verbs.insert(2, 'run')
print(verbs)   


#Exercise 2
#Instructions
#Write a script that counts the number of spaces in a string.

#assign a string to a variabe
name = 'my name is Abdallah'
#use the count method with the print function
print(name.count(" "))



#Exercise 3
#Instructions
#Write a script that calculates the number of upper case letters and lower case letters in a string.


#get the string first
journey =" I am on a journey to Jerusalem"
#use loop and islower and isupper techniques
lower =0
upper = 0
for i in journey :
    if i.islower():
          lower +=1 
    else:upper += 1

print(lower)
print(upper)

#Exercise 4
#Instructions
#Write a function to find the sum of an array without using the built in function:
#>>>my_sum([1,5,4,2])
#>>>12

#define the function
def addi(num):
    total= 0
    for value in num:
         total=total +value

    print(total) 

addi([1,5,4,2])   


#Exercise 5
#Instructions
#Write a function to find the max number in a list
#find_max([0,1,3,50])
#50

#define the function
def maxi(m):
     big = m[0]
     for i in m:
          if i > big:
               big =i
     print(big)           

maxi([0,1,3,50])   

#(bonus)
def mini(n):
     less=n[0]
     for i in n:
          if less > i:
               less=i
     print(less)


mini([0,1,3,50])   


#Exercise 6
#Instructions
#Write a function that returns factorial of a number
#>>>factorial(4)
#>>>24

def fac(m):
     facto=1
     for i in range(1, m +1):
          facto *=i
     print(facto)


fac(3)
fac(6)
fac(4)      
fac(5)

#Exercise 7
#Instructions
#Write a function that counts an element in a list (without using the count method):
#>>>list_count(['a','a','t','o'],'a')
#>>>2

def my_count(m,i):
     total=0

     for letter in m:
          if letter ==i:
           total+=1
     print(total)      
          
my_count(['a','a','t','o'],'a')


#Exercise 8
#Instructions
#Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:
#>>>norm([1,2,2])
#>>>3

def my_l2(m):
     l1=0
     l2=0
     for i in m:
          l1+=(i**2)
          l2 =l1**0.5
     print(l2)
my_l2([1,2,2])     
my_l2([1,2,5,7,8])

#Exercise 9
#Instructions
#Write a function to find if an array is monotonic (sorted either ascending of descending)
#>>>is_mono([7,6,5,5,2,0])
#>>>True
#>>>is_mono([2,3,3,3])
#>>>True
#>>>is_mono([1,2,0,4])
#>>>False

def my_mono(m):
     descrease= all(m[i+1] <=m[i] for i in range(len(m)-1))    
     increase= all(m[i+1] >=m[i] for i in range(len(m)-1))
     print(increase or descrease)     
my_mono([2,3,3,3])
my_mono([1,2,0,4])

#Exercise 10
#Instructions
#Write a function that prints the longest word in a list.

def my_long(m):
     long=" "
     for long0 in m:
          if len(long0) >= len(long):
               long= long0
     print(long)          

verbs =['go', 'come', 'recite', 'read' ]
my_long(verbs)
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'creditcard', 'rush', 'south']
my_long(wordslist)

#Exercise 11
#Instructions
#Given a list of integers and strings, put all the integers in one list, and all the strings in another one.

int_string =['go', 'come', 'recite', 'read' ,2,5,67,9]
ints=[]
string=[]
for item in int_string:
     if type(item)== int:
          ints.append(item)
     else:string.append(item)
print(ints) 
print(string)


#Exercise 12
#Instructions
#Write a function to check if a string is a palindrome:
#>>>is_palindrome('radar')
#>>>True
#>>>is_palindrome
def my_pal(letter):
     if letter.lower()==letter[::-1]:
           print(True) 
           print(f"the {letter} is pallindrome")
     else: 
          print(False) 
          print(f"the {letter} is not pallindrome")
     
          
my_pal('radar')
my_pal('letter')

#Exercise 13
#Instructions
#Write a function that returns the amount of words in a sentence with length > k:
#>>>sentence = 'Do or do not there is no try'
#>>>k=2
#>>>sum_over_k(sentence,k)
#>>>3
def len3(sentence, k):
     words = sentence.split()
     total = 0
     for word in words:
          if len(word) > k:
               total += 1
     return total

statement='Do or do not there is no try'
print(len3(statement, 4))

#Exercise 14
#Instructions
#Write a function that returns the average value in a dictionary (assume the values are numeric):
#>>>dict_avg({'a': 1,'b':2,'c':8,'d': 1})
#>>>3

def average1(dict):
     values = dict.values()
     mean = sum(values)/len(values)

     return mean

          
values = {'a': 1,'b':2,'c':8,'d': 1}
print(average1(values))     


#Exercise 15
#Instructions
#Write a function that returns common divisors of 2 numbers:
#>>>common_div(10,20)
#>>>[2,5,10]

def common_dividers(m, n):
     values = []
     #highest value required
     highest = min(m, n)
     for number in range(2, highest + 1):
          if m % number == 0 and n % number == 0:
               values.append(number)
     return values

print(common_dividers(50, 60))

#Exercise 16
#Instructions
#Write a function that test if a number is prime:
#>>>is_prime(11)
#>>>True

def is_prime(value):
          if value % 2 != 0:
               number = True
               print(f"{value} is prime")
          else: 
               number = False
               print(f"{value} is not prime")
          return number


num1 = 11
print(is_prime(num1))

print(is_prime(12))


#Exercise 17
#Instructions
#Write a function that prints elements of a list if the index and the value are even:
#>>>weird_print([1,2,2,3,4,5])
#>>>[2,4]


def are_even(integers):
     my_list =[]
     for num in integers: 
          if num % 2 == 0 and integers.index(num) % 2 == 0:
                    my_list.append(num)
                    

     return my_list

print(are_even([1,2,2,3,4,5,6]))


def are_even1(integers):
     my_list2 =[]
     for i, num in enumerate(integers): 
          if num % 2 == 0 and i % 2 == 0:
                    my_list2.append(num)
                    

     return my_list2

print(are_even1([1,2,2,3,4,5,6]))

#Exercise 18
#Instructions
#Write a function that accepts an undefined number of keyworded arguments and return the count of different types:
#>>>type_count(a=1,b='string',c=1.0,d=True,e=False)
#>>>int: 1, str:1 , float:1, bool:2

def return_type (**my_type):
     occurence={}
     for value in my_type.values():
          data_type = type(value).__name__
          occurence[data_type]= occurence.get(data_type, 0) + 1
     return occurence     
     

print(return_type(a=1,b='string',c=1.0,d=True,e=False))


#exercise 19
#Instructions
#Write a function that mimics the builtin .split() method for strings.

#By default the function uses whitespace but it should be able to take an argument for any character and split with that argument.

def my_split(sentence, delimeter = " "):
     split_list = []
     curruent_word = " "
     for word in sentence :
          if word == delimeter:
               split_list.append(curruent_word)
               curruent_word = " "
          else:curruent_word += word
     split_list.append(curruent_word)     
     return split_list
 
print(my_split("the letter is not pallindrome"))



#Exercise 20
#Instructions
#Convert a string into password format.
#Example:
#input : "mypassword"
#output: "***********"

password = "njededre"
format = "*" * len(password) 
print(format) 

