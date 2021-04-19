from string_reconstruction_pairs import reconstruct_string


k, d = map(int, input().split())
list_of_kmers = []
tmp = input()
while tmp != '':
    kmer1, kmer2 = tmp.split('|')
    list_of_kmers.append((kmer1, kmer2))
    tmp = input()
print(reconstruct_string(k, d, list_of_kmers))
