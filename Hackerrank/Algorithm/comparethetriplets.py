#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
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
