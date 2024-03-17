"""
思路：1，分解：将列表越分越小，直至分成一个元素
     2，终止条件：一个元素是有序的
     3，合并：将两个有序列表归并，列表越来越大
"""
import random


# 归并：时间复杂度O(n)，sort排序基于归并排序
def merge(li, low, mid, high):
    i = low
    j = mid+1
    l_tmp=[]
    while i<=mid and j<=high:  # 只要两边都有数
        if li[i] < li[j]:
            l_tmp.append(li[i])
            i+=1
        else:
            l_tmp.append(li[j])
            j+=1
    # 执行完之后，两部分肯定有一部分没数了
    while i <= mid:
        l_tmp.append(li[i])
        i+=1
    while j<= high:
        l_tmp.append(li[j])
        j+=1
    li[low:high+1]=l_tmp

"""时间复杂度：O(nlogn)
   空间复杂度：O(n)
"""
def merge_sort(li, low, high):
    if low<high:  # 至少有两个
        mid = (low+high)//2
        merge_sort(li, low, mid)
        merge_sort(li, mid+1, high)
        merge(li, low, mid, high)

li=[random.randrange(1,101) for i in range(1, 11)]
print(li)
merge_sort(li,0, len(li)-1)
print(li)


