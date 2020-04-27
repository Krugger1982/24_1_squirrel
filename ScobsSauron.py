def BalancedParentheses(N):
    result = []
    if N == 1:
        return ['()']
    elif N == 2:
        res = BalancedParentheses(N-1)
        for i in range (len(res)):
            result.append('()' + res[i])
            result.append(res[i] + '()')
            result.append('(' + res[i] + ')')
    else:
        res = BalancedParentheses(N-1)
        res1 = BalancedParentheses(N-2)
        for i in range (len(res)):
            result.append('()' + res[i])
            result.append(res[i] + '()')
            result.append('(' + res[i] + ')')        
            for i in range(len(res1)):
                result.append('(' * (N-2) + ')' * (N-2) + res1[i])
    n = []                     # Удаляем одинаковые элементы
    for i in result:
        if i not in n:
            n.append(i)
    return ' '.join(n)
