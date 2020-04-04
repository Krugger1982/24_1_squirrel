def ConquestCampaign (N, M, L, batalion):
    Round = []                                    # create a matrix N x M
    for i in range (N):
        B = []
        for j in range (M):
            B.append(0)
        Round.append(B)
    D = 1                                        # Day 1 - landing
    for i in range (len(batalion)):
        if i % 2 == 0:
            Round[batalion[i]-1][batalion[i+1]-1] = D
    if M*N == 1:
        return 1
    C = 0
    for i in range (N):                   # Checking the availability of free territories
            for j in range (M):
                if Round[i][j] == 0:
                    C +=1    
    while C != 0:
        D += 1                                    #  Next day - the occupation of territory
        for i in range (1, N-1, 1):              #  Capture of internal cells
            for j in range (1, M-1, 1):
                if Round[i][j] == D-1:
                    Round[i-1][j] = D
                    Round[i+1][j] = D
                    Round[i][j-1] = D
                    Round[i][j+1] = D
        for i in range (1, N-1, 1):              #  Capture cells along the horizontal border
            if Round[i][0] == D-1 and M > 1:
                Round[i-1][0] = D
                Round[i+1][0] = D
                Round[i][1] = D
            elif Round[i][0] == D-1:
                Round[i-1][0] = D
                Round[i+1][0] = D
            if Round[i][M-1] == D-1 and M > 1:
                Round[i-1][M-1] = D
                Round[i+1][M-1] = D
                Round[i][M-2] = D
            elif Round[i][M-1] == D-1:
                Round[i-1][M-1] = D
                Round[i+1][M-1] = D               
        for j in range (1, M-1, 1):          #  Capture cells along the vertical border 
            if Round[0][j] == D-1 and N > 1:
                Round[0][j-1] = D
                Round[0][j+1] = D
                Round[1][j] = D
            elif Round[0][j] == D-1:
                Round[0][j-1] = D
                Round[0][j+1] = D                
            if Round[N-1][j] == D-1 and N > 1:
                Round[N-1][j+1] = D
                Round[N-1][j-1] = D
                Round[N-2][j] = D
            elif Round[N-1][j] == D-1:
                Round[N-1][j+1] = D
                Round[N-1][j-1] = D
            if Round[0][0] == D-1 and N > 1 and M > 1:             # upper left corner
                Round[0][1] = D              
                Round[1][0] = D              
            elif Round[0][0] == D-1 and N > 1:
                Round[1][0] = D              
            elif Round[0][0] == D-1 and M > 1:
                Round[0][1] = D             
            if Round[N-1][0] == D-1 and N > 1 and M > 1:             # upper right corner
                Round[N-1][1] = D           
                Round[N-2][0] = D            
            elif Round[N-1][0] == D-1 and N > 1:
                Round[N-2][0] = D           
            elif Round[N-1][0] == D-1 and M > 1:
                Round[N-1][1] = D           
            if Round[0][M-1] == D-1 and N > 1 and M > 1:             # lower left corner
                Round[0][M-2] = D             
                Round[1][M-1] = D             
            elif Round[0][M-1] == D-1 and N > 1:
                Round[1][M-1] = D            
            elif Round[0][M-1] == D-1 and M > 1:
                Round[0][M-2] = D             
            if Round[N-1][M-1] == D-1 and N > 1 and M > 1:             # lower right corner
                Round[N-2][M-1] = D            
                Round[N-1][M-2] = D             
            elif Round[N-1][M-1] == D-1 and N > 1:
                Round[N-2][M-1] = D            
            elif Round[N-1][M-1] == D-1 and M > 1:
                Round[N-1][M-2] = D           
        C = 0        
        for i in range (N):                   # Checking the availability of free territories
            for j in range (M):
                if Round[i][j] == 0:
                    C +=1    
    return D
