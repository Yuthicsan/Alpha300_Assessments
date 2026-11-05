
n = 8
arr = [4021, 3377, 5120, 3377, 4021, 9001, 5120, 7122]

seen = set()

answer = -1

for i in range(n):
    if arr[i] in seen:
        answer = arr[i]
        break

    seen.add(arr[i])

print(answer)
