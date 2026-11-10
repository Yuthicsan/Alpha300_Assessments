n = 9
arr = [4, 4, 6, 2, 2, 2, 6, 9, 6]
freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
unique = list(freq.keys())
def merge_sort(items):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        a = left[i]
        b = right[j]
        if freq[a] < freq[b] or (freq[a] == freq[b] and a > b):
            result.append(a)
            i += 1
        else:
            result.append(b)
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
ordered = merge_sort(unique)
result = []
for num in ordered:
    for j in range(freq[num]):
        result.append(num)
print(*result)