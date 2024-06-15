def circularArrayRotation(a, k, queries):
    # Calculate effective rotations needed (handling cases where k is greater than length of array)
    n = len(a)
    k = k % n

    # Rotate the array by slicing
    rotated_a = a[-k:] + a[:-k]

    # Collect results for each query
    results = [rotated_a[q] for q in queries]

    return results
