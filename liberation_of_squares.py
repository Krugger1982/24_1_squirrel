def occupation (a, x):
    if x == 0:
        x = a
    return x

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
    C = 0
    for i in range (N):                   # Checking the availability of free territories
            for j in range (M):
                if Round[i][j] == 0:
                    C +=1    
    while C != 0:
        D += 1                                    #  Next day - the occupation of territory
        if N > 2 and M > 2:
            for i in range (1, N-1, 1):               #  Capture of internal cells
                for j in range (1, M-1, 1):
                    if Round[i][j] == D-1:
                        Round[i-1][j] = occupation (D, Round[i-1][j])
                        Round[i+1][j] = occupation (D, Round[i+1][j])
                        Round[i][j-1] = occupation (D, Round[i][j-1])
                        Round[i][j+1] = occupation (D, Round[i][j+1])
        for i in range (1, N-1, 1):              #  Capture cells along the horizontal border
            if Round[i][0] == D-1 and M > 1:
                Round[i-1][0] = occupation (D, Round[i-1][0])
                Round[i+1][0] = occupation (D, Round[i+1][0])
                Round[i][1] = occupation (D, Round[i][1])
            elif Round[i][0] == D-1:
                Round[i-1][0] = occupation (D, Round[i-1][0])
                Round[i+1][0] = occupation (D, Round[i+1][0])
            if Round[i][M-1] == D-1 and M > 1:
                Round[i-1][M-1] = occupation (D, Round[i-1][M-1])
                Round[i+1][M-1] = occupation (D, Round[i+1][M-1])
                Round[i][M-2] = occupation (D, Round[i][M-2])
            elif Round[i][M-1] == D-1:
                Round[i-1][M-1] = occupation (D, Round[i-1][M-1])
                Round[i+1][M-1] = occupation (D, Round[i+1][M-1])               
        for j in range (1, M-1, 1):          #  Capture cells along the vertical border 
            if Round[0][j] == D-1 and N > 1:
                Round[0][j-1] = occupation (D, Round[0][j-1])
                Round[0][j+1] = occupation (D, Round[0][j+1])
                Round[1][j] = occupation (D, Round[1][j])
            elif Round[0][j] == D-1:
                Round[0][j-1] = occupation (D, Round[0][j-1])
                Round[0][j+1] = occupation (D, Round[0][j+1])               
            if Round[N-1][j] == D-1 and N > 1:
                Round[N-1][j+1] = occupation (D, Round[N-1][j+1])
                Round[N-1][j-1] = occupation (D, Round[N-1][j-1])
                Round[N-2][j] = occupation (D, Round[N-2][j])
            elif Round[N-1][j] == D-1:
                Round[N-1][j+1] = occupation (D, Round[N-1][j+1])
                Round[N-1][j-1] = occupation (D, Round[N-1][j-1])
            if Round[0][0] == D-1 and N > 1 and M > 1:             # upper left corner
                Round[0][1] = occupation (D, Round[0][1])              
                Round[1][0] = occupation (D, Round[1][0])              
            elif Round[0][0] == D-1 and N > 1:
                Round[1][0] = occupation (D, Round[1][0])              
            elif Round[0][0] == D-1 and M > 1:
                Round[0][1] = occupation (D, Round[0][1])             
            if Round[N-1][0] == D-1 and N > 1 and M > 1:             # upper right corner
                Round[N-1][1] = occupation (D, Round[N-1][1])           
                Round[N-2][0] = occupation (D, Round[N-2][0])            
            elif Round[N-1][0] == D-1 and N > 1:
                Round[N-2][0] = occupation (D, Round[N-2][0])           
            elif Round[N-1][0] == D-1 and M > 1:
                Round [N-1][1] = occupation (D, Round [N-1][1])           
            if Round[0][M-1] == D-1 and N > 1 and M > 1:             # lower left corner
                Round[0][M-2] = occupation (D, Round[0][M-2])             
                Round[1][M-1] = occupation (D, Round[1][M-1])            
            elif Round[0][M-1] == D-1 and N > 1:
                Round[1][M-1] = occupation (D, Round[1][M-1])
            elif Round[0][M-1] == D-1 and M > 1:
                Round[0][M-2] = occupation (D, Round[0][M-2])            
            if Round[N-1][M-1] == D-1 and N > 1 and M > 1:             # lower right corner
                Round[N-2][M-1] = occupation (D, Round[N-2][M-1])           
                Round[N-1][M-2] = occupation (D, Round[N-1][M-2])             
            elif Round[N-1][M-1] == D-1 and N > 1:
                Round[N-2][M-1] = occupation (D, Round[N-2][M-1])           
            elif Round[N-1][M-1] == D-1 and M > 1:
                Round[N-1][M-2] = occupation (D, Round[N-1][M-2])        
        C = 0        
        for i in range (N):                   # Checking the availability of free territories
            for j in range (M):
                if Round[i][j] == 0:
                    C +=1    
    return D
