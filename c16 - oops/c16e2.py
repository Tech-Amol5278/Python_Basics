## Modify the same class to get the discounted price



class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand = brand_name
        self.model = model_name
        self.price = price

    def apply_disc(self,num):
        discounted_price = self.price - (self.price*num/100)
        return discounted_price



# creating objects
lap1 = Laptop('dell','d1',12000)
lap2 = Laptop('dell','d2',25000)


print(lap1.price)
print(lap1.apply_disc(40))

