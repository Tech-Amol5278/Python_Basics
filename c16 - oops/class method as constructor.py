# class method as constructor 
# we can define our own constructor..



class Persons:
    obj_count = 0
    def __init__(self,first_name,last_name):
        Persons.obj_count += 1
        self.fname = first_name
        self.lname = last_name

    @classmethod
    def person_construct(cls,string):
        fname,lname = string.split(',')
        return cls(fname,lname)




p1 = Persons("amol",'chavan')
p2 = Persons("akshay",'chavan')
p3 = Persons("niraj",'salokhe')
p4 = Persons("umesh",'patil')
p5 = Persons("viky",'hande')
p6 = Persons("Akshay",'k')
p7 = Persons.person_construct('rakesh, tanwar')   ## Owsn constructor  >> person_construct

print(Persons.obj_count)
