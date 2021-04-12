# there is one more variation of this function that works in a bit other way
# first of all find all the patterns hamming_distanced for 1 symbol
# then for every this pattern do the same and so on d times
# but it is O(k^d) when tha function below works for O((k-d)*4^d)
# so we choose a bit faster algorithm
def Variety(substr, mistakes):
    # this function creates all the k-mers with at most 'mistakes' mismatches
    # so that we can understand where this k-mer can come from
    if mistakes != 0:
        var = set([])
        for i in range(len(substr) - mistakes + 1):
            for j in set(['A', 'T', 'G', 'C']):
                # by taking a nucletide from all possible we work out
                # situations when there are less mismatches than 'mistakes'
                varsub = substr[:i] + j + substr[i+1:]
                tmp_var = Variety(varsub[i+1:], mistakes - 1)
                for s in tmp_var:
                    var |= set([varsub[:i+1] + s])
        return var
    else:
        return set([substr])


def ApproximatePatternCount(text, length, dist):
    # using Variety function we can find the most frequent pattern
    # the most interesting is that this pattern can be absent in this string
    FreqeuntApproximatePatterns = {}
    for i in range(len(text) - length + 1):
        substr = text[i:i+length]
        patterns = Variety(substr, dist)
        for pattern in patterns:
            if pattern in FreqeuntApproximatePatterns:
                FreqeuntApproximatePatterns[pattern] += 1
            else:
                FreqeuntApproximatePatterns[pattern] = 1
    return FreqeuntApproximatePatterns


dna = input()
length, d = map(int, input().split())
approximate_pattern_matches = ApproximatePatternCount(dna, length, d)
maxi = 0
ans = []
for pattern in approximate_pattern_matches:
    if approximate_pattern_matches[pattern] > maxi:
        ans = [pattern]
        maxi = approximate_pattern_matches[pattern]
    elif approximate_pattern_matches[pattern] == maxi:
        ans.append(pattern)
for i in ans:
    print(i, end=' ')
