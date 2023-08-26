def max_sequence(arr:list)->list:

    total_sequence_value = 0

    for elem in arr:
        if isinstance(elem, str):
            return "Error, list has a string value"
        if elem > 0:
            total_sequence_value += elem
        elif elem < 0:
            pass

    if total_sequence_value == 0:
        return 0
    else:
        return total_sequence_value