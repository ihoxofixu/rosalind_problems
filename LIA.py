def fact(num):
    tmp = 1
    for i in range(1, num+1):
        tmp *= i
    return tmp


def cmn(m, n):
    return fact(m)//(fact(n)*fact(m - n))


k, n = map(int, input().split())
m = 2 ** k
ans = 1
for i in range(n):
    ans -= (0.75) ** (m - i) * (0.25) ** i * cmn(m, i)
print(ans)
