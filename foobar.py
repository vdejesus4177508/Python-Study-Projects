foo = ['spam', 335, 'eggs', 323.234]
print(foo)

foo2 = foo[0:3]
print(foo2)

foo2.remove(335)

print(foo2)

footup = tuple(foo2)

kind = type(footup)

print(kind)

foo2.append('test')

print(foo2)

tup = ('spam', 335, 'eggs', 323.234)

foo2.append('jam')
print(foo2)
footup = tuple(foo2)
print(footup)

print(footup.count(foo2))










