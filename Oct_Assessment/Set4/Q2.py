n = 8
k = 2
arr = [7, 12, 5, 7, 12, 9, 12, 4]
seen = set()
answer = "NO"
for i in range(n):
    if arr[i] in seen:
        answer = "YES"
        break
    seen.add(arr[i])
    if i >= k:
        seen.remove(arr[i - k])
print(answer)