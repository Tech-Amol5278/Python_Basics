# create a class laptop with attributes like brand name, model name, price
# create two objects/instances of laptop class

### Sol ####

class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand = brand_name
        self.model = model_name
        self.price = price


# creating objects

lap1 = Laptop('dell','d1',12000)
lap2 = Laptop('dell','d2',25000)

# 
print(lap1.price)
print(lap2.price)


