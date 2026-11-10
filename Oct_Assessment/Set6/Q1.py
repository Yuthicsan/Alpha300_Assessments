n = 10
arr = [78, 92, 65, 78, 100, 0, 65, 92, 78, 55]
count = [0] * 101
for mark in arr:
    count[mark] += 1
result = []
for mark in range(101):
    for j in range(count[mark]):
        result.append(mark)
print(*result)