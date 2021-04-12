def hamming_distance(s1, s2):
    ans = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            ans += 1
    return ans


def ApproximatePatternCount(text, pattern, dist):
    count = []
    for i in range(len(text) - len(pattern) + 1):
        pattern1 = text[i:i+len(pattern)]
        mismatches = hamming_distance(pattern1, pattern)
        if mismatches <= dist:
            count.append(i)
    return count


substr = input()
dna = input()
d = int(input())
ans = ApproximatePatternCount(dna, substr, d)
for i in ans:
    print(i, end=' ')
