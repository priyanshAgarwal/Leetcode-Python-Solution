# cook your dish here

"""

"""

class Item:

    def __init__(self,name:str,price:float,quantity:int=1) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity 

    
    def total_price(self)->int:
        return self.quantity * self.price


item1 = Item('Iphone','Hellp',5)

print(item1.total_price())


print(item1.__dict__)