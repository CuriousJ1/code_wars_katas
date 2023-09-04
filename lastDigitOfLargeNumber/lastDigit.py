def last_digit(n1, n2):

    if n1 is None or n2 is None:
        raise ValueError("Both inputs must not be None")

    if not isinstance(n1, int) or not isinstance(n2, int) or isinstance(n1, bool) or isinstance(n2, bool):
        raise TypeError("Both inputs must be integers")

    if n1 < 0 or n2 < 0:
        raise ValueError("Inputs must be non-negative integers")

    result = n1 ** n2

    last_digit = result % 10

    return last_digit
