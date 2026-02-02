#show_user_menu() - this function should display the program menu 
# (not the restaurant menu!), and ask the user to :
#View an Item (V)
#Add an Item (A)
#Delete an Item (D)
#Update an Item (U)
#Show the Menu (S)
#Call the appropriate function that matches the user’s input.


import psycopg2
connection = psycopg2.connect(
user = 'postgres',
password = 'Abs0240574227',
host = 'localhost',
port = '5432',
database = 'menu'
)

cursor = connection.cursor()

from menu_item import  MenuItem
from menu_manager import MenuManager
def show_user_menu():
    while True:
     user_order = input("""kindly select from the options;
                      View an Item(V)
                      Add an Item(A)
                      Delete an item(D)
                       update an item(U)
                       Show the Menu(S)
                        EXIT(E): """).upper()
    
     if user_order == 'V':
        user_item= input ('Type in item to view: ')
        item_to_find = MenuManager.get_by_name(user_item) 
        if item_to_find:
            print (f"Item :{item_to_find[0]} | price {item_to_find[1]}")
        else:print(f"Sorry {user_item} not in the list")

     elif user_order == 'A':
        add_item_to_menu()
 
     elif user_order == 'D':
        remove_item_from_menu()

     elif user_order == 'U':
        update_item_from_menu()

     elif user_order == 'S':
        show_menu()
     elif user_order == 'E':
         break
     else:print(" invalid input! try again")

def add_item_to_menu():
    user_item = input("Type in the item to add to the MENU: ").title()
    user_price = input("Type in the price associated with the item: ")
    item_to_add = MenuItem(user_item, user_price)
    item_to_add.save()
    return item_to_add

def remove_item_from_menu():
    user_item = input("Type in the item to DELETE from the MENU: ").title()
    item_to_delete = MenuManager.get_by_name(user_item)
    if item_to_delete:
        item_instance = MenuItem(item_to_delete[0], item_to_delete[1])
        item_instance.delete()
        print(f"{user_item} has been deleted from the menu")
    else:
        print(f"{user_item} not found in the menu")
    

def update_item_from_menu():
    user_item = input("Type in the item to UPDATE from the MENU: ").title()
    item_to_update = MenuManager.get_by_name(user_item)
    if item_to_update:
        item_instance = MenuItem(item_to_update[0], item_to_update[1])
        new_item_name = input("Type in the NEW name for the item: ").title()
        new_item_price = input("Type in the NEW price for the item: ")
        item_instance.update(new_item_name, new_item_price)
        print(f"{user_item} has been updated to {new_item_name} with price {new_item_price}")
    else:
        print(f"{user_item} not found in the menu")

def show_menu():
    show_restaurant_menu()

    

def show_restaurant_menu():
    items = MenuManager.all_items()
    print("Restaurant Menu:")
    for item in items:
        print(f"Item: {item[0]}, Price: {item[1]}")


if __name__ == "__main__":
     show_user_menu()


  