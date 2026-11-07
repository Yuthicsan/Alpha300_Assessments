s = "Campus Library"
arr = list(s)
vowels = "aeiouAEIOU"
left = 0
right = len(arr) - 1
while left < right:
    while left < right and arr[left] not in vowels:
        left += 1
    while left < right and arr[right] not in vowels:
        right -= 1
    if left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
print("".join(arr))