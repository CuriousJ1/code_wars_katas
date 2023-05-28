import math

def is_square(n):

    if n >= 0:
        if math.sqrt(n).is_integer():  # you need to call the .is_integer method

            print(f"{n} is a square number")
            return True

        else:
            print(f"{n} is not a square number")
            return False

    else:
        print("Negative numbers cannot be square numbers")
        return False

is_square(5)
