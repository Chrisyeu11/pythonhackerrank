def viralAdvertising(n):
    # Initial number of people who receive the advertisement
    shared = 5
    cumulative_likes = 0

    for day in range(1, n + 1):
        # Calculate the number of likes on the current day
        liked = shared // 2
        # Update the cumulative likes
        cumulative_likes += liked
        # Calculate the number of people who will receive the advertisement the next day
        shared = liked * 3

    return cumulative_likes
