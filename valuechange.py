val1 = input("Enter str element 1/3: ")
val2 = int(input("Enter int element 2/3: "))
val3 = float(input("Enter float element 3/3: "))

lst = [val1, val2, val3]
tpl = (val1, val2, val3)
dict = {'first element': val1, 'second element': val2, 'third element': val3}

print("\n")
print("Here is the list you created:", lst)
print("Here is the tuple you created:", tpl)
print("Here is the dictionary you created:", dict)

print("\n")
val4 = input("Add a new str list element: ")
lst.append(val4)
print("Here is the updated list:", lst)

