def catAndMouse(x, y, z):
    # Calculate the distances of Cat A and Cat B from the Mouse C
    distance_cat_a = abs(x - z)
    distance_cat_b = abs(y - z)

    # Determine which cat catches the mouse or if it's a tie
    if distance_cat_a < distance_cat_b:
        return "Cat A"
    elif distance_cat_b < distance_cat_a:
        return "Cat B"
    else:
        return "Mouse C"
