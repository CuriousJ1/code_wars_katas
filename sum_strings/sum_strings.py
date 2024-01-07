def sum_strings(x: str, y: str) -> str:
    if x is None or y is None:
        raise ValueError("Inputs must not be None")

    if not isinstance(x, str) and isinstance(y, str):
        raise TypeError("Inputs must be strings")

    result = []
    carry = 0

# Make the lengths of x and y the same by adding leading zeros
    x = x.rjust(len(y), '0')
    y = y.rjust(len(x), '0')

    for i in range(len(x) - 1, -1, -1):
        digit_sum = int(x[i]) + int(y[i]) + carry
        result.append(str(digit_sum % 10))
        carry = digit_sum // 10

    if carry:
        result.append(str(carry))

    return ''.join(result[::-1])

