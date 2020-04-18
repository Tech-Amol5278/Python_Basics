# Inheritance intro
# this is the phone class created in previous slides, suppose if we want to make a new class for smartphones
# which will have the base features of phone class

class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model = model_name
        self.price = max(price,0)

    def make_a_call(self,phone_num):
        print(f"Calling {phone_num} .....")

    def full_name(self):
        print(f"{self.brand} {self.model}")


## see the Inheritance below
# this Smart phones always have additonal features such as Rear camera, front camera on top of the base featues (Like Phone class)
# Not necessary to write code for base features again, we can simply invoke the parent class
# two ways to inherit the parent class:
#   parent_class_name.__init__(attributes to inherits from parent inluding self separated by comma)
        # ex: Phone.__init__(self,brand,model_name,price)  # which is uncommon way
#
#   super().__init__(attributes to inherit from parent excluding self)
        # ex: super().__init__(brand,model_name,price)        # Common way
class SmartPhone(Phone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
# two ways
        Phone.__init__(self,brand,model_name,price)   # Uncommon way
# or
        # super().__init__(brand,model_name,price)        # Common way (Super() method inherits all the properties of the base class)
        # super().__init__(brand,model_name,price)
        self.ram = ram
        self.int_mem = internal_memory
        self.rearcam = rear_camera


phone1 = Phone('nokia','1100',5600)
smphone1 = SmartPhone('samsung','M30',14000,'4 GB','64 GB','8 MP')
print(smphone1.__dict__)
print(smphone1.price)



