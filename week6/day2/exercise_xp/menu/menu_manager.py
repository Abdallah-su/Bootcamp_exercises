
#In the file menu_manager.py, create a new class called MenuManager
#Create a Class Method called get_by_name that will return a single item 
# from the Menu_Items table depending on it’s name, 
# if an object is not found (there is no item matching
#  the name in the get_by_name method) return None.

import psycopg2
connection = psycopg2.connect(
user = 'postgres',
password = 'Abs0240574227',
host = 'localhost',
port = '5432',
database = 'menu'
)

cursor = connection.cursor()

class MenuManager:
    @classmethod
    def all(cls):
        query ="select item_name, item_price from menu_item"
        cursor.execute(query)
        connection.commit()
        menu = cursor.fetchall()
        return menu
        

        
        
    @classmethod
    def get_by_name(cls, item_name):
        query = "select item_name, item_price from menu_item where item_name = %s"
        cursor.execute(query, (item_name,))
        connection.commit()
        dish = cursor.fetchone()
        return dish
   
    