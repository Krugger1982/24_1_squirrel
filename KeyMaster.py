def Keymaker(k):
    A = []
    for i in range(k):
        A.append(True)    
    for i in range (2, k+1):   # шаги
        for j in range(k):     # позиция двери
            if (j+1) % i == 0:
                A[j] = not A[j]
    for i in range(k):
        if A[i]:
            A[i] = '1'
        else:
            A[i] = '0'
    return ''.join(A)
