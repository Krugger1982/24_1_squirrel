def UFO(N, data, octal):
    if octal:
        X = 8
    else:
        X = 16
    for i in range(N):
        S = list(str(data[i]))
        Number = 0
        S.reverse()
        for j in range(len(S)):
            Number += int(S[j]) * (X**j)
        data[i] = Number
    return data
