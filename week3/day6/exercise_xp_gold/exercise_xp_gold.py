import json
menu = {
    "items": [
        {
            "name": "Vegetable soup",
            "price": 30
        },
        {
            "name": "Hamburger",
            "price": 44.9
        },
        {
            "name": "Milkshake",
            "price": 22.5
        },
        {
            "name": "Artichoke",
            "price": 18
        },
        {
            "name": "Beef stew",
            "price": 52.5
        }
    ]
}


#menu_dict = json.loads(menu)
with open('restaurant_menu.json', 'w') as json_file:
    json.dump(menu, json_file, indent=4)
file = open("restaurant_menu.json", "r")
content = file.read()
print(content)
#print(menu)
    