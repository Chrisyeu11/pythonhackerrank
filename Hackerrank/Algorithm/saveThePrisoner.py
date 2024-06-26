def saveThePrisoner(n, m, s):
    # Calculate the position of the last sweet
    result = (s + m - 1) % n
    
    # If the result is 0, it means the last sweet is given to the last prisoner
    if result == 0:
        return n
    else:
        return result
