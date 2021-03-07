def common_substr_of_len(length):
    d = {}
    for i in a:
        d_tmp = {}
        for j in range(len(i) - length + 1):
            substr = i[j:j+length]
            if substr not in d_tmp:
                d_tmp[substr] = 1
        for j in d_tmp:
            if j in d:
                d[j] += 1
            else:
                d[j] = 1
    for i in d:
        if d[i] == len(a):
            return i
    return ''


s = input()
a = []
dna = ''
while s != '':
    if s[0] == '>':
        if dna != '':
            a.append(dna)
            dna = ''
    else:
        dna += s
    s = input()
a.append(dna)
left = 0
right = len(min(a)) + 1
while left != right - 1:
    mid = (left + right) // 2
    if common_substr_of_len(mid) != '':
        left = mid
    else:
        right = mid
print(f(left))
