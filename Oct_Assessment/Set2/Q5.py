def reverse(arr, left, right):
    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
n, k = 7, 3
arr = [1, 2, 3, 4, 5, 6, 7]
k = k % n
reverse(arr, 0, n - 1)
reverse(arr, 0, k - 1)
reverse(arr, k, n - 1)
print(*arr)