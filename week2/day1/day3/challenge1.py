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
          

