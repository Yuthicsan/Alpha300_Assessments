n = 8
arr = [4, 3, 2, 7, 8, 2, 3, 1]

for i in range(n):
    val = abs(arr[i])
    i = val - 1
    if arr[i] > 0:
        arr[i] = -arr[i]
found = False
for i in range(n):
    if arr[i] > 0:
        if found:
            print(" ")
        print(i + 1)
        found = True
if not found:
    print("None")
else:
    print()
