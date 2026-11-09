n = 7
k = 3
arr = [29, 14, 36, 7, 21, 14, 50]
for i in range(k):
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    temp = arr[i]
    arr[i] = arr[min_index]
    arr[min_index] = temp
print(*arr[:k])