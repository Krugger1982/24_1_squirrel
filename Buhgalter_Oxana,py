def SumOfThe(N, data):
    for i in range (N):
        S = 0
        if i == 0:
            for j in range(1, N):
                S += data[j]
        else:
            for j in range(i):
                S += data[j]
            for j in range(i+1, N):
                S += data[j]
        if S == data[i]:
            return data[i]
