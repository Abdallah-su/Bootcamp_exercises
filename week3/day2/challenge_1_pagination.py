import math
#  1: Create the Pagination Class

# Define a class called Pagination to represent paginated content.
# It should optionally accept a list of items and a page size when initialized.

#  Step 2: Implement the __init__ Method

# Accept two optional parameters:
# items (default None): a list of items
# page_size (default 10): number of items per page

# Behavior:

# If items is None, initialize it as an empty list.
# Save page_size and set current_idx (current page index) to 0.
# Calculate total number of pages using math.ceil.
 

class Pagination:
    def __init__(self, page_size = 10, items = None):
        self.items = items if items is not None else []
        self.page_size = int(page_size)
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)
# Step 3: Implement the get_visible_items() Method

# This method returns the list of items visible on the current page.
# Use slicing based on the current_idx and page_size.
      
    def  get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]
#   Step 4: Implement Navigation Methods
# These methods should help navigate through pages:
# go_to_page(page_num)
# → Goes to the specified page number (1-based indexing).
# → If page_num is out of range, raise a ValueError.
# first_page()
# → Navigates to the first page.
# last_page()
# → Navigates to the last page.
# next_page()
# → Moves one page forward (if not already on the last page).
# previous_page()
# → Moves one page backward (if not already on the first page).
# 📝 Note:
# Pages are indexed internally from 0, but user input is expected to start at 1.
# All navigation methods (except go_to_page) should return self to allow method chaining.

    
    def next_page(self):
            if self.current_idx < self.total_pages - 1:
                self.current_idx += 1
            return self.get_visible_items() 
    
    def previous_page(self):
            if self.current_idx > 0:
                self.current_idx -= 1
            return self.get_visible_items()  


    def go_to_page(self, page_number):
            if 0 <= page_number < self.total_pages:
                self.current_idx = page_number
            return self.get_visible_items()
    def get_total_pages(self):
            return self.total_pages
    def get_current_page(self):
            return self.current_idx + 1
    def add_item(self, item):
            self.items.append(item)
            self.total_pages = math.ceil(len(self.items) / self.page_size)
            return self.items
    def remove_item(self, item):
            if item in self.items:
                self.items.remove(item)
                self.total_pages = math.ceil(len(self.items) / self.page_size)
            return self.items
    def clear_items(self):
            self.items = []
            self.current_idx = 0
            self.total_pages = 0
            return self.items
    def get_all_items(self):
            return self.items
    def set_page_size(self, page_size):
            self.page_size = int(page_size)
            self.total_pages = math.ceil(len(self.items) / self.page_size)
            self.current_idx = 0
            return self.page_size
    def get_page_size(self):
            return self.page_size
    def is_first_page(self):
            return self.current_idx == 0
    def is_last_page(self):
            return self.current_idx == self.total_pages - 1                
    
    
   