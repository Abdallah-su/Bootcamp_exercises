#exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dict = dict(zip(keys, values))
print(my_dict)

#exercise 2
#Family members’ ages are stored in a dictionary.
#The ticket pricing rules are as follows:
#Under 3 years old: Free
#3 to 12 years old: $10
#Over 12 years old: $15

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
cost1 = 0
cost2 = 0           
cost3 = 0
for name,age in family.items():
    if age < 3:
        cost1 += 0
    elif 3 <= age <= 12:
        cost2 += 10      
    else:
        cost3 += 15
total_cost = cost1 + cost2 + cost3
print(f"The total cost for the family is ${total_cost}")

#         exercise 3
brand = {"name": "Zara",
"creation_date": 1975,
"creator_name": "Amancio Ortega Gaona",
"type_of_clothes": ["men", "women", "children", "home"],
"international_competitors":[ "Gap", "H&M", "Benetton"],
"number_stores": 7000,
"major_color":{
"France": "blue", 
"Spain": "red", 
"US":[ "pink", "green" ]}}

brand["number_stores"]= 2
print(f'{brand["name"]} has {brand["type_of_clothes"][0]}, {brand["type_of_clothes"][1]}, {brand["type_of_clothes"][2]} and {brand["type_of_clothes"][3]} clothes ')
brand["country_creation"] = "Spain"
#checking international competitors
print(brand["international_competitors"])
brand["international_competitors"].append("Desigual")

#Delete the creation_date key.
del brand["creation_date"]

#Print the last item in international_competitors.
print(brand["international_competitors"][3])

#Print the major colors in the US.
print(brand["major_color"]["US"])

#Print the number of keys in the dictionary.
print(len(brand))
#Print all keys of the dictionary
for key in brand:
    print(key)





#Create another dictionary called more_on_zara with 
# creation_date and number_stores. Merge this dictionary 
# with the original brand dictionary and print the result.
more_on_zara = {"creation_date":"1950-10-01", "number_stores": 10}
merged_brand = brand | more_on_zara
print(merged_brand)

#exercise 4

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
#Create a dictionary that maps characters to their indices:
#{"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
map_indices = {index: user for index, user in enumerate(users)}
print(map_indices)

#2. Create a dictionary that maps indices to characters:
map_char = {user: index for index, user in enumerate(users)}
print(map_char)
#{0: "Mickey", 1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
#3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:
#{"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
user_sort = sorted(users)
sorted_alpha = {user: index for index, user in enumerate(user_sort)}
print(sorted_alpha)
