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
    show_restaurant_menu()
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
    global item_to_add
    user_add = input ('select what to add: ').title()
    user_price= input('select the price associated with the item added: ')
    item_to_add = MenuItem(user_add, user_price)
    if item_to_add:
            return item_to_add
    print(f"Your {item_to_add.item} is added ")
    


def remove_item_from_menu():
    user_delete = input('select what to delete: ').title()
    item_to_delete =  MenuManager.get_by_name(user_delete)
    if item_to_delete: 
        item_to_delete.delete()

def update_item_from_menu():
     user_update_item = input("Type in the item to confirm your ORDER: ").title()
     user_update = MenuManager.get_by_name(user_update_item)
     user_update_price = input('type in the associated price: ' )
     if user_update:
            user_update.update(user_update_item, user_update_price)
     print('Your order has been updated')

def show_menu():
    menu = [ ]
    if item_to_add:
        menu.append(item_to_add)
    print(menu)
    

def show_restaurant_menu():
    print('\n---------RESTAURANT MENU--------')
    menu = MenuManager.all()
    for dish in menu:
       print (f"\n {dish[0]}        |    {dish[1]}  ")
    print('\n --------------------------')

if __name__ == "__main__":
     show_user_menu()


  