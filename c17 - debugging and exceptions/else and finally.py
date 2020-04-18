# Else and fianlly


while True:   ## Loop to accept input til true comes
    try:
        age  = int(input("Enter a number: "))
    except ValueError:   # valueerror : optional only if we know the error which can come
        print("Please enter age only in integer ")
    except:             # when error is unpredictable
        print("Unexpected error")
    else:       # executes when there is no exception
        print(f"You entered {age}")
        break
    finally:    # this executes in both the cases, errors and no errors
        print("finally blocks......")

        



if age > 18:
    print("Welcome to play game")
else:
    print("You cant play this game")
