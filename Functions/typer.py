# no return value

def typer(x):
    """
    This function takes an integer x and returns a string indicating whether x is even or odd.
    If x is even, it returns 'even', otherwise it returns 'odd'.
    """
    if type(x) == int:
        print('This is an integer.')
    elif type(x) == str:
        print('This is a string.')
    else:
       print('This is not an integer or string.')

typer('hello')
