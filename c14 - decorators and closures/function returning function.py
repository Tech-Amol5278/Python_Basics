# Function returning function, also called as closure and first class function





def outer_func():
    def inner_func():
        print("inside inner func")
    return inner_func # not executing inner func
    # return inner_func() # to execute inner func  ()

var = outer_func()  ## we are not executing function here
# to execuet the function, use below or place () after theh inner_func while defining the function
var()

##### 
def outer_func2(msg):
    def inner_func2():
        print(f"message is {msg}")
    return inner_func2


var = outer_func2("Hi there")
var()





