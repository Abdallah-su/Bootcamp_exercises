import random
list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number   = 3728
for i in list_of_numbers:
    for j in list_of_numbers:
      if target_number == i + j :
        print(f"sum of {i} and {j} is {target_number}")       
        