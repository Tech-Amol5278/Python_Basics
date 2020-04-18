# Exercise - watch coco 
# ask user's name and age
# if user's name starts with ('a' or 'A') and age is above 10 then 
# print 'you can watch coco movie'
# Else print 'sorry, you cant wathc coco'

############################### Sol ####################################################################

name,age = input("Enter user's name and age, separated by comma: ").split(",")

name_lower=name.lower()
init_name=name_lower[0]
age = int(age)

if init_name=='a' and age > 10:
    print("You can watch coco movie")
else:
    print("You can't watch coco")
















