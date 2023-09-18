def pig_latin(text:str)->str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    text = text.split()

    pigged_words = []

    for word in text:
        # Check if the word consists of alphabetic characters
        if word.isalpha():
            # Move the first letter to the end and add "ay"
            pigged_word = word[1:] + word[0] + "ay"
        else:
            # If the word contains non-alphabetic characters (punctuation), leave it unchanged
            pigged_word = word

        # Append the modified word to the list
        pigged_words.append(pigged_word)

        # Join the modified words back into a single string
    pig_latin_text = " ".join(pigged_words)

    return pig_latin_text