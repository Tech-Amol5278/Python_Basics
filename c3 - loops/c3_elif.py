# if elif else statement
# show ticket pricing
# 0 to 3 (free)
# 4 to 10 (150)
# 11 to 60 (250)
# above 60 (200)

################################################################################################

age = input("Enter user's age: ")
age = int(age)

if age <= 3:
    print("ticket free")
elif age >= 4 and age <= 10:
    print("ticket is 150")
elif age >= 11 and age <= 60:
    print("ticket is 250")
else:
    print("ticket is 200")


