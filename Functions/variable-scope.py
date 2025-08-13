#variable scope-global and local variables

def demo(f_in):
    """
    Demonstrates variable scope in Python.
    The function takes an input and modifies a global variable.
    """
    global somevar # shared with main code
    demo.tom = 16 # An attribute accessible from main code
    somevar += 1
    another = 12
    res = f_in+14 # Value passed in (f_in)
    return res

somevar = 27 # accessed in function via global
another = 17 # not accessed in function
#pval = 16 # accessed in function via parameter

#print demo(pval)

print demo.tom #function attribute
print somevar
print another