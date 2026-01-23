
#In the file menu_manager.py, create a new class called MenuManager
#Create a Class Method called get_by_name that will return a single item 
# from the Menu_Items table depending on it’s name, 
# if an object is not found (there is no item matching
#  the name in the get_by_name method) return None.

class MenuManager:
    @classmethod
    def all(cls):
        return [ ]
        
    @classmethod
    def get_by_name(cls, item):
        item_list = all(cls)
        for object in item_list:
            if object == item :
                return object
        return None
   
    