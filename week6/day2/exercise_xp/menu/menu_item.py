#In the file menu_item.py, create a new class called MenuItem,
#  the attributes should be the name and price of each item.

import psycopg2
connection = psycopg2.connect(
user = 'postgres',
password = 'Abs0240574227',
host = 'localhost',
port = '5432',
database = 'menu'
)

cursor = connection.cursor()
class MenuItem:
    def __init__(self, item, price):
        self.price = price
        self.item = item

    def save (self):
        query = "insert into MenuItem(item_name, item_price) values (%s, %s);"
        cursor.execute(query,(self.item, self.price))
        connection.commit()
        print(f"Your order for {self.item} is saving, a momment please!")
        return True
    
    def delete(self):
        query = "delete from MenuItem where self.item = %s"
        cursor.execute(query, (self.item,) ) 
        connection.commit()
        print("your order for {self.item} is being deleted")
        return self.item
   
    def update(self, other_item,  other_price):
        query = "update MenuItem set self.item = %s, self.price = %s"
        cursor.execute(query,(self.item, other_item, other_price)) 
        connection.commit()
        

        


       


#Create several methods (save, delete, update) these methods will allow a user to save, delete and 
#update items from the Menu_Items table. The update method can update the name
#  as well as the price of an item.

#In the file menu_manager.py, create a new class called MenuManager
#Create a Class Method called get_by_name that will return a single item 
# from the Menu_Items table depending on it’s name, 
# if an object is not found (there is no item matching
#  the name in the get_by_name method) return None.

#Create a Class Method called all_items which will return a list of all the items from the Menu_Items table.

