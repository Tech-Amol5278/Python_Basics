# property and setter decorator
# the below code from last slide it has below problems
#   1. this accepts the negative amount for price
        # sol: write a validation not to accept negative numbers
        # using getter(),setter()
#   2. After changing the price , complete specification shows the old price. 
        # sol: write those specification in seprate function
        # OR using property decorator




# class Phone:
#     def __init__(self,brand,model_name,price):
#         self.brand = brand
#         self.model = model_name
#         self._price = price
#         self.complete_spefic = f" {self.brand} {self.model_name} and price {_price}"

#     def make_a_call(self,phone_num):
#         print(f"Calling {phone_num} .....")

#     def full_name(self):
#         print(f"{self.brand} {self.model}")

# phone1 = Phone('nokia','1100',5600)
# print(phone1._price)
###################################################################################################

class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model = model_name
        if price >= 0:
            self._price = price
        else:
            self._price = 0     ###  or use below line
#        self._price = max(price,0)   ## this checks for the maximum number between given number and 0 and returns the max number either given number or 0
        # self.complete_spefic = f" {self.brand} {self.model} and price {self._price}"

    def make_a_call(self,phone_num):
        print(f"Calling {phone_num} .....")

    def full_name(self):
        print(f"{self.brand} {self.model}")
    
    def specs(self):
        return f" {self.brand} {self.model} and price {self._price}"

# @Property- using this decorator we can use this function as method and we can call this method as attribute
    @property
    def property_spec(self):
        return f" {self.brand} {self.model} and price {self._price}"        

# getter(), setter() for price validation
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,new_price):
        self._price = max(new_price,0)




phone1 = Phone('nokia','1100',-5600)
phone1._price  = 2200
print(phone1._price)
print(phone1.specs())
print(phone1.property_spec)   ## see here we are not given parenthesis()
### to set the new price from getter and setter
phone1.price  = 3400
print(phone1.price)   # used price instead of _price 
print(phone1.property_spec)   ## see here we are not given parenthesis()





