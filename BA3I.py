from BA3I_functions import reconstruct_string


k = int(input())
kmers = []
for i in range(2**k):
    tmp = bin(i)[2:]
    if len(tmp) < k:
        tmp = '0' * (k - len(tmp)) + tmp
    kmers.append(tmp)
st = reconstruct_string(kmers)
st = st[:len(st)-k+1]
print(st)
