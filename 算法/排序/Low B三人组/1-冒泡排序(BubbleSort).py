"""
列表每两个相邻的数，如果前面的比后面的大，则交换这两个数。
一趟排序完成后，则无序区减少一个数，有序区增加一个数。
"""
import random
def Bubble_Sort(li):
    for i in range(len(li)-1):
        #exchange=False
        for j in range(len(li)-i-1):
            if li[j]>li[j+1]:
                li[j], li[j+1]=li[j+1], li[j]
                #exchange=True


        #if not exchange:
            #break
        print(li)

li = [random.randint(0, 100) for i in range(10)]
Bubble_Sort(li)


