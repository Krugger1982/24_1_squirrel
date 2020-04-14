def MassVote(N, Votes):
    Copy = sorted(Votes, reverse=True)
    winner = Copy[0]
    if N != 1 and Copy[1] == winner:
        return 'no winner'
    S = 0
    for i in range(N):
        S += Votes[i]
        if Votes[i] == winner:
            K = i+1
    if S == 0:
        return 'no winner'
    if winner / S > 0.5:
        res1 = 'majority '
    else:
        res1 = 'minority '
    return res1 + 'winner ' + str(K)
