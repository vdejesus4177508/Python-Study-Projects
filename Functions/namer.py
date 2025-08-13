#another exercise using functions from cbtnuggets course


def namer(fn, ln='Warner'):
    # return value, default value
    #r = print('Your name is', fn, ln)
    #return r ## Since `print` returns None, r will be None.
    return f'Your name is {fn} {ln}'


result = namer(fn, ln='Warner'):  # Output: Your name is John Warner
# This function takes a first name and an optional last name (default is 'Warner'

print(result)  # Output: None, since print returns None`

