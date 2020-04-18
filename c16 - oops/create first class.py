# # Creating a class 
#   init method or also called as constructors in othet programming languages
#   attributes and instance variables
#   creating object

class Person:   ## good practice to keep the 1st letter of class in CAPS
    def __init__(self,first_name,last_name,age):
        # instance variables 
        self.fname = first_name
        self.lname = last_name
        self.age = age

# self - represents the objects
# fname,lname - stores arguements passed in first_name, last_name
# below are the objects of the class (p1,p2)

p1 = Person('amol','chavan',30)
p2 = Person('umesh','patil',34)


print(p1.fname)
print(p2.fname)







