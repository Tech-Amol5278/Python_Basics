# Default Parameters
# Can only be declared in the last

def user_info(f_name,l_name,age=23):  ## default age is 23
    print(f"First name is {f_name}")
    print(f"Last name is {l_name}")
    print(f"and your Age is {age}")
    return

print(user_info("Amol","Chavan"))
