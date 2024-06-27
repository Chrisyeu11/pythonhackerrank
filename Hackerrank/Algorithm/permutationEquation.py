#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#
def permutationEquation(p):
    # Create a dictionary to map values to their indices
    value_to_index = {value: index + 1 for index, value in enumerate(p)}
    
    result = []
    # Loop through each position from 1 to n
    for x in range(1, len(p) + 1):
        # Find y such that p(p(y)) = x
        y = value_to_index[value_to_index[x]]
        result.append(y)
    
    return result
