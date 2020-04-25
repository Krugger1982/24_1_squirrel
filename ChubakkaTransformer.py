def Transform(A, N):
    B = []
    for i in range(N):
        for j in range(N - i - 1):
            k = i + j
            B.append(max(A[j:k+1]))
    return B

def TransformTransform(A, N):
    B = Transform(A, N)
    C = Transform(B, len(B))
    return sum(C) % 2 == 0
