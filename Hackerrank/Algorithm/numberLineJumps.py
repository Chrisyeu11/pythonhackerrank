
def kangaroo(x1, v1, x2, v2):
    # x1 + n*v1 = x2 + n*v2
    # n = (x2 - x1) / (v1 - v2)
    if v1 > v2 and (x2 - x1) % (v1 - v2) == 0:
        return 'YES'
    else:
        return 'NO'
