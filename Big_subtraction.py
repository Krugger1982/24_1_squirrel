def BigMinus(s1,s2):
    S1 = list(s1)
    S2 = list(s2)
    bol = [0]
    men = [0]
    if len (S1) > len (S2):
        bol = S1
        men = S2
    elif len (S2) > len (S1):
        bol = S2
        men = S1
    else:
        for i in range(len(S1)):
            if S1[i] > S2[i]:
                bol = S1
                men = S2
                break
            elif S1[i] < S2[i]:
                bol = S2
                men = S1
                break
    if bol == [0]:
        return '0'
    res = []
    for i in range(-1, -len(men)-1, -1):
        if int(bol[i]) >= int(men[i]):
            x = int(bol[i]) - int(men[i])
        else:
            x = int(bol[i]) + 10 - int(men[i])
            bol[i-1] = (int(bol[i-1]) + 9) % 10
        res.insert(0, str(x))
    for i in range(len(bol) - len(men)):
        res.insert(i, str(bol[i]))
    i = 0
    while len(res) > 0:
        if str(res[i]) == '0':
            del res[i]
        else:
            break        
    return ''.join(res)
