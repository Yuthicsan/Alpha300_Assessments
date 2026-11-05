n = 7
arr = [12, 35, 8, 35, 20, 12, 5]
max = 0
smax = 0
for i in range(n):
    current = arr[i]
    if current > max:
        smax = max
        max = current
    elif current != max:
        if current > smax:
            smax = current
if smax == 0:
    print("None")
else:
    print(smax)
