# create a funtion divide which returns answer
    # handle : zero divide error
    #          only ints allowed



# ZeroDivisionError:
# print(devide(4,0))


def division(a,b):
    try:
        return (a/b)
    except ZeroDivisionError as err:  ## as err: to get the default msg 
        print(err)
    except TypeError:
        print("Please input ints only")
    except:
        print("Unexpected error")


print(division(4,2))
