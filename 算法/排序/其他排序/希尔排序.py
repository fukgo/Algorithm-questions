"""
① 先取一个小于n的整数d1作为第一个增量，把文件的全部记录分成d1个组。
② 所有距离为d1的倍数的记录放在同一个组中，在各组内进行直接插入排序。
③ 取第二个增量d2小于d1重复上述的分组和排序，直至所取的增量dt=1(dt小于dt-l小于…小于d2小于d1)，即所有记录放在同一组中进行直接插入排序为止。
"""
def insert_sort(li, gap):
    for i in range(gap, len(li)):
        tmp=li[i]
        j = i-gap  # j指的是手中牌的下标
        while j>= 0 and li[j] > tmp:
            li[j+gap] = li[j]
            j -= gap
        li[j+gap] = tmp

def sheel_sort(li):
    d = len(li)//2
    insert_sort(li, d)
    d //= 2


