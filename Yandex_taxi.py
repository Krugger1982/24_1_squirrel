def Unmanned(L, N, track):
    S = 0
    t = 0    
    for j in range(N): 
        flag = False      
        track[j].append(flag)
    while S < L:          
        Step = True     
        for j in range(N): 
            track[j][3] = not ((t % (track[j][1] + track[j][2])) < track[j][1])   
            if S == track[j][0]:        
                Step = Step and track[j][3]
        if Step:
            S += 1  
        t += 1
    return t
