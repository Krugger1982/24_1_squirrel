def squirrel (n):
    n = int (n)
    x = 1    
    for i in range (1, n+1):
        x *= i
    while x // 10 != 0:
        x //= 10
    return x
