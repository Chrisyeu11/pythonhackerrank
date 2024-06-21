#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Initial height of the tree
    height = 1

    # Loop through each cycle
    for cycle in range(1, n + 1):
        if cycle % 2 == 1:  # Odd cycle (spring)
            height *= 2
        else:  # Even cycle (summer)
            height += 1

    return height
