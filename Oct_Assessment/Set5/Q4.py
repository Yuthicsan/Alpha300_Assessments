n = 6
arr = [5, 3, 8, 6, 2, 7]
def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, count1 = merge_sort(arr[:mid])
    right, count2 = merge_sort(arr[mid:])
    i = 0
    j = 0
    merged = []
    count = count1 + count2
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            count += len(left) - i
            j += 1
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged, count
sorted_arr, inversions = merge_sort(arr)
print(inversions)