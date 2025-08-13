#arbitrary number of arguments. *args and kwargs

def foo(a, b, *args, **kwargs):
    """
    Function that takes two mandatory arguments, an arbitrary number of positional arguments,
    and an arbitrary number of keyword arguments.

    Args:
        a: First mandatory argument.
        b: Second mandatory argument.
        *args: Additional positional arguments.
        **kwargs: Additional keyword arguments.

    Returns:
        A tuple containing the mandatory arguments, the list of additional positional arguments,
        and the dictionary of additional keyword arguments.
    """
    print("Here is 'a'", a)
    print("Here is 'b'", b)
    print("Here are the '*args'", *args)
    return a, b, args, kwargs

print(foo('spam', 'eggs', 'arb1', 'arb2', 'arb3'))

