n = 8
arr = [-1, 0, 1, 2, -1, -4, 3, -2]

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def sort_arr(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    return merge(sort_arr(a[:mid]), sort_arr(a[mid:]))

nums = sort_arr(arr)
found = False

for i in range(n - 2):
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    if nums[i] > 0:
        break
        
    left, right = i + 1, n - 1
    while left < right:
        total = nums[i] + nums[left] + nums[right]
        if total == 0:
            print(f"{nums[i]} {nums[left]} {nums[right]}")
            found = True
            left += 1
            right -= 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
        elif total < 0:
            left += 1
        else:
            right -= 1

if not found:
    print("None")