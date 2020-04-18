# expetion handeling
# below example which is made only to accept integer values

while True:   ## Loop to accept input til true comes
        try:
            age  = int(input("Enter a number: "))
            break
        except ValueError:   # valueerror : optional only if we know the error which can come
            print("Please enter age only in integer ")
        except:             # when error is unpredictable
            print("Unexpected error")



if age > 18:
    print("Welcome to play game")
else:
    print("You cant play this game")
