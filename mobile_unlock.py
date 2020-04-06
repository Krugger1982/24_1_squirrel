def PatternUnlock(N, hits):
    small = [(1, 2), (1, 6), (1, 9), (2, 1), (2, 3), (2, 8), (2, 5), (3, 2), (3, 4), (3, 7), (4, 3), (4, 5), (5, 2), (5, 4), (5, 6), 
             (6, 1), (6, 5), (7, 3), (7, 8), (8, 2), (8, 7), (8, 9), (9, 1), (9, 8)]
    big = [(1, 8), (1, 5), (2, 4), (2, 6), (2, 7), (2, 9), (3, 5), (3, 8), (4, 2), (5, 1), (5, 3), (6, 2), (7, 2), (8, 1), (8, 3), (9, 2)]
    result = 0
    for i in range(N-1):
        step = (hits[i], hits[i+1])
        if step in small:
            result += 1
        else:
            result += 1.4142135623730950488016887242097 
    result = list (str(int(round(result, 5) * 100000)))                      
    for i in range (len(result)-1, -1, -1):
        if result[i] == '0':
            del result[i]
    S = ''.join(result)
    return S
