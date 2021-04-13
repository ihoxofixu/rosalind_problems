def splitter(string, length):
    ans = []
    for i in range(len(string) - length + 1):
        ans.append(string[i:i+length])
    return ans


n = int(input())
dna = input()
composition = splitter(dna, n)
composition.sort()
for i in composition:
    print(i)
