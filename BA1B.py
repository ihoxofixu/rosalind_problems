def PatternCount(text, length):
    FreqeuntPatterns = {}
    for i in range(len(text) - length + 1):
        substr = text[i:i+length]
        if substr in FreqeuntPatterns:
            FreqeuntPatterns[substr] += 1
        else:
            FreqeuntPatterns[substr] = 1
    return FreqeuntPatterns


dna = input()
length = int(input())
d = PatternCount(dna, length)
maxi = 0
ans = []
for pattern in d:
    if d[pattern] > maxi:
        ans = [pattern]
        maxi = d[pattern]
    elif d[pattern] == maxi:
        ans.append(pattern)
print(*ans)
