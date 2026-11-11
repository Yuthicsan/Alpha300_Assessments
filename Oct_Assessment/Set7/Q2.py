n = 6
arr = [10, 20, 30, 45, 60, 80]
t = 50

lo = 0
hi = n - 1
answer = n

while lo <= hi:
    mid = lo + (hi - lo) // 2

    if arr[mid] >= t:
        answer = mid
        hi = mid - 1
    else:
        lo = mid + 1

print(answer)