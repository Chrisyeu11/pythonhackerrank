def hurdleRace(k, height):
    # Find the maximum height of the hurdles
    max_hurdle = max(height)
    
    # Calculate the number of doses needed
    doses_needed = max(0, max_hurdle - k)
    
    return doses_needed
