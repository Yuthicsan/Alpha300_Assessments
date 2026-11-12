n = 5
intervals = [
    [1, 3],
    [6, 9],
    [12, 15],
    [18, 20],
    [22, 25]
]
new_iv = [8, 13]

res = []
i = 0

while i < n and intervals[i][1] < new_iv[0]:
    res.append(intervals[i])
    i += 1

while i < n and intervals[i][0] <= new_iv[1]:
    if intervals[i][0] < new_iv[0]:
        new_iv[0] = intervals[i][0]
    if intervals[i][1] > new_iv[1]:
        new_iv[1] = intervals[i][1]
    i += 1
res.append(new_iv)

while i < n:
    res.append(intervals[i])
    i += 1

for start, end in res:
    print(f"{start} {end}")