s = "Was it a car or a cat I saw?"
left = 0
right = len(s) - 1
is_palindrome = True
while left < right:
    if not s[left].isalnum():
        left += 1
    elif not s[right].isalnum():
        right -= 1
    else:
        if s[left].lower() != s[right].lower():
            is_palindrome = False
            break
        left += 1
        right -= 1
if is_palindrome:
    print("YES")
else:
    print("NO")