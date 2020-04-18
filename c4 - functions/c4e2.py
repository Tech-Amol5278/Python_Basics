# palidrome function - which checks for given string if it matches reverse of the same string returns true

# palindrome - words those can be read same, forwards and backwards

name ='Amol'
# # print(name[len(name)-1])
# for i in range(len(name)-1,-1,-1):
#     print(name[i])
#     i -= 1


#### Sol 1 ##########################################

def is_palindrome(word):
    rev_word = ''
    for i in range(len(word)-1,-1,-1):
        rev_word += word[i]
        i -= 1
    
    print(rev_word)
    if word == rev_word: 
        return True
    
    return False

##### Sol 2 ######################################
def is_palindrome_1(word):
    rev_word = word[::-1]

    if word == rev_word:
        return True
    return False


strg = input("Enter a word to check for palindrome: ")
print(len(strg))
print(is_palindrome(strg))
print(is_palindrome_1(strg))
