n = 8
arr = [1, 2, 3, 1, 4, 5, 2, 3]
seen = set()
left = 0
max_length = 0
for right in range(n):
    while arr[right] in seen:
        seen.remove(arr[left])
        left += 1
    seen.add(arr[right])
    current_length = right - left + 1
    if current_length > max_length:
        max_length = current_length
print(max_length)