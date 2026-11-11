n = 10
arr = [5, 7, 7, 8, 8, 8, 8, 10, 12, 12]
x = 8
first = -1
lo, hi = 0, n - 1
while lo <= hi:
    mid = lo + (hi - lo) // 2
    if arr[mid] == x:
        first = mid
        hi = mid - 1 
    elif arr[mid] < x:
        lo = mid + 1
    else:
        hi = mid - 1
last = -1
lo, hi = 0, n - 1
while lo <= hi:
    mid = lo + (hi - lo) // 2
    if arr[mid] == x:
        last = mid
        lo = mid + 1
    elif arr[mid] < x:
        lo = mid + 1
    else:
        hi = mid - 1
        
print(f"{first} {last}")