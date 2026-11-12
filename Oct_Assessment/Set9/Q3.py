m, n = 6, 6
A = [9, 4, 9, 5, 12, 4]
B = [12, 9, 9, 8, 4, 12]

set_a = set()
for x in A:
    set_a.add(x)

seen_common = set()
common_list = []
for y in B:
    if y in set_a and y not in seen_common:
        seen_common.add(y)
        common_list.append(y)

if not common_list:
    print("None")
else:
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

    sorted_common = sort_arr(common_list)
    print(" ".join(str(x) for x in sorted_common))