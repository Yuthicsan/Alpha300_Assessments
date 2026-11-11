n = 9
arr = [2, 5, 9, 14, 20, 17, 11, 6, 1]
h = 11
lo, hi = 0, n - 1
peak = 0
while lo <= hi:
    mid = lo + (hi - lo) // 2
    left_val = arr[mid - 1] if mid > 0 else -float('inf')
    right_val = arr[mid + 1] if mid < n - 1 else -float('inf')
    
    if arr[mid] > left_val and arr[mid] > right_val:
        peak = mid
        break
    elif mid > 0 and arr[mid] < arr[mid - 1]:
        hi = mid - 1
    else:
        lo = mid + 1
def binary_search_asc(l, r):
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] == h:
            return m
        elif arr[m] < h:
            l = m + 1
        else:
            r = m - 1
    return -1
def binary_search_desc(l, r):
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] == h:
            return m
        elif arr[m] < h:
            r = m - 1
        else:
            l = m + 1
    return -1
ans = binary_search_asc(0, peak)
if ans == -1:
    ans = binary_search_desc(peak + 1, n - 1)
    
print(ans)