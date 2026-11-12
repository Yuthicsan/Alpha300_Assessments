n, D = 7, 3
weights = [4, 2, 7, 1, 8, 3, 5]
lo = 0
hi = 0
for w in weights:
    if w > lo:
        lo = w
    hi += w
ans = hi
while lo <= hi:
    mid = lo + (hi - lo) // 2
    days_needed = 1
    current_load = 0
    for w in weights:
        if current_load + w > mid:
            days_needed += 1
            current_load = w
        else:
            current_load += w
    if days_needed <= D:
        ans = mid
        hi = mid - 1
    else:
        lo = mid + 1
print(ans)