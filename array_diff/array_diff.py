def array_diff(a:list, b:list) ->list:

    if a is None or b is None:
        raise ValueError("Both inputs must not be None")

    if not isinstance(a, list) or not isinstance(b, list):
        raise TypeError("Both inputs must be lists")

    if not all(isinstance(item, int) for item in a) or not all(isinstance(item, int) for item in b):
        raise TypeError("Both lists must contain only integers")

    # cannot use a list data type as an object to filter.
    # x == elements in the list a
    # if the elements in list a  are not in list b, keep it in a list
    array_difference = list(filter(lambda x: x not in b, a))

    return array_difference
