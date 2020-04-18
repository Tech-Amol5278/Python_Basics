# the class laptop and can be modified using the class variables(by defining the discout as class variable ).see below




class Laptop:
    discnt = 10   # default 10 percent discount
    def __init__(self,brand_name,model_name,price):
        self.brand = brand_name
        self.model = model_name
        self.price = price

    def apply_disc(self):
        discounted_price = self.price - (self.price * Laptop.discnt/100)
        return discounted_price



# creating objects
lap1 = Laptop('dell','d1',63000)
lap2 = Laptop('dell','d2',56000)


print(lap1.price)
print(lap1.apply_disc())


# to override the discount (this will override the default discount)
Laptop.discnt = 20
print(lap1.apply_disc())

# to know the available data in class inidiviual objects laptop
print(lap1.__dict__)

# all the laptops will have the same discounts
# Incase we need to have diffrent discounts for diffrent laptops, code can be tweaked as below.



class Laptop:
    discnt = 10   # default 10 percent discount
    def __init__(self,brand_name,model_name,price):
        self.brand = brand_name
        self.model = model_name
        self.price = price

    def apply_disc(self):
        discounted_price = self.price - (self.price * self.discnt/100)
        return discounted_price




lap1 = Laptop('dell','d1',63000)
lap2 = Laptop('dell','d2',56000)


lap1.discnt = 40
print(lap1.__dict__)  ## this changes as the discount object wise, default discount were 10
print(lap1.apply_disc())

