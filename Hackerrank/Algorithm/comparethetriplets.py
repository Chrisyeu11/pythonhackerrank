def compareTriplets(a, b):
    # Initialize scores for both lists
    alice_score = 0
    bob_score = 0
    
    # Iterate through both lists simultaneously
    for alice_val, bob_val in zip(a, b):
        # Compare elements and update scores accordingly
        if alice_val > bob_val:
            alice_score += 1
        elif bob_val > alice_val:
            bob_score += 1

    # Return the scores as a list
    return [alice_score, bob_score]
