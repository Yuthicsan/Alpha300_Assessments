n = 9
arr = [3, 2, 3, 3, 1, 3, 2, 3, 3]
candidate = None
count = 0
for i in range(n):
    if count == 0:
        candidate = arr[i]
        count = 1
    elif arr[i] == candidate:
        count += 1
    else:
        count -= 1
print(candidate)