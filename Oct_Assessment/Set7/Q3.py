n = 10
arr = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]

lo = 0
hi = n - 1
answer = -1

while lo <= hi:
    mid = lo + (hi - lo) // 2

    if arr[mid] == 1:
        answer = mid + 1
        hi = mid - 1
    else:
        lo = mid + 1

print(answer)