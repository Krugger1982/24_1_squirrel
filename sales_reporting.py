def ShopOLAP(N, items):
    S = []
    for i in range(N):
        position = items[i].split(' ')
        S.append(position)
    for i in range(len(S)):
    # summing the same items in the sales list
        for j in range(-1, -len(S)-1, -1):
            if (S[i][0] == S[j][0]) and (j != (i - len(S))):
                S[i][1] = str(int(S[i][1]) + int(S[j][1]))
                S[j][1] = '0'
    M = len(S) - 1

    k = 1
    while k > 0 :    
        k = 0       
        for i in range (len(S)-1) :
        # "The bubble" sorting
            if S[i][1] < S[i+1][1] :     
                S[i], S[i+1] = S[i+1], S[i]   
                k += 1   
            elif S[i][1] == S[i+1][1] and S[i][0] > S[i+1][0]:
                S[i], S[i+1] = S[i+1], S[i]
                k +=1
    while M > 0:
    # deleting empty elements in the sales list
        if S[M][1] == '0':
            del S[M]
        M -= 1
    for i in range(len(S)):
        S[i] = ' '.join(S[i])

    return S
