def Brackets(N):
    result = []
    if N == 1:
        return ['()']
    elif N == 2:
        res = Brackets(N-1)
        for i in range (len(res)):
            result.append('()' + res[i])
            result.append(res[i] + '()')
            result.append('(' + res[i] + ')')
    else:
        res = Brackets(N-1)
        res1 = Brackets(2)
        for i in range (len(res)):
            result.append('()' + res[i])
            result.append(res[i] + '()')
            result.append('(' + res[i] + ')')        
            for i in range(len(res1)):
                result.append('(' * (N-2) + ')' * (N-2) + res1[i])
    n = []                      
    for i in result:
        if i not in n:
            n.append(i)
    return n
def BalancedParentheses(N):
    return ' '.join(Brackets(N))
