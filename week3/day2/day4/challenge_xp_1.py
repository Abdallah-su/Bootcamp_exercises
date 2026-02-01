#Your Circle class should be able to:

#✅ Compute the circle’s area.
#✅ Print the attributes of the circle — use a dunder method (__str__ or __repr__).
#✅ Add two circles together and return a new circle with the new radius — use a dunder method (__add__).
#✅ Compare two circles to see which is bigger — use a dunder method (__gt__).
#✅ Compare two circles to check if they are equal — use a dunder method (__eq__).
#✅ Store multiple circles in a list and sort them — implement __lt__ or other comparison methods.

class circle:
   def __init__(self, radius):
      self.radius = radius
   def __str__(self):
      return f"Circle with radius: {self.radius}"
   def __add__(self, other):
      if isinstance(other, circle):
         return circle(self.radius + other.radius)
   def area(self):
      return 3.14 * (self.radius ** 2) 
   
   def  __gt__(self, other):
      if isinstance(other, circle):
         return self.radius > other.radius
   def __lt__(self, other):
      if isinstance(other, circle):
         return self.radius < other.radius
   def __eq__(self, other):
      if isinstance(other, circle):
         return self.radius == other.radius     
circle1 = circle(5)
circle2 = circle(10)       
circle3 = circle(7)
print(circle1)    
print(circle1.area())
print(circle1.__gt__(circle2))