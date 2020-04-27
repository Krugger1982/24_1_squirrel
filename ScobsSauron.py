def BalancedParentheses(N):
    result = []
    if N == 1:
        return ['()']
    else:
        res = BalancedParentheses(N-1)
        for i in range (len(res)):
            result.append('()' + res[i])
            result.append(res[i] + '()')
            result.append('(' + res[i] + ')')
            n = []                     # Удаляем одинаковые элементы
            for i in result:
                if i not in n:
                    n.append(i)
    return n
