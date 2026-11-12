n = 7
prices = [3, 8, 12, 19, 25, 31, 40]
T = 44

left, right = 0, n - 1
while left < right:
    curr_sum = prices[left] + prices[right]
    if curr_sum == T:
        print(f"{left + 1} {right + 1}")
        break
    elif curr_sum < T:
        left += 1
    else:
        right -= 1