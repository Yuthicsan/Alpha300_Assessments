n = 6
arr = [3, -2, 5, 4, 1, 5]
tsum = sum(arr)
lsum = 0
ans = -1
for i in range(n):
    right_sum = tsum - lsum - arr[i]
    if lsum == right_sum:
        ans = i
        break
    lsum += arr[i]
print(ans)
