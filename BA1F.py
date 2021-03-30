def all_min(array):
    mini = min(array)
    ans = []
    for i in range(len(array)):
        if array[i] == mini:
            ans.append(i)
    return ans


dna = input()
skew = [0 for i in range(len(dna)+1)]
for i in range(1, len(dna)+1):
    skew[i] = skew[i-1]
    if dna[i-1] == 'C':
        skew[i] -= 1
    if dna[i-1] == 'G':
        skew[i] += 1
print(*all_min(skew))
