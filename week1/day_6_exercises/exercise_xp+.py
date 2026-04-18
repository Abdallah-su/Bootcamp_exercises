#  Exercise 1 : Student Grade Summary
# Instructions
# You are given a dictionary containing student names as keys and lists of their grades as values. 
# Your task is to create a summary report that calculates the average grade for each student,
#  assigns a letter grade, and determines the class average.
import re


student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}
# Requirements:
# Calculate the average grade for each student and store the results in a new dictionary called student_averages.
for student,grades in student_grades.items():
    average = round(sum(grades)/len(grades), 2)
    student_averages ={student: average}
    
# Assign each student a letter grade (A, B, C, D, F) 
# based on their average grade according to the following scale,
#  and store the results in a dictionary called student_letter_grades:
# A: 90 and above
# B: 80 to 89
# C: 70 to 79
# D: 60 to 69
#  F: Below 60
student_letter_grades = {}
for student, average in student_averages.items():
    if average >= 90:
        letter_grade = 'A'
    elif average >= 80:
        letter_grade = 'B'
    elif average >= 70:
        letter_grade = 'C'
    elif average >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    student_letter_grades[student] = letter_grade


# Calculate the class average (the average of all students’ averages) and print it.

class_average = sum(student_averages.values)/len(student_averages)
print(class_average)
# Print the name of each student, their average grade, and their letter grade.
# Hints:
# Use loops to iterate through the student_grades dictionary.
# You may use sum() and len() functions to help calculate averages.
# Initialize empty dictionaries for student_averages and student_letter_grades before filling them with data.
