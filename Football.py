def Football(F, N):
    A = sorted(F)
    temp = []
    B = []                    # Список цепочек несовпадений
    M = 0                     # Счтчик  несовпадений в очередной цепочке
    for i in range(N):
        if A[i] != F[i]:
            M += 1
            temp.append(F[i])
        elif M > 0:
            B.append(temp)
            M = 0
            temp = []
    if len(temp) > 0:
        B.append(temp)
    if len(B) == 1:                            # Если цепочка одна, то проверяем "B.reverse == B.sort" (критерий приема № 2)
        B1 = B[0][:]
        B1.reverse()
        B2 = B[0] [:]
        B2.sort()
        return B1 == B2
    elif len(B) == 2:                          # Если есть только 2 единичные цепочки то можно применить прием № 1
        return len(B[0]) == 1 and len(B[1]) == 1
    return False
