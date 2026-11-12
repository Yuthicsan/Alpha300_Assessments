n = 8
prices = [120, 98, 105, 90, 112, 130, 95, 118]

min_price = prices[0]
max_profit = 0

for i in range(1, n):
    if prices[i] < min_price:
        min_price = prices[i]
    else:
        profit = prices[i] - min_price
        if profit > max_profit:
            max_profit = profit

print(max_profit)