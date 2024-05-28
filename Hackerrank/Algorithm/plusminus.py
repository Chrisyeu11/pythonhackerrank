def plusMinus(arr):
    pos, neg, zer = [0]*3
    l = len(arr)
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zer += 1
    print(f"{pos/l:.6f}")
    print(f"{neg/l:.6f}")
    print(f"{zer/l:.6f}")