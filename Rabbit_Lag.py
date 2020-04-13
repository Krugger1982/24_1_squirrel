def TheRabbitsFoot(s, encode):
    if encode:
        S = list(s)
        i = 0
        while i < len(S):
            if S[i] == ' ':
                del S[i]
            else:
                i += 1
        N = int(len(S) ** 0.5)
        M = N + 1
        if M * N < len(S):
            N += 1
        matrix = []
        for i in range(N):
            str_ = []
            for j in range(M):
                if (M*i+j) < len(S):
                    str_.append(S[M*i+j])
                else:
                    str_.append(-1)
            matrix.append(str_)
    
        matrix_T = []                                
        # Creating a transposed matrix  
        for i in range(M):
            str_ = []
            for j in range(N):
                if matrix[j][i] != -1:
                    str_.append(matrix[j][i])
            matrix_T.append(str_) 
        res = []
        for i in range(len(matrix_T)):
            s1 = ''.join(matrix_T[i])
            res.append(s1)
        result1 = ' '.join(res)
        return result1
    else:
        S = list(s)
        matrix = []
        str_ = []
        for i in range(len(S)):
            if S[i] != ' ':
                str_.append(S[i])
            else:
                matrix.append(str_)
                str_ = []
        matrix.append(str_)
        N = len(matrix)
        M = len(matrix[0])  
        # Obviously, the first "word" is the longest one
        for i in range(N):
        # Fill in the empty spaces with the number -1
            while len(matrix[i]) < M:
                matrix[i].append(-1)
        matrix_T = []                                
        # Creating a transposed matrix  
        for i in range(M):
            str_ = []
            for j in range(N):
                if matrix[j][i] != -1:
                    str_.append(matrix[j][i])
            matrix_T.append(str_) 
        res = []
        for i in range(len(matrix_T)):
            s1 = ''.join(matrix_T[i])
            res.append(s1)
        result1 = ''.join(res)
        return result1
