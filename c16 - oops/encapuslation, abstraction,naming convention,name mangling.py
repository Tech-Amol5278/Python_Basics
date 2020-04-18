# Encapsulation
# abstraction
# some special naming conventions
# name mangling (not a convention)


#### 



class Phone:
    def __init__(self,brand,model_name,price,feature):
        self.brand = brand
        self.model = model_name
        self._price = price
        self.__feature = feature

    def make_a_call(self,phone_num):
        print(f"Calling {phone_num} .....")

    def full_name(self):
        print(f"{self.brand} {self.model}")

phone1 = Phone('nokia','1100',5600,'camera')
## Encapsulation:
# Consider above example:
#   we created class
#   we added instance variables
#   we created funcitions to call and to get the full name of the model
# 
# Process of having data and its functions at one location, is called Encapsulation
# #########################################################################################
## Abstraction:
l = [7,2,6,3] 
l.sort()
print(l)  
# Consinder above Example of List which is a class in python   
#   we have performed sort method on class List
#   sort has multiple algorithms such as tim(which is being used in python) which is coaded and given a SORT method
#   Process of hiding the complexity and making a reusable objects is called Abstraction
# ##########################################################################################
# Naming Conventions
# Different programming languages have diffrent accessibility options such as private,public
# # Python's objects by default accessed publicaly
# For exmample 
#   _name   : Private naming convention,in Phone class (_Phone: Denotes developer, that this is private. not to tamper )
#   __name__: called as dunder / magic methods
# Note : Though _name is private, we can change its attiributes(since it is limited to devlopers only for readability)
# See below
print(phone1._price)
phone1._price = 1200  ## changing attributes
print(phone1._price)   
#################################################################################################
# name mangling (not a convention)
#   __name : this is used for inheritance
# for example 
print(phone1.__dict__)   ## __feature
# {'brand': 'nokia', 'model': '1100', '_price': 1200, '_Phone__feature': 'camera'}
# name has changed, __feature >> _Phone__feature for inheritance




