def LineAnalysis(line):
    if line == '*':
        return True     
    if line[len(line)-1] != '*' or line[0]  != '*': 
        return False
    pattern = []   
    for i in range(1, len(line)):
        if line[i] != '*':           
            pattern.append(line[i]) 
        else:
            break
    pat = ''.join(pattern)    
    S2 = line.split('*') 
    del S2[0]            
    del S2[-1]
    result = True            
    for i in range(len(S2)):
        if (S2[i] != pat):      
            result = False
            break
    return result
