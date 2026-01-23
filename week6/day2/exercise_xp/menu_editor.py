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
    
    user_order = input("""kindly select from the options;
                        View an Item(V)
                       Add an Item(A)
                       Delete an item(D)
                       update an item(U)
                       Show the Menu(S): """)
    if user_order == 'V':
        user_item= input ('Type in item to view: ')
        item_to_find = MenuManager.get_by_name(user_item) 
        if item_to_find:
            print (f"Item :{item_to_find.item} | price {item_to_find.price}")
        else:print(f"Sorry {user_item} not in the list")

    elif user_order == 'A':
        add_item_to_menu()

    elif user_order == 'D':
        remove_item_from_menu

    elif user_order == 'U':
        update_item_from_menu()

    elif user_order == 'S':
        show_restaurant_menu()
    else:print(" invalid input! try again")

def add_item_to_menu():
    user_add = input ('select what to add: ')
    user_price= input('select the price associated with the item added: ')
    item_to_add = MenuItem(user_add, user_price)
    if item_to_add:
            item_to_add.save()
    print(f"Your {item_to_add.item} is added ")

def remove_item_from_menu():
    user_delete = input('select what to delete: ')
    item_to_delete =  MenuManager.get_by_name(user_delete)
    if item_to_delete: 
        item_to_delete.delete()

def update_item_from_menu():
     user_update_item = input("Type in the item to confirm your ORDER: ")
     user_update_price = input("Type in the price to confirm ORDER: " )
     user_update = MenuManager.get_by_name(user_update_item)
     if user_update:
            user_update.update(user_update_item, user_update_price)
def show_restaurant_menu():
    all_select = MenuManager.all()
    print('\n ---RESTAURANT MENU---')
   
    for item in all_select:
        print(f"Your Menu is {item.item} | {item.price}")
    print('\n --------------------------')

if __name__ == "__main__":
     show_user_menu()


  