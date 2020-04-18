# take two comma separated inputs from user 
# 1. username 
# 2. a single character

# output -2 print lines
# 1. user's name length
# 2. count the character that user inputed (bonus: cases insensitive count)

#### Sol #################################################

name,search_char = input("Enter your name and search character in comma separated: ").split(",")

name=name.lower()
search_char=search_char.lower()

print(len(name))
print(name.count(search_char))

### sol using strip method #########
print("using strip method")

name = name.strip()
search_char=search_char.strip()

print(len(name))
print(name.count(search_char))
