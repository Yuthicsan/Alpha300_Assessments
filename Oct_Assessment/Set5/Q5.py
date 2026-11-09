n = 9
k = 3
arr = [40, 25, 60, 25, 90, 75, 60, 30, 50]
target = n - k
def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i
low = 0
high = n - 1
while low <= high:
    pivot_index = partition(arr, low, high)

    if pivot_index == target:
        print(arr[pivot_index])
        break
    elif pivot_index < target:
        low = pivot_index + 1
    else:
        high = pivot_index - 1