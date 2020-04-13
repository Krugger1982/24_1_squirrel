def PrintingCosts(Line):
    cod = []
    Cost = [0, ' ']
    cod.append(Cost)
    Cost = [3, '`', "'"]
    cod.append(Cost)
    Cost = [4, '.']
    cod.append(Cost)
    Cost = [6, '"']
    cod.append(Cost)
    Cost = [7, ',', '-', '^']
    cod.append(Cost)
    Cost = [8, ':', '_']
    cod.append(Cost)
    Cost = [9, '!', '~']
    cod.append(Cost)
    c = '\ '
    c = list(c)
    Cost = [10, '>', '<', '/', c[0]]
    cod.append(Cost)
    Cost = [11, ';']
    cod.append(Cost)
    Cost = [12, '|', '(', ')']
    cod.append(Cost)
    Cost = [13, 'v', 'r', 'x', '+']
    cod.append(Cost)
    Cost = [14, 'Y', '=']
    cod.append(Cost)
    Cost = [15, '?', 'i']
    cod.append(Cost)
    Cost = [16, 'L', 'T', 'l', '7']
    cod.append(Cost)
    Cost = [17, 't', 'c', 'u', '*']
    cod.append(Cost)
    Cost = [18, 'J', 'n', ']', '{', '[', '}', 'X', 'f', 'I']
    cod.append(Cost)
    Cost = [19, 'V', 'z', 'w', '1']
    cod.append(Cost)
    Cost = [20, 'o', 'F', 'j', 'C']
    cod.append(Cost)
    Cost = [21, 'h', 'K', 'k', '4', 's']
    cod.append(Cost)
    Cost = [22, '2', '0', 'Z', '%', 'm']
    cod.append(Cost)
    Cost = [23, '8', 'P', '3', 'e', 'U', 'a']
    cod.append(Cost)
    Cost = [24, '&', '#', 'A', 'y']
    cod.append(Cost)
    Cost = [25, 'b', 'd', 'p', 'G', 'S', 'q', 'H', 'N']
    cod.append(Cost)
    Cost = [26, 'D', '9', 'E', 'W', '6', 'O']
    cod.append(Cost)
    Cost = [27, '5']
    cod.append(Cost)
    Cost = [28, 'M', 'R']
    cod.append(Cost)
    Cost = [29, '$', 'B']
    cod.append(Cost)
    Cost = [30, 'g']
    cod.append(Cost)
    Cost = [31, 'Q']
    cod.append(Cost)
    Cost = [32, '@']
    cod.append(Cost)
    S = 0    
    for i in range(len(Line)):
        N = 0
        for j in range(len(cod)):
            if Line[i] in cod[j]:
                N = cod[j][0]
        if N == 0 and Line[i] != ' ':
            N = 23
        S += N
    return S
