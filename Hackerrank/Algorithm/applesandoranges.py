def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_pos = [x+a for x in apples]
    oranges_pos = [x+b for x in oranges]
    apples_home = 0
    oranges_home = 0
    for i in apples_pos:
        if s <= i <= t:
            apples_home += 1
    for j in oranges_pos:
        if s <= j <= t:
             oranges_home += 1
    print(str(apples_home))
    print(str(oranges_home))
    
