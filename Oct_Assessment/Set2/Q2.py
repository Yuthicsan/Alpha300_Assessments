n = 10
arr = [17, 23, 17, 8, 23, 42, 8, 5, 42, 17]
freq = {}
for i in range(n):
    if arr[i] in freq:
        freq[arr[i]] += 1
    else:
        freq[arr[i]] = 1
ans = -1
for i in range(n):
    if freq[arr[i]] == 1:
        ans = arr[i]
        break
print(ans)