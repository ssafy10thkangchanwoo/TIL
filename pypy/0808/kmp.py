def kmp(t, p):
    N = len(t)
    M = len(p)
    lps = [0] * (M+1)

    j = 0
    lps[0] = -1
