n , T = 10 , 30
arr = [28, 35, 40, 31, 30, 12, 33, 36, 29, 41]
curr = 0
longest = 0
for i in range(n):
    if arr[i] >= T:
        curr += 1
        if curr > longest:
            longest = curr
    else:
        curr = 0
print(longest)