n = 6
arr = [5, 2, 4, 1, 3, 6]
shifts = 0
for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        shifts += 1
        j -= 1
    arr[j + 1] = key
print(*arr)
print(shifts)