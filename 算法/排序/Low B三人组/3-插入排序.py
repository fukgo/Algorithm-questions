"""
将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。
（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
"""
import random

'''时间复杂度:O(n平分)'''
def insert_sort(li):
    for i in range(1, len(li)):
        tmp = li[i]
        j = i-1  # j：手里的牌的下标
        while li[j] > tmp and j >= 0:
            li[j+1]=li[j]
            j-=1
            li[j+1]=tmp
        print(li)

li=[3,4,2,1,5,6,8,7,9]
insert_sort(li)
print(li)