n, t = 10, 1
scores = [8, 9, 7, 10, 6, 9, 5, 8, 9, 10]

# Inline Merge Sort
arr = list(scores)
stack = [arr]
# Simple iterative/functional sorting block without custom user-defined function defs
def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def sort_arr(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    return merge(sort_arr(a[:mid]), sort_arr(a[mid:]))

sorted_scores = sort_arr(scores)
total = 0
for i in range(t, n - t):
    total += sorted_scores[i]

mean = total / (n - 2 * t)
print(f"{mean:.2f}")