
class Persons:
    obj_count = 0  ## class varialble / attribute
    def __init__(self,first_name,last_name):  ## constructor
        Persons.obj_count += 1
        self.fname = first_name
        self.lname = last_name
    
    @classmethod
    def get_instanc_count(cls):   # this belongs to Persons class
        return f"You have created {Persons.obj_count} instances in {cls.__name__} class"   ##  cls represents to Persons class
        




p1 = Persons("amol",'chavan')
p2 = Persons("akshay",'chavan')
p3 = Persons("niraj",'salokhe')
p4 = Persons("umesh",'patil')
p5 = Persons("viky",'hande')
p6 = Persons("Akshay",'k')


print(Persons.obj_count)
print(Persons.get_instanc_count())

