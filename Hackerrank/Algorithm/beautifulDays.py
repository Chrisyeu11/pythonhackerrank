def beautifulDays(i, j, k):
    def reverse_number(n):
        return int(str(n)[::-1])
    
    beautiful_days_count = 0
    
    for day in range(i, j + 1):
        reversed_day = reverse_number(day)
        if abs(day - reversed_day) % k == 0:
            beautiful_days_count += 1
            
    return beautiful_days_count
