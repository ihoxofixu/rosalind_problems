def PatternCount(text, length):
    FreqeuntPatterns = {}
    for i in range(len(text) - length + 1):
        substr = text[i:i+length]
        if substr in FreqeuntPatterns:
            FreqeuntPatterns[substr] += 1
        else:
            FreqeuntPatterns[substr] = 1
    return FreqeuntPatterns


def Clumps(text, L, t, k):
    ans = set([])
    for i in range(len(text) - L + 1):
        tmp = PatternCount(text[i:i+L], k)
        for i in tmp:
            if tmp[i] >= t:
                ans |= set([i])
    return ans


dna = input()
k, L, t =  map(int, input().split())
print(*Clumps(dna, L, t, k))
