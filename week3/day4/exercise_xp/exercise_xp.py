#exercise 1
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        if self.amount != 1:
          return f"{self.amount} {self.currency}s" 
        else: return f"{self.amount} {self.currency}"
            
    def __repr__(self):
        return f"{self.amount} {self.currency}s"

    def __add__(self, other):
        if isinstance(other, Currency):
            if other.currency == self.currency:
             return other.amount + self.amount
        else: raise TypeError (" {other.currency} and {self.currency} cannot be added")
         
    def  __iadd__(self, other):
       if isinstance(other, Currency):
           if other.currency != self.currency:
               raise TypeError (" {other.currency} and {self.currency} cannot be added")
           self.amount += other.amount
       else: self.amount += other
       return self
    
    
    
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
print(c1.__add__(c2))
print(c1)
print(repr(c1))
print(c1.__iadd__(5))
c1.__iadd__(c2)
print(c1)
print(c1.__add__ (c3))