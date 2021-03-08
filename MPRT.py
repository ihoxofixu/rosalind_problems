from urllib import request


def convert_from_bytes_to_str(num):
    ans = ''
    for i in num:
        ans += chr(i)
    return ans


def get_polypeptide(str):
    aResp = request.urlopen('https://www.uniprot.org/uniprot/'+str+'.fasta')
    web_pg = aResp.readlines()
    for i in range(len(web_pg)):
        web_pg[i] = convert_from_bytes_to_str(web_pg[i])
    polypeptide = ''
    for i in range(1, len(web_pg)):
        polypeptide += web_pg[i][:-1]
    return polypeptide


def N_glycosylation_motif(str):
    return str[0] == 'N' \
        and str[1] != 'P' \
        and (str[2] == 'S' or str[2] == 'T') \
        and str[3] != 'P'


s = input()
all_proteins = []
while s != '':
    all_proteins.append(s)
    s = input()
for protein in all_proteins:
    primary = get_polypeptide(protein)
    tmp = []
    for i in range(len(primary) - 3):
        if N_glycosylation_motif(primary[i:i+4]):
            tmp.append(i+1)
    if tmp:
        print(protein)
        print(*tmp)
