def climbingLeaderboard(ranked, player):
    # Remove duplicates and sort the ranked list in descending order if not already
    unique_ranks = sorted(list(set(ranked)), reverse=True)
    
    # Prepare to collect player ranks
    player_ranks = []
    
    # Use binary search to find where each player's score fits into the ranked scores
    for score in player:
        low, high = 0, len(unique_ranks)
        while low < high:
            mid = (low + high) // 2
            if unique_ranks[mid] > score:
                low = mid + 1
            else:
                high = mid
        # The rank is the index + 1, since rank is 1-based index
        player_ranks.append(low + 1)
    
    return player_ranks
