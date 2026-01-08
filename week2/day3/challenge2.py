#Exercise 1
#Instructions
#Draw the following pattern using for loops:
#    *
#   ***
#  *****
for i in range (1, 6, 2):
    stars = '*' * i
    print(stars.center(5))    



#Draw the following pattern using for loops:
   # *
  # **
 # ***
# ****
#*****

for i in range(1,6):
    m = '*' * i
    print(m.rjust(5))

#Draw the following pattern using for loops:
#*
#**
#***
#****
#*****
#*****
# ****
#  ***
#   **
#    *


for i in range(1, 6): 
        m = '*' * i
        n = m.rjust(5)
for i in range (5,0, -1) :   
        m = '*' * i
        n = m.ljust(5)
        
        print(n)


#Exercise 2
#Instructions
#Analyse this code before executing it. Write some commnts next to each line. Write the value of each variable and their changes, and add the final output. Try to understand the purpose of this program.
my_list = [2, 24, 12, 354, 233]

# i in the range of the list -1
for i in range(len(my_list) - 1):

#   the execution will not go beyond i 
    minimum = i

#  j in the range of lenth of the list starting from i +1    
    for j in range( i + 1, len(my_list)):

#if the values of j < i, execution cannaot go beyond j        
        if(my_list[j] < my_list[minimum]):
            minimum = j
            if(minimum != i):
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
print(my_list)
