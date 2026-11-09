n = 5
arr = [5, 1, 4, 2, 8]
productive_passes = 0
for i in range(n - 1):
    swapped = False
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
            swapped = True
    if swapped:
        productive_passes += 1
    else:
        break
print(*arr)
print(productive_passes)