### continued from c2e3  #######
name  = "      amol       "
dots  = "................."

# Strip removes the blank spaces from string
## lstrip method
print("using strips method")
print(name)
print(name + dots)
print(name.lstrip() + dots)
print(name.lstrip().rstrip() + dots)
print(name.strip() + dots)


## replace method
print("using replace method")
print(name.replace(" ","") + dots)




