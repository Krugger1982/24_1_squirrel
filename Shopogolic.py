def MaximumDiscount( N, price):
    Copy = sorted(price, reverse=True)
    discont = 0
    collection = []
    set_ = []
    for i in range (N):
        if (i + 1) % 3 != 0:
            set_.append(Copy[i])
        else:
            set_.append(Copy[i])
            collection.append(set_)
            set_ = []
    for i in range (len(collection)):
        if len (collection[i]) > 2:
            discont += collection[i][2]
    return discont
