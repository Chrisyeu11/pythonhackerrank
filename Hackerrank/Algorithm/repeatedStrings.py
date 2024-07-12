#https://www.hackerrank.com/challenges/repeated-string/problem?isFullScreen=true
def repeatedString(s, n):
    # Find the number of 'a's in the original string s
    count_a_in_s = s.count('a')
    
    # Calculate how many times the entire string s repeats in the first n characters
    full_repeats = n // len(s)
    
    # Calculate the remaining characters after the full repeats
    remainder = n % len(s)
    
    # Total count of 'a's in the fully repeated portion
    total_a = full_repeats * count_a_in_s
    
    # Add the count of 'a's in the remaining portion of the string
    total_a += s[:remainder].count('a')
    
    return total_a
