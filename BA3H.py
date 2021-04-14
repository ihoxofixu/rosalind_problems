from BA3H_functions import reconstruct_string


k = int(input())
list_of_kmers = []
tmp = input()
while tmp != '':
    list_of_kmers.append(tmp)
    tmp = input()
print(reconstruct_string(k, list_of_kmers))
