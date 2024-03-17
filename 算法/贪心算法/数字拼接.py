"""
有n个非负整数，将其按照字符串拼接的方式拼接为一个整数。
如何拼接可以使得得到的整数最大?
例:32,94,128,1286,6,71可以拼接除的最大整数为94716321286128
"""
#from functools import reduce
l=[32,94,128,1286,6,71]
print(list(map(str, l)))
def num_join(li):
    li=list(map(str, li))
    #print(li)
    for i in range(len(li)-1):
        for j in range(i, len(li)-1):
            if int(li[j] + li[j + 1]) < int(li[j + 1] + li[j]):
                li[j], li[j+1] = li[j+1], li[j]
    print(''.join(li))
num_join(l)


