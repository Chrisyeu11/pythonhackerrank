#https://www.hackerrank.com/challenges/queens-attack-2/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign
#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Convert the list of obstacles to a set of tuples for O(1) lookups
    obstacles_set = {(r, c) for r, c in obstacles}
    
    # Define the 8 possible directions the queen can move
    directions = [
        (-1,  0), # Up
        ( 1,  0), # Down
        ( 0, -1), # Left
        ( 0,  1), # Right
        (-1, -1), # Up-Left
        (-1,  1), # Up-Right
        ( 1, -1), # Down-Left
        ( 1,  1)  # Down-Right
    ]
    
    # Initialize the count of attackable squares
    attackable_squares = 0
    
    # Check each direction
    for dr, dc in directions:
        nr, nc = r_q + dr, c_q + dc
        while 1 <= nr <= n and 1 <= nc <= n:
            if (nr, nc) in obstacles_set:
                break
            attackable_squares += 1
            nr += dr
            nc += dc
    
    return attackable_squares

