import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Frequency dictionary to count the occurrence of each number
    frequency = {}
    
    # Populate the frequency dictionary
    for number in a:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    
    # Initialize the maximum length variable
    max_length = 0

    # Check the combined length of each number and its consecutive number
    for number in frequency:
        # Current number count
        current_count = frequency[number]
        # Consecutive number count
        consecutive_count = frequency.get(number + 1, 0)
        
        # Update the maximum length
        max_length = max(max_length, current_count + consecutive_count)
    
    return max_length


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
