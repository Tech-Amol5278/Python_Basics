# Create any class and make the instances 
# Return the no. of instances.


class Persons:
    obj_count = 0
    def __init__(self,first_name,last_name):
        Persons.obj_count += 1
        self.fname = first_name
        self.lname = last_name

p1 = Persons("amol",'chavan')
p2 = Persons("akshay",'chavan')
p3 = Persons("niraj",'salokhe')
p4 = Persons("umesh",'patil')
p5 = Persons("viky",'hande')
p6 = Persons("Akshay",'k')


print(Persons.obj_count)

