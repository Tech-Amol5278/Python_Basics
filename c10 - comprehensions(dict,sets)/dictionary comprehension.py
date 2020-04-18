# dictionary comprehension
# square = {1:1, 2:4,3:9}

sq_list = {i:i**2 for i in range(1,11)}
print(sq_list)

# ammendment
sq_list = { f"Square of {i} is":i**2 for i in range(1,11)}
print(sq_list)

for k,v in sq_list.items():
    print(f"{k} : {v}")


## wordcount using normal method
name = "Amol Subodh Chavan"

wc_dict = {}
# normal method 
for i in name.lower():
    wc_dict[i] = name.lower().count(i)

print(wc_dict)

## wordcount using dict comprehension

wc_dict2 = {i:name.lower().count(i) for i in name.lower() }
print(wc_dict2)
