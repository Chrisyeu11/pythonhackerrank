# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

def circularArrayRotation(a, k, queries):
    # Calculate effective rotations needed (handling cases where k is greater than length of array)
    n = len(a)
    k = k % n

    # Rotate the array by slicing
    rotated_a = a[-k:] + a[:-k]

    # Collect results for each query
    results = [rotated_a[q] for q in queries]

    return results

if __name__ == '__main__':
