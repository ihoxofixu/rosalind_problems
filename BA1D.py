def PatternCount(text, pattern):
    count = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            count.append(i)
    return count


substr = input()
dna = input()
print(*PatternCount(dna, substr))
