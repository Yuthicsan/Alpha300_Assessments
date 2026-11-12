n = 6
intervals = [
    [8, 10],
    [1, 3],
    [2, 6],
    [15, 18],
    [17, 20],
    [6, 7]
]

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0] or (left[i][0] == right[j][0] and left[i][1] <= right[j][1]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def sort_intervals(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(sort_intervals(arr[:mid]), sort_intervals(arr[mid:]))

sorted_iv = sort_intervals(intervals)
result = [sorted_iv[0]]

for i in range(1, n):
    curr_start, curr_end = sorted_iv[i]
    last_start, last_end = result[-1]
    
    if curr_start <= last_end:
        if curr_end > last_end:
            result[-1][1] = curr_end
    else:
        result.append([curr_start, curr_end])

for start, end in result:
    print(f"{start} {end}")