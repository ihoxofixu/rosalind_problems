d = {'A' : 'T', 'C' : 'G', 'G' : 'C', 'T' : 'A'}
dna1 = input()
dna2 =  ''.join([d[dna1[i]] for i in range(-1, -len(dna1)-1, -1)])
print(dna2)
