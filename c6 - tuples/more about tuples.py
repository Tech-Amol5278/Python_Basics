# looping in tuples 
# tuple with one element
# tuple without parenthesis
# tuple unpacking
# list inside tuple 
# Functions can be used with tuples

mixed = (1,2,3,4.0)

# for loop and  tuple 
for i in mixed:
    print(i)


# tuple with one element
# below are not tuples, those are integers and strings
nums = (1) 
words = ('word1')

print(type(nums))
print(type(words))

# to create a tuple with only one element, must have comma after the element. Please refer below
nums = (1,) 
words = ('word1',)

print(type(nums))
print(type(words))

# tuple without parenthesis, see below
guitars = "yamaha","baton rouge","taylor"
print(type(guitars))

# tuple unpacking, see below
guitarists = ('Maneli Jamal','Eddie Van Der Meer','Andrew Foy')
guitarist1,guitarist2,guitarist3 = guitarists
print(guitarist1)

# list inside tuple, we can operate on the lists using same functions which was covered in Lists.
favourites =  ("Southern Mongolia",["Tokyo Ghoul Theme","Landscape"])
favourites[1].pop
favourites[1].append("We made it")
print(favourites)

# More functions (Min,Max,Sum)

print(min(mixed))
print(max(mixed))
print(sum(mixed))


