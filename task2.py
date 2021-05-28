"""As second task: you have the list of symbols (example: a, b, c, c, a (it’s very primitive)).
You should write function that returns the first repeating element from this list (in our example it’s “c”)."""

list_to_check = ['a', 'd', 'b', 'c', 'd', 'a', 'd']


def first_repeating(list_of_symbols):
    """
    Function to find first repeating of elements in list
    :param list_of_symbols: list with symbols
    :return: first repeating element if there is any
    """
    seen = []
    for symbol in list_of_symbols:
        if symbol in seen:
            return f'First repeating element is {symbol}'
        else:
            seen.append(symbol)
    return 'There are no repeating elements in this list'


print(first_repeating(list_to_check))
