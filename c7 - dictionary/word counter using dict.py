string = "Amol Subodh Chavan"

print(string.count('a'))

def wordcount_dict(s):
    wc = {}

    for i in s:
        wc[i.lower()] = s.lower().count(i.lower())

    return wc 

print(wordcount_dict(string))


