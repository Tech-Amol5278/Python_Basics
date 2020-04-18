# Class variables ;
#   accessed through out the class unlike methods
#   it can minimize the code


# for example, to find the circumference of circle, we will create one class
# formula for circumferece = 2*pie*r (Pie = 3.14... which is constant)


class circle:
    pi = 3.14    # this is class variable which will be shared will all the methods in the class
    def __init__(self,radius):
        self.r = radius

    def calc_circum(self):
        return 2*circle.pi*self.r  ## accessing the class variable   class.variable


circle1 = circle(2)
print(circle1.calc_circum())






