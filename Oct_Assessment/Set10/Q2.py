n = 6
prices = [10, 20, 30, 40, 50, 60]
q = 35

floor_val = None
lo, hi = 0, n - 1
while lo <= hi:
    mid = lo + (hi - lo) // 2
    if prices[mid] <= q:
        floor_val = prices[mid]
        lo = mid + 1
    else:
        hi = mid - 1

ceil_val = None
lo, hi = 0, n - 1
while lo <= hi:
    mid = lo + (hi - lo) // 2
    if prices[mid] >= q:
        ceil_val = prices[mid]
        hi = mid - 1
    else:
        lo = mid + 1

print(f"{floor_val} {ceil_val}")