"""
桶排序：首先将元素分在不同的桶中，在对每个桶中的元素排序
"""

def bucket_sort(li, n=100, max_num=10000):
    """
    :param li:
    :param n: 桶的个数
    :param max_num: 最大数范围
    """
    buckets = [[] for _ in range(n)]
    for val in li:
        i = min(var // (max_num//n), n-1)  # var放在几号桶
        buckets[i].append(val)
        for j in range(len(buckets[i])-1, 0, -1):
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:
                break
    # 把排序好的二维列表buckets变成一维列表
    sorted_li=[]
    for bucket in buckets:
        sorted_li.append(bucket)
    return sorted_li




