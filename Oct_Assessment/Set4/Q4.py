s = "cbaebabacd"
p = "abc"
n = len(s)
m = len(p)
if m > n:
    print("None")
else:
    text_freq = [0] * 26
    pattern_freq = [0] * 26
    for i in range(m):
        pattern_freq[ord(p[i]) - ord('a')] += 1
        text_freq[ord(s[i]) - ord('a')] += 1
    result = []
    if text_freq == pattern_freq:
        result.append(0)
    for i in range(m, n):
        outgoing = ord(s[i - m]) - ord('a')
        incoming = ord(s[i]) - ord('a')
        text_freq[outgoing] -= 1
        text_freq[incoming] += 1
        if text_freq == pattern_freq:
            result.append(i - m + 1)
    if len(result) == 0:
        print("None")
    else:
        print(*result)