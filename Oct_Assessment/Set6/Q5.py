n = 10
arr = [3, 1, 3, 2, 3, 1, 2, 3, 1, 3]
stack = [(0, n - 1)]
while stack:
    low, high = stack.pop()
    if low >= high:
        continue
    pivot = arr[(low + high) // 2]
    lt = low
    i = low
    gt = high
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    if low < lt - 1:
        stack.append((low, lt - 1))
    if gt + 1 < high:
        stack.append((gt + 1, high))
print(*arr)