position = [['', 1]]
N = 0

def add(arg, string):
    return string + arg        

def delete(arg, string):
    if arg < len(string):
        string = string[0:len(string)-arg]
    else:
        string = ''
    return string
        
def ind(arg, string):
    if arg < len(string):
        return string[arg]
    else:
        return ''
    
def BastShoe(command):
    global position
    global N
    S = []  
    S.append(int(command[0]))         
    S.append(command[2:])
    if S[0] == 1 and N < len(position)-1:
        del position[:N]  # обнуляем цепочку перед этой командой (больше назад не откатишь)
        del position[1:]  # и цепочку после этой команды (вперед тоже не откатишь, начали новую ветку)
        N = 0             # В массиве остался единственный элемент - предыдущее состояние        
        position.append([add(S[1], position[N][0]), S[0]])
        N += 1
    elif S[0] == 1:
        position.append([add(S[1], position[N][0]), S[0]])
        N += 1        
    elif S[0] == 2 and S[1].isdigit() and N < len(position)-1:
        line = delete(N, int(S[1]), position[N][0])
        position.append([line, S[0]])
        del position[:N]  # обнуляем цепочку перед этой командой (больше назад не откатишь)
        del position[1:]  # и цепочку после этой команды (вперед тоже не откатишь, начали новую ветку)
        N = 1             # В массиве остался единственный элемент - предыдущее состояние        
    elif S[0] == 2 and S[1].isdigit():
        line = delete(N, int(S[1]), position[N][0])
        position.append([line, S[0]])
        N += 1
    elif S[0] == 3 and S[1].isdigit():
        line = ind(int(S[1]), position[N][0])
        return line
    elif S[0] == 4 and S[1] == '' and (position[N][1] == 1 or position[N][1] == 2) and (N > 0):
        N -= 1
    elif S[0] == 5 and S[1] == '' and N < (len(position)-1):
        N += 1
    return position[N][0]
