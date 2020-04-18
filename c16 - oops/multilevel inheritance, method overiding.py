# Multilevel inheritance:
#   this means inherting the having a parent class A inherted by class B. Class C which is inherited from class B
# MRO(Method Resolution Order):
#   This helps in identifying the search order of method i.e see below
#  |  Method resolution order:
#  |      SmartPhone 
#  |      Phone
#  |      builtins.object
# Method Overriding
# isinstace
# issubclass      
    

class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model = model_name
        self._price = max(price,0)

    def make_a_call(self,phone_num):
        print(f"Calling {phone_num} .....")

    def full_name(self):
        return (f"{self.brand} {self.model}")



class SmartPhone(Phone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        super().__init__(brand,model_name,price)        # Common way
        self.ram = ram
        self.int_mem = internal_memory
        self.rearcam = rear_camera
    
    def full_name(self):
        return (f" Price: {self._price} {self.brand} {self.model} internal memory: {self.int_mem},rear camera: {self.rearcam}")

class FlashipPhone(SmartPhone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera,front_camera):
        super().__init__(brand,model_name,price,ram,internal_memory,rear_camera)
        self.frontcam = front_camera

    def full_name(self):
        return (f" Price: {self._price} {self.brand} {self.model} internal memory: {self.int_mem},rear camera: {self.rearcam}, front camera:{self.frontcam}")

###################################################
phone1 = Phone('nokia','1100',5600)
smphone1 = SmartPhone('samsung','M30',14000,'4 GB','64 GB','8 MP')
fsphone1 = FlashipPhone('one plus','T',50000,'12 GB','128 GB','20 MP','12 MP')

print(smphone1.__dict__)
print(phone1.full_name())

print(smphone1._price)
print(smphone1.full_name())

print(fsphone1._price)
print(fsphone1.full_name())

#### MRO #########################
# check the oveeriding for method full name

## isinstance ##
# to check the object or instance belongs to given class, this returns boolean value
# syntax:   isinstance(object,class_name)
print(isinstance(smphone1,FlashipPhone))
print(isinstance(smphone1,Phone))
print(isinstance(smphone1,SmartPhone))
## issubclass ##
# to check the given child classs belongs to parent class
# syntax;   issubclass(child class,parent class)
print(issubclass(SmartPhone,Phone))
print(issubclass(SmartPhone,FlashipPhone))
print(issubclass(FlashipPhone,SmartPhone))
print(issubclass(FlashipPhone,Phone))











