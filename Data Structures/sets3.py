#example from video 9 in cbtnuggets course


"""
global name - variables in a function are local names
and variables outside of a function are global names
"""


S = [x**2 for x in range(10)]
#print(S)

def choice_a(x):
    print(S)
    return
def choice_b(x):
    V = [2**i for i in range(x)]
    print(V)
    return

def choice_c(y):
    M = [x for x in range(y) if x % 2 == 0]
    print(M)

def choice_d():
    raise SystemExit


# This code demonstrates the use of sets in Python.
print("Which operation do you want to perform?\n")
print("""
a: x to the second power
b: 2 to the xth power
c: mod 2
d: quit program
""")

resp = input("Choice: ")
resp2 = int(input("Upper limit? "))

if resp == 'a':
    choice_a(resp2)
elif resp == 'b':
    choice_b(resp2)
elif resp == 'c':
    choice_c(resp2)
else:
    choice_d()


