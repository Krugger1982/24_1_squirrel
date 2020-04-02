def odometer(A):
    S = 0
    for i in range(0, len(A), 2):
        if i == 0:
            S += A[i] * A[i+1]
        else:
            S += A[i] * (A[i+1]-A[i-1])
    return S
