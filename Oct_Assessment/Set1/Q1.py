n = 5
arr =[120,45,80,200,35,150]
T = 235

seen = {}

for i in range(n):
    complement = T - arr[i]

    if complement in seen:
        print(seen[complement], i)
        break

    seen[arr[i]] = i
