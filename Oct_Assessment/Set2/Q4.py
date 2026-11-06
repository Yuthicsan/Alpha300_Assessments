n, q = 8, 4
sales = [5, 3, 8, 2, 7, 1, 9, 4]
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + sales[i]
for i in range(q):
    l, r = 0,2
    answer = prefix[r + 1] - prefix[l]
    print(answer)