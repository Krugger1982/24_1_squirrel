def sortlist(x):
    k = 1
    L = len(x)
    while k > 0 :
        k = 0
        for i in range (L-1) :
            if x[i] > x[i+1] :
                x[i], x[i+1] = x[i+1], x[i]
                k += 1
    return x
                
def SynchronizingTables (N, ids, salary):
    ids2 = []
    # Creating copy of list "ids"
    for i in range (N):             # create a copy of the array  "ids"
        ids2.append(ids[i])         
    ids2 = sortlist(ids2)           # sorting ids2  in ascending order
    salary = sortlist(salary)       # sorting salary  in ascending order
    salary2 = []
    for i in range (N):                 
        for j in range (N):             
            if ids[i] == ids2[j]:       
                salary2.append(salary[j])    
    return salary2
