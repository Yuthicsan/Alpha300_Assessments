n = 9
arr = [102, 118, 130, 145, 160, 177, 190, 204, 230]
q = 177

lo = 0
hi = n - 1
answer = -1

while lo <= hi:
    mid = lo + (hi - lo) // 2

    if arr[mid] == q:
        answer = mid
        break
    elif arr[mid] < q:
        lo = mid + 1
    else:
        hi = mid - 1

print(answer)