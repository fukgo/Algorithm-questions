"""时间复杂度: O(n)"""
"""注意：mix_count已知数的范围在0，100之间"""
def count_sort(li, mix_count=100):
    count=[0 for i in range(mix_count+1)]
    for val in li:
        count[val]+=1
    li.clear()  # 清空列表
    for ind, val in enumerate(count):
        for i in range(val):
            li.append(ind)

def sys_sort(li):
    li.sort()

import random
li=[random.randint(1, 100) for _ in range(1, 1001)]
count_sort(li)
print(li)



