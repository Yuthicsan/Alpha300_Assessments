m = 5
n = 4
A = [3, 8, 12, 20, 25]
B = [5, 8, 20, 31]
i = 0
j = 0
result = []
while i < m and j < n:
    if A[i] < B[j]:
        result.append(A[i])
        i += 1
    elif A[i] > B[j]:
        result.append(B[j])
        j += 1
    else:
        result.append(A[i])
        i += 1
        j += 1
while i < m:
    result.append(A[i])
    i += 1
while j < n:
    result.append(B[j])
    j += 1
print(*result)