n = 8
arr = [15, 18, 22, 31, 3, 6, 9, 12]
t = 9

lo, hi = 0, n - 1
ans = -1

while lo <= hi:
    mid = lo + (hi - lo) // 2
    if arr[mid] == t:
        ans = mid
        break
        
    if arr[lo] <= arr[mid]:
        if arr[lo] <= t < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    else:
        if arr[mid] < t <= arr[hi]:
            lo = mid + 1
        else:
            hi = mid - 1

print(ans)