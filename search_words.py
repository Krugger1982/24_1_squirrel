def WordSearch (Len, s, subs):
    S2 = s.split(' ')
    Text = []
    k = 0
    i = 0
    string = []
    while i < len(S2):                  
        if len(S2[i]) > Len:
            slovo = list(S2[i]) 
            sl = []
            for j in range(Len):
                sl.append(slovo[0])           
                del slovo[0]                  
            S2[i] = ''.join(slovo)
            S2.insert(i, ''.join(sl))
            string.append(S2[i])
            Text.append(string)
            string = []
            i += 1
        elif (k + len(string) + len(S2[i])) > Len:
            Text.append(string)
            string = []
            k = 0
        else:
            string.append(S2[i])
            k += len(S2[i])
            i += 1
    Text.append(string)
    Ansver = []
    for i in range(len(Text)):
        if subs in Text[i]:
            Ansver.append(1)
        else:
            Ansver.append(0)
    return Ansver    
