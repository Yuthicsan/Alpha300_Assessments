n = 10
arr = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4]
k = 0
for i in range(n):
    if k < 2 or arr[i] != arr[k - 2]:
        arr[k] = arr[i]
        k += 1
print(k)
for i in range(k):
    print(arr[i], end=" ")
print()