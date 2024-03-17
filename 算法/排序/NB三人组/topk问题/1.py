"""
取列表前k个元素建立一个小根堆，堆顶就是目前第k大的数
依次向后遍历原列表，对于列表中的元素1，如果小于堆顶，则忽略该元素；
如果大于堆顶，则将该元素更换为该元素，并且堆堆进行一次调整
遍历列表所有元素后，倒序弹出列表

"""
"""
比较排序
"""
"""时间复杂度nlogn"""
import random


def sift(li, low, high):
    """
    :param li:列表
    :param low:堆的根节点位置(堆顶位置)
    :param high:堆的最后一个元素的位置
    """
    i = low    # i,最开始指向根节点
    j= 2 * i + 1  # j,最开始指根下面一层左孩子
    tmp = li[low]
    while j <= high:  # 只要j位置有数就一直循环
        #  (j+1) <= high 保证存在右孩子
        if (j+1) <= high and li[j+1] < li[j]:  # 如果右孩子比左孩子大
            j=j+1  # 指向右孩子
        if li[j] < tmp:
            li[i]=li[j]
            i=j  # j 往下移，变成j层
            j=2*i+1  # j变成i下面一层
        else:  # tmp更大,把tmp放在i的位置上
            li[i]=tmp
            break
    else:  # 当下面没有数后：把tmp放回原来叶子节点上
        li[i]=tmp

def topK(li,k):
    heap = li[0:k]
    for i in range((k-2)//2, -1, -1):
        sift(heap, i, k-1)

    # 建堆：
    for i in range(k,len(li)-1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k-1)
    # 遍历：
    for i in range(k-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, k-1)
    return heap

def heap_sort(li):
    # 先建堆，找最后一个叶子节点 (n-1-1)//2
    n = len(li)
    #  循环每一个小堆
    for i in range((n-2)//2, -1, -1):  # 从最后一个叶子节点到li[0],步长为-1
        sift(li, i, n-1)  # high为最后一个元素下标，n-1
    for i in range(n-1, -1, -1):
        #  当i指向当前堆的最后一个元素
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i-1)


list = [random.randint(1, 100) for i in range(122)]
print(topK(list, 10))
