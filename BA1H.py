def hamming_distance(s1, s2):
    ans = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            ans += 1
    return ans


def PatternCount(text, pattern, dist):
    count = []
    for i in range(len(text) - len(pattern) + 1):
        if hamming_distance(text[i:i+len(pattern)], pattern) <= dist:
            count.append(i)
    return count


substr = input()
dna = input()
d = int(input())
print(*PatternCount(dna, substr, d))
