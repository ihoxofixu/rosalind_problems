ans = ''
tmp = input()
ans += tmp[:-1]
while tmp != '':
    ans += tmp[-1]
    tmp = input()
print(ans)
