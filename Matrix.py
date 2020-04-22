def  MatrixTurn(Matrix, M, N, T):
    A = []
    for i in range(len(Matrix)):
        A.append(list(Matrix[i]))
    perimetr = []
    temp = []
    while len(A) > 2 and len (A[0]) > 2:       # Разбираем матрицу на "периметры"
        for i in range(len(A[0])):
            temp.append(A[0][i])
        del A[0]
        for i in range(len(A)-1):
            temp.append(A[i][len(A[i])-1])
            del A[i][len(A[i])-1]
        for i in range(-1, -len(A[len(A)-1])-1, -1):
            temp.append(A[len(A)-1][i])
        del A[len(A)-1]
        for i in range(-1, -len(A)-1, -1):
            temp.append(A[i][0])
            del A[i][0]
        perimetr.append(temp)
        temp = []
    if N <= M:                                    # Последний периметр, состоящий из 2-х строк
        for i in range(len(A[0])):
            temp.append(A[0][i])
        del A[0]
        for i in range(-1, -len(A[0])-1, -1):
            temp.append(A[0][i])
        del A[0]
    else:
        temp.append(A[0][0])
        for i in range(len(A)):
            temp.append(A[i][1])
            del A[i][1]
        for i in range(-1, -len(A), -1):
            temp.append(A[-1][0])
            del A[i]
        del A[0]
    perimetr.append(temp)
    perimetr.reverse()
    for i in range(len(perimetr)):            #Проворачиваем каждую линию "периметра"
        for j in range(T):
            perimetr[i].insert(0, perimetr[i].pop())
    A = []                  # Сборка повернутой матрицы производится в обратном порядке - от внутрених слоев к внешним
    if N <= M:                                                  # Для горизнтальной или квадратной матрицы
        R = M - N
        A.append([]) 
        A.append([])
        for j in range(len(perimetr)):
            if j == 0:                                          # заполняем внутренний периметр (только 2 строки)
                z = len(perimetr[0])
                for i in range(len(perimetr[0])):
                    if i < z//2:
                        A[0].append(perimetr[0][i])
                    else:
                        A[1].insert(0, perimetr[0][i])
            else:                                              # Заполняем следующие периметры
                A.insert(0, [])
                A.append([])
                for i in range(len(perimetr[j])):              # Верхняя строка
                    if i < R + 2 * j + 2:
                        A[0].append(perimetr[j][i])
                    elif i < R + 4 * j + 2:                    # Правый столбец
                        A[i - (R + 2 * j + 2 - 1)].append(perimetr[j][i])
                    elif i < (2 * R + 6 * j + 4):
                        A[len(A)-1].insert(0, perimetr[j][i])  # нижняя строка
                    else:
                        A[-(i - (2 * R + 6 * j + 4) + 2)].insert(0, perimetr[j][i])   # Левый столбец  
    else:                                                       # Для матрицы, вытянутой ветикально
        R = N - M
        for i in range (len(perimetr[0])//2):
            A.append([])
        for j in range(len(perimetr)):
            if j == 0:                                          # заполняем внутренний периметр (только 2 строки)
                for i in range(len(perimetr[0])):
                    if i == 0:
                        A[0].append(perimetr[j][0])
                    elif i < (len(perimetr[0])//2+1):
                        A[i-1].append(perimetr[0][i])
                    else:
                        A[-(i - 2 * R - 1)].insert(0, perimetr[0][i]) 
            else:
                A.insert(0, [])
                A.append([])
                for i in range(len(perimetr[j])):                             # Верхняя строка
                    if i < 2 * j + 2:
                        A[0].append(perimetr[j][i])
                    elif i < R + 4 * j + 2:                                   # Правый столбец
                        A[i - ( 2 * j + 2 - 1)].append(perimetr[j][i])
                    elif i < (R + 6 * j + 4):
                        A[len(A)-1].insert(0, perimetr[j][i])                 # нижняя строка
                    else:
                        A[-(i - (R + 6 * j + 2))].insert(0, perimetr[j][i])   # Левый столбец                  
    for i in range(len(A)):
        A[i] = ''.join(A[i])
    return A
