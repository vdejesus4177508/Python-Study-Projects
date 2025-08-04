#using dictionaries
#dictionaries are unordered collections of key-value pairs and need brackets {}

months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June"}

print(months)
print(type(months))

print(months[1])

months[7] = "July"

print(months)

months[8] = "August"

print(months)

months[6] = 'hot month'

print(months)

monthlist = list(months)

print(monthlist)

monthlist = list(months.values())

print(monthlist)

monthlist.pop(7)

print(monthlist)
