n = 8
k = 3
T = 5
arr = [4, 6, 5, 3, 8, 7, 6, 4]
window_sum = 0
count = 0
for i in range(k):
    window_sum += arr[i]
if window_sum >= k * T:
    count += 1
for i in range(k, n):
    window_sum = window_sum - arr[i - k] + arr[i]
    if window_sum >= k * T:
        count += 1
print(count)