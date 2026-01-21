#exercise 1
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        for currency1, currency2 in self.currency:
            if currency1 == currency2:
                continue
            else: raise Exception("maths error")
            

    def __add__(self,  b):
        return self.amount + b
    
    
    
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
print(c1.__add__(c2))