def duplicate_count(text:str) ->int:

    if text is None is None:
        raise ValueError("Inputs must not be None")

    if not isinstance(text, str):
        raise TypeError("Inputs must be lists")

    if not all(isinstance(item, str) for item in text):
        raise TypeError("Both lists must contain only integers")

    text = text.lower()
    seen = set()
    duplicate_counter = 0

    for letter in text:
        if letter in seen:
            continue  # Skip this letter if it's already been counted as a duplicate
        elif text.count(letter) > 1:
            duplicate_counter += 1
            seen.add(letter)

    return duplicate_counter
