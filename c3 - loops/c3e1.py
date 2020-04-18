# Exercise, nuumber guessing game
# make a variable like winning number and assign a number to it
# ask user to guess a number
# if user guessed correctly then print "You Win !!!!"
# if user didnot guess correctly then:
#     if user guessed lower than actual number then print "too low"
#     if user guessed higher than actual number then print "too high"
# google "how to generate random number in python"
# winning number

#################### Sol #######################################################
import random  # package to generate random no.

## random no ##
for x in range(1):
  winning_no = random.randint(1,100)
#######################

usr_no = input("Enter a random no. between 1 to 100: ")
usr_no = int(usr_no)

if usr_no < winning_no:
    print("too low")
else :
    pass

if usr_no > winning_no:
    print("too high")
else :
    pass

if usr_no == winning_no:
    print("You Win !!!!")
else :
    pass













