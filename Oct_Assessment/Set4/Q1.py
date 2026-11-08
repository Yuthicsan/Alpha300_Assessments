n, k = 9 , 3
arr = [4, 2,10, 1, 3, 9, 6, 5, 7]
window_sum = 0
for i in range(k):
    window_sum += arr[i]
max_sum = window_sum
for i in range(k, n):
    window_sum = window_sum - arr[i - k] + arr[i]
    if window_sum > max_sum:
        max_sum = window_sum
print(max_sum)