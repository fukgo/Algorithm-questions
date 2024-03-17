"""
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。

再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。

重复第二步，直到所有元素均排序完毕。
"""
import random
import time
print(time.time())
def select_sort(li):
    new=[]
    for i in range(len(li)):
        min_val=min(li)  # min()函数是O(n)
        new.append(min_val)
        li.remove(min_val)  # remove()不是O(n)
    return new
li=[random.randint(0, 100000) for i in range(100000)]
#print(select_sort(li))

#两层循环就是O(n平分)
def select_sort_advance(li):
    for i in range(len(li)-1):
        min_loc=i  # 无序区的位置
        for j in range(i+1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc]=li[min_loc], li[i]
    return li
list = [6,458,5,2,45,42,75]
print(select_sort_advance(li))
print(time.time())


