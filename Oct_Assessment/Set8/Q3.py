def solve_earliest_slot():
    n = 7
    arr = [40, 50, 60, 70, 10, 20, 30]
    
    lo, hi = 0, n - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] > arr[hi]:
            lo = mid + 1
        else:
            hi = mid
            
    print(arr[lo])