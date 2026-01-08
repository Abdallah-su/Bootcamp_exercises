#Exercise 1: Formula
#Instructions
#Write a program that calculates and prints a value according to this given formula:
#Q = Square root of [(2 * C * D)/H]
#Following are the fixed values of C and H:
#C is 50.
#H is 30.
#Ask the user for a comma-separated string of numbers, use each number from the user as D in the formula and return all the results
#For example, if the user inputs: 100,150,180
#The output should be:
#18,22,24

C = 50
H = 30
result = [ ]
user_list = input("type in a list of numbers seperated by ',':  ")
for D_str in user_list.split(","):
    D = int(D_str)
    Q = int((2*C*D)/H)**0.5
    result.append(str(Q))
print(",".join(result))

#Exercise 2 : List of integers
my_number = [22, 47, 99, -80, 22, 99, 54, -23, 5, 7] 
#B =  [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
#C = [3, 21, 76, 53, 9, -82, -3, 49, 1, 76]  
#D = [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]

#2. Print the following information:
#a. The list of numbers – printed in a single line
#b. The list of numbers – sorted in descending order (largest to smallest)
#c. The sum of all the number
print(my_number)
print(sorted(my_number))
print(my_number)
#3. A list containing the first and the last numbers.
#4. A list of all the numbers greater than 50.
#5. A list of all the numbers smaller than 10.
#6. A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.
new_list =[ ]
new_list.append(my_number[0])
new_list.append(my_number[-1])
print(new_list)
num50 = [ ]
num10 = []
numsquare = [ ]
for num in my_number:
    if num > 50:
        num50.append(num)
    elif num < 10:
        num10.append(num)
print(num50)
print(num10)
for num in my_number:
    numsquare.append(num**2)
print(numsquare)

#7. The numbers without any duplicates – also print how many numbers are in the new list.
#8. The average of all the numbers.
#9. The largest number.
#10.The smallest number.
#11. Bonus: Find the sum, average, largest and smallest number without using built in functions.
#12. Bonus: Instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100. Ask the user for an integer between -100 and 100 – repeat this question 10 times. Each number should be added into a variable that you created earlier.
#13. Bonus: Instead of asking the user for 10 integers, generate 10 random integers yourself. Make sure that these random integers are between -100 and 100.
#14. Bonus: Instead of always generating 10 integers, let the amount of integers also be random! Generate a random positive integer no smaller than 50.
#15. Bonus: Will the code work when the number of random numbers is not equal to 10?
set_nums = set(my_number)
my_new_num =list(set_nums)
print(my_new_num)
print(len(my_new_num))
average = sum(my_number)/len(my_number)
print(average)
sorted_list = sorted(my_number)
print(sorted_list[0])
print(sorted_list[-1])
#Exercise 3: Working on a paragraph
#Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
#Paste it to your code, and store it in a variable.
#Let’s analyze the paragraph. Print out a nicely formatted message saying:
#How many characters it contains (this one is easy…).
#How many sentences it contains.
#How many words it contains.
#How many unique words it contains.
#Bonus: How many non-whitespace characters it contains.
#Bonus: The average amount of words per sentence in the paragraph.
#Bonus: the amount of non-unique words in the paragraph.

