def BiggerGreater(input):
    S = list(input)
    if len(S) < 2 or S == sorted(S, reverse=True):
        return ''
    while ''.join(S) <= input:
        for i in range(- 1, -len(S), -1):
            S[i], S[i-1] = S[i-1], S[i]
            if S[i] < S[i-1] and ''.join(S) > input:
                break
            elif S[i] < S[i-1]:
                continue              
    return ''.join(S)
