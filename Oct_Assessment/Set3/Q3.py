n = 9
arr = [0, 14, 0, 3, 7, 0, 0, 9, 5]
write = 0
for read in range(n):
    if arr[read] != 0:
        arr[write] , arr[read] = arr[read] , arr[write]
        write += 1
for i in range(write, n):
    arr[i] = 0
print(*arr)