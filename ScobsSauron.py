def gen_breckets(N, prefix='', A = []):
    if N == 0:
        A.append(prefix)
    else:
        gen_breckets(N-1, prefix + '(')
        gen_breckets(N-1, prefix + ')')
    return A

def BalancedParentheses(N):
    M = 2*N
    A = gen_breckets(M)
    B = []
    for i in range(len(A)):
        Ability = True
        Count1 = 0
        Count0 = 0
        for j in range(len(A[i])):
            if A[i][j] == '(':
                Count1 += 1
            else:
                Count0 += 1
            if Count0 > Count1:
                Ability = False
        if Ability and A[i][0] == '(' and A[i][-1] == ')' and Count1 == Count0 and len(A[i]) == 2*N and A[i] not in B:
            B.append(A[i])
    return ' '.join(B)
