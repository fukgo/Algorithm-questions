def match(l1,l2):
    """
    :param l1:
    :param l2:目标列表
    :return:
    """
    if sorted(l1)!=sorted(l2):
        return False

    map_index = {}
    switch_num = 0
    for j, val in enumerate(l2):
        map_index[val]=j
    #print(map_index)
    for i in range(0,len(l1)):
        if l1[i]!=l2[i]:
            ind = map_index[l1[i]]
            l1[i],l1[ind] = l1[ind],l1[i]
            switch_num += 1
    return l1==l2 and switch_num % 2 ==0


a = ['a','c','b','d']
b = ['a','b','c','d']
print(match(a,b))

def chan(l1,l2):
    d = {}
    for i,j in zip(l1,l2):
        if not d and i != j:
            i=j
            d[j]=i

