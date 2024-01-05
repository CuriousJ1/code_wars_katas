def cakes(recipe: dict, available: dict) -> int:
    if recipe is None or available is None:
        raise ValueError("Inputs must not be None")

    if not isinstance(recipe, dict):
        raise TypeError("Recipe is not a dictionary")

    if not isinstance(available, dict):
        raise TypeError("Available is not a dictionary")

    ratios = []

    # Iterate through each ingredient in the recipe
    for ingredient in recipe:
        # If the ingredient is not present in the available ingredients, set its ratio to 0
        available_amount = available.get(ingredient, 0)

        # Calculate the ratio of available amount to required amount for the current ingredient
        # as the ingredient will be the key
        ratio = available_amount // recipe[ingredient]

        # Append the ratio to the list
        ratios.append(ratio)

    # Return the minimum ratio, as that will be the limiting factor for the number of cakes
    return min(ratios, default=0)