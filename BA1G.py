def hamming_distance(s1, s2):
    ans = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            ans += 1
    return ans


print(hamming_distance(input(), input()))
