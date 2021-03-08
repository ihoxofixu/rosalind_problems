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


print(get_polypeptide(input()))
