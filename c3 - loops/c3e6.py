# modify number guessing game 
# ask user to enter a number until he wins

#### Sol #############################################
import random  # package to generate random no.

## random no ##
for x in range(1):
  winning_no = random.randint(1,100)
#######################

i = 1
attempt = 0
while True:
    attempt += i
    num = input("Guess a number between 1 to 100: ")

    if int(num) < winning_no:
        print("too low")
    elif int(num) > winning_no:
        print("too high")
    else:
        print(f"You win, you guessed correct number in {attempt} attempts")
        break

