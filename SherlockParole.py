def  SherlockValidString(s):
    pattern = []
    S = list(s)
    N = 0
    while len(S) > 0:
        temp = S[0]
        pattern.append(S.count(temp))
        while temp in S:
            S.remove(temp)
    average = int(sum(pattern)/len(pattern))
    for i in range (len(pattern)):
        if pattern[i] - average == 1 or pattern[i] - average == 0:
            N += pattern[i] - average
        else:
            return False
    return N < 2
