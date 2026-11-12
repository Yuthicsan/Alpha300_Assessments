n = 7
arr = [-9, -4, -2, 0, 3, 5, 8]

res = [0] * n
left, right = 0, n - 1
pos = n - 1

while left <= right:
    left_sq = arr[left] * arr[left]
    right_sq = arr[right] * arr[right]
    if left_sq > right_sq:
        res[pos] = left_sq
        left += 1
    else:
        res[pos] = right_sq
        right -= 1
    pos -= 1

print(" ".join(str(x) for x in res))