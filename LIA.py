def merge(d1, d2):
    for i in d2:
        if i in d1:
            d1[i] += d2[i]
        else:
            d1[i] = d2[i]
    return d1


def mate(str, amount=1):
    d = {}
    al1 = str[:2]
    al2 = str[2:]
    for i in al1:
        for j in al2:
            for ii in 'Aa':
                for jj in 'Bb':
                    A = min(i, ii)
                    a = max(i, ii)
                    B = min(j, jj)
                    b = max(j, jj)
                    tmp = A + a + B + b
                    if tmp in d:
                        d[tmp] += amount
                    else:
                        d[tmp] = amount
    return d


dd = mate('AaBb')
k = int(input())
for i in range(k-1):
    d_tmp = {}
    for i in dd:
        merge(d_tmp, mate(i, dd[i]))
    dd = d_tmp
print(dd)
