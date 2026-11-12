R, C = 3, 4
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
t = 16
lo, hi = 0, R * C - 1
while lo <= hi:
    mid = lo + (hi - lo) // 2
    val = matrix[mid // C][mid % C]
    if val == t:
        print(f"{mid // C} {mid % C}")
        break
    elif val < t:
        lo = mid + 1
    else:
        hi = mid - 1
else:
    print("-1 -1")